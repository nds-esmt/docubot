import streamlit as st


#Config
st.set_page_config(layout="wide", page_icon="💬", page_title="STEVE | DocBot")


#About
with st.sidebar.expander("About"):

    st.markdown("""
**STEVE was adapted from [yvann-hub/Robby-chatbot](https://github.com/yvann-hub/Robby-chatbot) by [nds-esmt](https://github.com/nds-esmt)**
""", unsafe_allow_html=True)


#Title
st.markdown(
    """
    <h2 style='text-align: center;'>Hi, I'm STEVE</h1>
    """,
    unsafe_allow_html=True,)

st.markdown("---")


#Description
st.markdown(
    """ 
    <h5 style='text-align:center;'> I eat your docs and then talk to you about them. I eat PDFs, TXTs, CSVs, & Youtube transcripts 🧠</h5>
    """,
    unsafe_allow_html=True)
st.markdown("---")


#Pages
st.subheader("variations of STEVE")
st.write("""
- **STEVE-Chat**: General Chat about data (PDF, TXT,CSV) with a [vectorstore](https://github.com/facebookresearch/faiss) (index useful parts (max 4) with which to respond to the user) | works with [ConversationalRetrievalChain](https://python.langchain.com/en/latest/modules/chains/index_examples/chat_vector_db.html)
- **STEVE-Sheet** (beta): Chat about tabular data (CSV) | for precise information | process the whole file | works with [CSV_Agent](https://python.langchain.com/en/latest/modules/agents/toolkits/examples/csv.html) + [PandasAI](https://github.com/gventuri/pandas-ai) for data manipulation and graph creation
- **STEVE-Tube**: Summarize YouTube videos with [summarize-chain](https://python.langchain.com/en/latest/modules/chains/index_examples/summarize.html)
""")
st.markdown("---")







