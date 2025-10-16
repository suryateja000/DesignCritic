from typing import Dict,List,Optional,TypedDict
from langchain.schema import HumanMessage,SystemMessage
from llm import get_llm
from rag.retriever import retrieve

class DesignState(TypedDict):
    image_bytes:bytes
    colors:List[str]
    report:Optional[str]
    ds_findings:Optional[str]
    chat_history:List[Dict[str,str]]
    chat_reply:Optional[str]

llm=get_llm(temperature=0.2)

SYSTEM_PROMPT="""You are DesignCritic Chat, a senior design reviewer.
SCOPE: Only discuss colors/palettes/tokens, contrast (WCAG), accessibility, components (buttons/cards) and states, spacing grids (8dp/4px), typography, and guidelines (Material, Apple HIG, Fluent, Ant).
OFF‑TOPIC RULE: If the user asks anything outside the scope (e.g., math like “2+2”, general knowledge, personal questions), respond with EXACTLY this sentence and nothing else:
"Please ask a design-related question (colors, contrast/WCAG, components, spacing, typography, Material/HIG/Fluent/Ant) according to your uploaded photo."

STYLE
- Be concise (3–6 bullets or 1–2 short paragraphs).
- Include hex codes and contrast ratios when relevant.
- If the user explicitly asks for yes/no on an in-scope question, reply "Yes." or "No." followed by a single short clause.
CITATIONS:
- You may cite only items present in the provided "Guideline excerpts" by writing (System • Section • Topic).
- If no excerpts are present, do not invent citations; focus on the provided design review and palette.
"""

FEW_SHOTS=[
    ("user","2+2?"),
    ("assistant","Please ask a design-related question (colors, contrast/WCAG, components, spacing, typography, Material/HIG/Fluent/Ant) according to your uploaded photo."),
    ("user","Is #1499dd on #141e63 accessible for body text? Just yes or no."),
    ("assistant","No. The contrast is below the required 4.5:1 for body text."),
    ("user","How is the color palette? Any issues?"),
    ("assistant","The color palette is well-balanced, but consider increasing the contrast between text and background colors.")
]

def run(state:DesignState)->Dict:
    cols=state.get("colors",[])
    rep=state.get("report") or ""
    find=state.get("ds_findings") or ""
    hist=state.get("chat_history",[])
    q=""


    for h in reversed(hist):
        if h.get("role")=="user":
            q=h.get("content","")
            break

    qry=(f"{q} buttons outlined filled tonal elevated states spacing 8dp 4px layout "
         f"cards elevation shadows contrast wcag accessibility material hig fluent ant "
         f"palette {cols} {rep[:800]} {find[:800]}")
    


    res=retrieve(query=qry,k=6)
    st=[]

    for e in res:
        st.append(
            f"- {e.get('system','Unknown')} • {e.get('section','(No section)')} • {e.get('topic','(No topic)')}\n"
            f"  Source: {e.get('source_url','(No URL)')}\n"
            f"  Excerpt: {e.get('content','')[:380]}..."
        )

    gctx="\n".join(st) if st else "No guideline excerpts retrieved."

    ctx=(f"Palette: {cols}\n\n"
         f"Design Review:\n{rep}\n\n"
         f"Design Systems Validator:\n{find}\n\n"
         f"Guideline excerpts:\n{gctx}\n")
    

    msgs=[SystemMessage(content=SYSTEM_PROMPT)]
    for role,text in FEW_SHOTS:
        if role=="user":
            msgs.append(HumanMessage(content=[{"type":"text","text":text}]))
        else:
            msgs.append(SystemMessage(content=text))

    msgs.append(HumanMessage(content=[{"type":"text","text":f"Context:\n{ctx}"}]))
    msgs.append(HumanMessage(content=[{"type":"text","text":q}]))
    r=llm.invoke(msgs)

    return {"chat_reply":r.content}