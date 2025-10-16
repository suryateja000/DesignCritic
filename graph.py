from typing import TypedDict,Optional,List
from langgraph.graph import StateGraph,END
from utils.color import extract_palette
from nodes import review_with_image,design_systems_validator,chat_assistant

class DesignState(TypedDict):

    image_bytes:bytes
    colors:List[str]
    report:Optional[str]
    ds_findings:Optional[str]
    chat_history:List[dict]
    chat_reply:Optional[str]

def extract_colors_node(s:DesignState):

    return {"colors":extract_palette(s["image_bytes"])}

def build_graph():

    g=StateGraph(DesignState)

    g.add_node("extract_colors",extract_colors_node)

    g.add_node("review_with_image",review_with_image.run)
    g.add_node("design_systems_validator",design_systems_validator.run)
    g.add_node("chat_assistant",chat_assistant.run)

    g.set_entry_point("extract_colors")
    g.add_edge("extract_colors","review_with_image")
    g.add_edge("review_with_image","design_systems_validator")

    g.add_edge("design_systems_validator",END)

    return g.compile()