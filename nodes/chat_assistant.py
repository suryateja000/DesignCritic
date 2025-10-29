from typing import Dict, List, Optional, TypedDict
from langchain_core.messages import HumanMessage, SystemMessage
from llm import get_llm
from rag.retriever import retrieve


class DesignState(TypedDict):
    image_bytes: bytes
    colors: List[str]
    report: Optional[str]
    ds_findings: Optional[str]
    chat_history: List[Dict[str, str]]
    chat_reply: Optional[str]


llm = get_llm(temperature=0.2)


SYSTEM_PROMPT = """
You are DesignCritic Chat, a senior design reviewer.

SCOPE: Only discuss:
- Colors, palettes, tokens
- Contrast ratios (WCAG 2.1 AA/AAA)
- Accessibility (visual design only)
- Components (buttons, cards) and their states
- Spacing grids (8dp/4px systems)
- Typography (hierarchy, scale, weight, line height)
- Design guidelines: Material Design, Apple HIG, Fluent, Ant Design

OFF‑TOPIC RULE: If the user asks anything outside this scope (e.g., math like "2+2", general knowledge, personal questions), respond with EXACTLY this sentence and nothing else:
"Please ask a design-related question (colors, contrast/WCAG, components, spacing, typography, Material/HIG/Fluent/Ant) according to your uploaded photo."

STYLE:
- Be concise: 3–6 bullets or 1–2 short paragraphs
- Include hex codes and contrast ratios when relevant
- If the user asks a yes/no question within scope, respond "Yes." or "No." followed by a short clause

CITATIONS:
- Cite only from provided "Guideline excerpts" using format (System • Section • Topic)
- If no excerpts are present, do not invent citations; focus on design review and palette
"""


FEW_SHOTS = [
    ("user", "2+2?"),
    ("assistant", "Please ask a design-related question (colors, contrast/WCAG, components, spacing, typography, Material/HIG/Fluent/Ant) according to your uploaded photo."),
    
    ("user", "Is #1499dd on #141e63 accessible for body text? Just yes or no."),
    ("assistant", "No. The contrast ratio is 3.45:1, which is below the WCAG AA minimum of 4.5:1 for normal text."),
    
    ("user", "How is the color palette? Any issues?"),
    ("assistant", "The palette is visually cohesive, but #888888 on white lacks sufficient contrast (2.89:1). Consider using darker tones for body text to meet WCAG AA."),
    
    ("user", "Are the button states compliant with Material Design?"),
    ("assistant", "Yes. The hover, focus, and disabled states follow Material guidelines with appropriate elevation, opacity, and color feedback."),
    
    ("user", "Is the spacing grid consistent?"),
    ("assistant", "Mostly consistent with an 8dp base grid, but some card margins use 6dp instead of 8dp multiples. Recommend aligning all spacing to 8dp increments."),
    
    ("user", "Is the typography hierarchy clear?"),
    ("assistant", "Yes. The use of 32px bold headers, 20px subheaders, and 16px body text creates a clear hierarchy. Line height and weight are well balanced.")
]


def run(state: DesignState) -> Dict:
    cols = state.get("colors", [])
    rep = state.get("report") or ""
    find = state.get("ds_findings") or ""
    hist = state.get("chat_history", [])
    q = ""

    for h in reversed(hist):
        if h.get("role") == "user":
            q = h.get("content", "")
            break

    qry = (f"{q} buttons outlined filled tonal elevated states spacing 8dp 4px layout "
           f"cards elevation shadows contrast wcag accessibility material hig fluent ant "
           f"palette {cols} {rep[:800]} {find[:800]}")
    
    res = retrieve(query=qry, k=6)
    st = []

    for e in res:
        st.append(
            f"- {e.get('system', 'Unknown')} • {e.get('section', '(No section)')} • {e.get('topic', '(No topic)')}\n"
            f"  Source: {e.get('source_url', '(No URL)')}\n"
            f"  Excerpt: {e.get('content', '')[:380]}..."
        )

    gctx = "\n".join(st) if st else "No guideline excerpts retrieved."

    ctx = (f"Palette: {cols}\n\n"
           f"Design Review:\n{rep}\n\n"
           f"Design Systems Validator:\n{find}\n\n"
           f"Guideline excerpts:\n{gctx}\n")
    
    msgs = [SystemMessage(content=SYSTEM_PROMPT)]
    
    for role, text in FEW_SHOTS:
        if role == "user":
            msgs.append(HumanMessage(content=[{"type": "text", "text": text}]))
        else:
            msgs.append(SystemMessage(content=text))

    msgs.append(HumanMessage(content=[{"type": "text", "text": f"Context:\n{ctx}"}]))
    msgs.append(HumanMessage(content=[{"type": "text", "text": q}]))
    
    r = llm.invoke(msgs)

    return {"chat_reply": r.content}
