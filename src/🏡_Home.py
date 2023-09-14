import streamlit as st
from trubrics.integrations.streamlit import FeedbackCollector

#Config
st.set_page_config(layout="wide", page_icon="💬", page_title="DocuBot")


#About
with st.sidebar.expander("🧠 About"):

    st.markdown("""
DocuBot was adapted from [yvann-hub/Robby-chatbot](https://github.com/yvann-hub/Robby-chatbot) by [nds-esmt](https://github.com/nds-esmt)
""", unsafe_allow_html=True)

#Disclaimer
with st.sidebar.expander("⚠️ Disclaimer"):
    
    st.markdown("""
Large language models are trained on massive text datasets to predict words based on context. They can generate remarkably human-like text, but they have no real understanding - just excellent pattern recognition.

Any output received here may be biased, inaccurate, or nonsensical. Although DocuBot draws its information from documents you provide, it may only receive a limited subset of the document data with a given query — thus answers received may be incomplete or incorrect.
                
You should verify any information DocuBot provides. Remember, this is just a tool - the responsibility lies with you, the user.
    """)

#Feedback
collector = FeedbackCollector(
            project="docubot",
            email=st.secrets.TRUBRICS_EMAIL,
            password=st.secrets.TRUBRICS_PASSWORD,
        )

with st.sidebar.expander("📩 Feedback", expanded=False):
        collector.st_feedback(
            component="gen feedback",
            feedback_type="textbox",
            model="gpt-3.5-turbo",
            prompt_id=None,  # see prompts to log prompts and model generations
            open_feedback_label='Please report bugs and provide any feedback here'
        )

#Title
st.markdown(
    """
    <h2 style='text-align: center;'>Hi, I am DocuBot</h1>
    """,
    unsafe_allow_html=True,)

st.markdown("---")


#Description
st.markdown(
    """ 
    <h5 style='text-align:center;'> Upload your documents and then ask me questions about them. You can upload PDFs, TXTs, & CSVs 🧠</h5>
    """,
    unsafe_allow_html=True)
st.markdown("---")


#Pages
st.write("""
- **Document Chat**: General Chat about data (PDF, TXT,CSV) with a [vectorstore](https://github.com/facebookresearch/faiss) (index useful parts (max 4) with which to respond to the user) | works with [ConversationalRetrievalChain](https://python.langchain.com/en/latest/modules/chains/index_examples/chat_vector_db.html)
- **Sheet Chat** (beta): Chat about tabular data (CSV) | for precise information | process the whole file | works with [CSV_Agent](https://python.langchain.com/en/latest/modules/agents/toolkits/examples/csv.html) + [PandasAI](https://github.com/gventuri/pandas-ai) for data manipulation and graph creation. Note: This is a beta version and as such is less reliable and may throw errors.
""")
st.markdown("---")







