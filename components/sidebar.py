import streamlit as st

from components.faq import faq
from dotenv import load_dotenv
import os

load_dotenv()


def sidebar():
    with st.sidebar:
        st.markdown(
            "## How to use\n"
            "1. Paste your Job description🔑\n"  # noqa: E501
            "2. Upload resume in pdf or mp4📄\n"
            "3. Get answers for your questions💬\n"
        )

        st.markdown("---")
        st.markdown("# About")
        st.markdown(
            "📖Smart ATS allows you to answer about your "
            "job description and resume . "
        )
        st.markdown(
            "This tool is a work in progress. "
            "You can contribute to the project on [GitHub](https://github.com/mmz-001/knowledge_gpt) "  # noqa: E501
            "with your feedback and suggestions💡"
        )

        st.markdown("---")

        faq()