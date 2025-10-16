from typing import Dict,List,TypedDict,Optional
from langchain.schema import HumanMessage
from llm import get_llm
from utils.image import ensure_png_bytes,png_bytes_to_data_url

class DesignState(TypedDict):
    image_bytes:bytes
    colors:List[str]
    report:Optional[str]
    ds_findings:Optional[str]

llm=get_llm()

def run(state:DesignState)->Dict:
    
    palette=state["colors"]

    png=ensure_png_bytes(state["image_bytes"])
    data_url=png_bytes_to_data_url(png)
    parts=[
        {"type":"image_url","image_url":{"url":data_url}},
        {"type":"text","text":f"""You are a senior design auditor. Review this actual design image in context AND the given color palette. 
Return a concise, professional report in the EXACT format below for normal users to understand. 
Keep each bullet to one sentence. Use real WCAG contrast ratios for examples. 
Prefer evaluating real regions you can see in the image; use the palette for supporting evidence.

Palette: {palette}

RETURN THIS EXACT STRUCTURE (no extra text, no intros, no conclusions):

Title
- Palette verdict: <one sentence vibe/suitability>

Scores
- Overall: <0-100> (Grade: <A|B|C|D|F>)
- Accessibility: <0-100>
- Visual design: <0-100>

Use these together
- Good pairs (pass contrast):
  - <#text on #bg — X.Y:1>
  - <#text on #bg — X.Y:1>
  - <#text on #bg — X.Y:1>

Avoid these
- Failing pairs (don’t use):
  - <#text on #bg — X.Y:1 — Fail>
  - <#text on #bg — X.Y:1 — Fail>
  - <#text on #bg — X.Y:1 — Fail>

Accessibility
- Risks:
  - <plain-language risk 1 seen in the image>
  - <plain-language risk 2 seen in the image>
  - <plain-language risk 3 seen in the image>
- Fixes:
  - Use <#hex> for text/icons on dark backgrounds.
  - Replace <#hex> on dark with <#hex> for contrast.
  - Add accent <#hex> to avoid relying on one hue.

Visual design
- What works:
  - <one sentence on tone/brand fit seen in the image>
- What limits it:
  - <one sentence on monotony/hierarchy seen in the image>
- Fixes:
  - Add brighter blue <#hex> for interactive states.
  - Use light background <#hex> and subtle section <#hex>.
  - Reserve accent <#hex> for CTAs/alerts.

Ready-to-apply rules
- Body text on dark: use <#hex>.
- Buttons on dark: use <#hex> or <#hex> with bold weight.
- Accent for CTAs/alerts: <#hex> on <#hex>.
- Never place dark blue text on dark blue backgrounds.

Rules
- Keep every bullet to one sentence.
- Refer to specific areas in the image where applicable (e.g., header text on hero background).
- Use real hex codes from the palette or clearly introduced additions where fixes require.
- Use real contrast ratios where listed.
- Do not add any sections beyond what’s specified.
"""}]
    
    msg=HumanMessage(content=parts)
    r=llm.invoke([msg])

    
    return {"report":r.content}