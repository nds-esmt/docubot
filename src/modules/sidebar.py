import streamlit as st
from trubrics.integrations.streamlit import FeedbackCollector



class Sidebar:

    MODEL_OPTIONS = ["gpt-3.5-turbo", "gpt-4"]
    TEMPERATURE_MIN_VALUE = 0.0
    TEMPERATURE_MAX_VALUE = 1.0
    TEMPERATURE_DEFAULT_VALUE = 0.0
    TEMPERATURE_STEP = 0.01

    @staticmethod
    def about():
        about = st.sidebar.expander("🧠 About DocuBot ")
        sections = [
            "#### DocuBot is an AI chatbot with a conversational memory, designed to allow users to discuss their data in a more intuitive way. 📄",
            "#### It uses large language models to provide users with natural language interactions about user data content. 🌐",
            "#### Powered by [Langchain](https://github.com/hwchase17/langchain), [OpenAI](https://platform.openai.com/docs/models/gpt-3-5) and [Streamlit](https://github.com/streamlit/streamlit) ⚡",
            "#### Adapted from [yvann-hub/Robby-chatbot](https://github.com/yvann-hub/Robby-chatbot) by [nds-esmt](https://github.com/nds-esmt)",
        ]
        for section in sections:
            about.write(section)

    @staticmethod
    def disclaimer():
        with st.sidebar.expander("⚠️ Disclaimer"):
    
            st.markdown("""
            Large language models are trained on massive text datasets to predict words based on context. They can generate remarkably human-like text, but they have no real understanding - just excellent pattern recognition.

            Any output received here may be biased, inaccurate, or nonsensical. Although DocuBot draws its information from documents you provide, it may only receive a limited subset of the document data with a given query — thus answers received may be incomplete or incorrect.
                        
            You should verify any information DocuBot provides. Remember, this is just a tool - the responsibility lies with you, the user.
            """)

    @staticmethod
    def reset_chat_button():
        if st.button("Reset chat"):
            st.session_state["reset_chat"] = True
        st.session_state.setdefault("reset_chat", False)

    def model_selector(self):
        model = st.selectbox(label="Model", options=self.MODEL_OPTIONS)
        st.session_state["model"] = model

    def temperature_slider(self):
        temperature = st.slider(
            label="Temperature",
            min_value=self.TEMPERATURE_MIN_VALUE,
            max_value=self.TEMPERATURE_MAX_VALUE,
            value=self.TEMPERATURE_DEFAULT_VALUE,
            step=self.TEMPERATURE_STEP,
        )
        st.session_state["temperature"] = temperature
        
    def show_options(self):
        with st.sidebar.expander("🛠️ DocuBot Tools", expanded=False):

            self.reset_chat_button()
            self.model_selector()
            self.temperature_slider()
            st.session_state.setdefault("model", self.MODEL_OPTIONS[0])
            st.session_state.setdefault("temperature", self.TEMPERATURE_DEFAULT_VALUE)

    def feedback(self):
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
    