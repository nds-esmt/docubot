import os
import streamlit as st
import re
from modules.layout import Layout
from modules.utils import Utilities
from modules.sidebar import Sidebar
from youtube_transcript_api import YouTubeTranscriptApi
from langchain.chains.summarize import load_summarize_chain
from langchain.chains import AnalyzeDocumentChain
from youtube_transcript_api import YouTubeTranscriptApi
from langchain.llms import OpenAI
import os
from langchain.text_splitter import CharacterTextSplitter

st.set_page_config(layout="wide", page_icon="💬", page_title="STEVE | DocBot")

# Instantiate the main components
layout, sidebar, utils = Layout(), Sidebar(), Utilities()

st.markdown(
    f"""
    <h1 style='text-align: center;'> Ask STEVE to summarize youtube video !</h1>
    """,
    unsafe_allow_html=True,
)

user_api_key = utils.load_api_key()

sidebar.about()

def main():
    if not user_api_key:
        layout.show_api_key_missing()

    else:
        os.environ["OPENAI_API_KEY"] = user_api_key

        script_docs = []

        def get_youtube_id(url):
            video_id = None
            match = re.search(r"(?<=v=)[^&#]+", url)
            if match :
                video_id = match.group()
            else : 
                match = re.search(r"(?<=youtu.be/)[^&#]+", url)
                if match :
                    video_id = match.group()
            return video_id

        video_url = st.text_input(placeholder="Enter Youtube Video URL", label_visibility="hidden", label =" ")
        if video_url :
            video_id = get_youtube_id(video_url)

            if video_id != "":
                t = YouTubeTranscriptApi.get_transcript(video_id, languages=('en','fr','es', 'zh-cn', 'hi', 'ar', 'bn', 'ru', 'pt', 'sw' ))
                finalString = ""
                for item in t:
                    text = item['text']
                    finalString += text + " "

                text_splitter = CharacterTextSplitter()
                chunks = text_splitter.split_text(finalString)

                summary_chain = load_summarize_chain(OpenAI(temperature=0),
                                                chain_type="map_reduce",verbose=True)
                
                summarize_document_chain = AnalyzeDocumentChain(combine_docs_chain=summary_chain)

                answer = summarize_document_chain.run(chunks)

                st.subheader(answer)

def check_password():
    """Returns `True` if the user had the correct password."""

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if st.session_state["password"] == st.secrets["password"]:
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # don't store password
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        # First run, show input for password.
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        return False
    elif not st.session_state["password_correct"]:
        # Password not correct, show input + error.
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        st.error("😕 Password incorrect")
        return False
    else:
        # Password correct.
        return True

if check_password():
    system_msg = ""
    main()