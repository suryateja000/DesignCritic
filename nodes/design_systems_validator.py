from typing import Dict,List,Optional,TypedDict
from langchain.schema import HumanMessage
from llm import get_llm
from rag.retriever import retrieve,ALL_ENTRIES

class DesignState(TypedDict):
    image_bytes:bytes
    colors:List[str]
    report:Optional[str]
    ds_findings:Optional[str]

llm=get_llm()

PROMPT="""You are the Design Systems Validator. Using the design context and the retrieved guideline excerpts, list concise violations and map each to its source.

Return exactly:

Design Systems Validator
- Summary: <one sentence>
- Violations:
  - <violation> — <system • section • topic> (source: URL)
  - <violation> — <system • section • topic> (source: URL)
  - <violation> — <system • section • topic> (source: URL)
- Recommendations:
  - <fix mapped to guideline>
  - <fix mapped to guideline>
  - <fix mapped to guideline>
"""

def run(state:DesignState)->Dict:
    
    palette=state.get("colors",[])
    prior=(state.get("report") or "")[:1600]
    query=("design system validation "
           "buttons button states primary secondary text outlined tonal elevated "
           "cards elevation shadows spacing 8dp 4px grid layout typography color contrast accessibility wcag "
           "material design apple hig fluent ant design "
           f"palette {palette} "
           f"{prior}")

    hits=retrieve(query=query,k=8)
    if not hits:
        fallback=("Design Systems Validator\n"
                  "- Summary: No relevant guidelines found. Ensure rag/docs/*.rd exist and are loaded.\n"
                  "- Violations:\n"
                  "  - N/A\n"
                  "- Recommendations:\n"
                  "  - Add/expand .rd files and reload.\n")
        return {"ds_findings":fallback}
    

    stit=[]
    for e in hits:
        stit.append(
            f"- {e.get('system','Unknown')} • {e.get('section','(No section)')} • {e.get('topic','(No topic)')}\n"
            f"  Source: {e.get('source_url','(No URL)')}\n"
            f"  Excerpt: {e.get('content','')[:400]}..."
        )
    context="\n".join(stit)

    full=(f"{PROMPT}\n\n"
          f"Design context (palette + review excerpt):\n{palette}\n{prior}\n\n"
          f"Guideline excerpts:\n{context}\n")
    

    msg=HumanMessage(content=[{"type":"text","text":full}])
    resp=llm.invoke([msg])


    return {"ds_findings":resp.content}