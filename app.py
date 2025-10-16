import os,base64,mimetypes,streamlit as st
from typing import TypedDict,Optional,List
from graph import build_graph
from rag.retriever import load_all
from nodes import chat_assistant

BASE_DIR=os.path.dirname(os.path.abspath(__file__))
DOCS_DIR=os.path.join(BASE_DIR,"rag","docs")
load_all(DOCS_DIR)

class DesignState(TypedDict):
    image_bytes:bytes
    colors:List[str]
    report:Optional[str]
    ds_findings:Optional[str]

graph=build_graph()

def make_data_url(uploaded_file)->str:

    raw=uploaded_file.getvalue()
    mime=uploaded_file.type or mimetypes.guess_type(uploaded_file.name)[0] or "image/png"
    b64=base64.b64encode(raw).decode("utf-8")

    return f"data:{mime};base64,{b64}"

def display_results_interactive(result:DesignState):

    if report:=result.get("report"):

        st.subheader("Design Review")
        with st.expander("View Accessibility and Visual Design Report",expanded=True):
            st.markdown(report,unsafe_allow_html=True)

    else:

        st.warning("The Design Review report could not be generated.")

    if ds_findings:=result.get("ds_findings"):

        st.subheader("Design Systems Validator")
        with st.expander("View Design System Compliance Details",expanded=False):
            st.markdown(ds_findings,unsafe_allow_html=True)

    else:

        st.warning("The Design Systems Validator report could not be generated.")


    if colors:=result.get("colors"):

        st.subheader("Extracted Palette")
        cols=st.columns(len(colors))

        for i,color in enumerate(colors):
            with cols[i]:
                try:
                    brightness=sum(int(color[j:j+2],16) for j in (1,3,5))
                    text_color='white' if brightness<382 else 'black'
                    st.markdown(f"""<div style="background-color:{color};height:80px;border-radius:8px;border:2px solid #ddd;display:flex;align-items:center;justify-content:center;color:{text_color};font-weight:600">{color}</div>""",unsafe_allow_html=True)
                except Exception:
                    st.error(f"Invalid color value: {color}")
    st.write("---")

    with st.expander("Download Reports",expanded=False):
        col1,col2=st.columns(2)
        with col1:
            st.download_button(label="📥 Download Design Review",data=result.get("report",""),file_name="design_review.md",mime="text/markdown",use_container_width=True)
        with col2:
            st.download_button(label="📥 Download DS Findings",data=result.get("ds_findings",""),file_name="design_systems_validator.md",mime="text/markdown",use_container_width=True)


st.set_page_config(page_title="DesignCritic AI — Interactive Results",page_icon="🎨",layout="wide")
st.title("🎨 DesignCritic AI")
st.caption("Image Review + Palette Analysis + Design Systems Validator (Material, Apple HIG, Fluent, Ant)")

if 'analysis_result' not in st.session_state:
    st.session_state['analysis_result']=None

if 'chat_history' not in st.session_state:
    st.session_state['chat_history']=[]
uploaded=st.file_uploader("Upload a design image",type=["png","jpg","jpeg"])
col_analyze,col_clear=st.columns([1,1])
with col_analyze:

    analyze_clicked=st.button("🚀 Analyze Design",type="primary",use_container_width=True)
with col_clear:
    if st.button("🗑️ Clear Session",use_container_width=True):
        st.session_state['analysis_result']=None
        st.session_state['chat_history']=[]
        st.toast("Session cleared.",icon="🧹")
        st.rerun()
if analyze_clicked and not uploaded:
    st.warning("Please upload an image to analyze.")

elif analyze_clicked and uploaded:
    initial_state:DesignState={"image_bytes":uploaded.getvalue(),"colors":[],"report":None,"ds_findings":None}
    with st.spinner("🚀 Running analysis... This may take a moment."):
        try:
            result=graph.invoke(initial_state)
            result["image_bytes"]=initial_state["image_bytes"]
            st.session_state['analysis_result']=result
            st.success("Analysis complete.")
        except Exception as e:
            st.error(f"An error occurred during analysis: {e}")
            st.session_state['analysis_result']=None
result=st.session_state['analysis_result']

if result:
    st.write("---")
    st.header("Analysis Results")
    display_results_interactive(result)
else:

    st.info("Upload an image and click Analyze to get a review and validator report.")
st.write("---")

st.subheader("Chat with DesignCritic")
for turn in st.session_state['chat_history'][-14:]:
    if turn["role"]=="assistant":
        with st.chat_message("assistant"):
            st.markdown(turn["content"])
    else:
        with st.chat_message("user"):
            st.markdown(turn["content"])
user_msg=st.chat_input("Ask about colors, contrast, components, spacing, or guidelines...")
if user_msg:
    st.session_state['chat_history'].append({"role":"user","content":user_msg})
    with st.chat_message("user"):
        st.markdown(user_msg)
    if not st.session_state['analysis_result']:
        guidance="Please upload an image and click Analyze first so I can reference your palette, review, and design-system checks."
        st.session_state['chat_history'].append({"role":"assistant","content":guidance})
        with st.chat_message("assistant"):
            st.markdown(guidance)
    else:
        with st.chat_message("assistant"):

            thinking=st.empty()
            thinking.markdown("_DesignCritic is thinking…_")
        ctx=st.session_state['analysis_result']
        chat_state={

            "image_bytes":ctx.get("image_bytes",b""),
            "colors":ctx.get("colors",[]),
            "report":ctx.get("report",""),
            "ds_findings":ctx.get("ds_findings",""),
            "chat_history":st.session_state['chat_history'],
            "chat_reply":None,
        }
        try:

            out=chat_assistant.run(chat_state)
            reply=out.get("chat_reply","")

        except Exception as e:

            reply=f"Sorry, something went wrong generating a reply: {e}"
        thinking.markdown(reply)
        st.session_state['chat_history'].append({"role":"assistant","content":reply})
