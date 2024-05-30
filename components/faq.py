# flake8: noqa
import streamlit as st


def faq():
    st.markdown(
        """
# FAQ
## How does SmartATS work?
Users input a job description and upload their resume. 
SmartATS then evaluates the resume against the job description, calculating the match percentage and identifying areas for improvement.
It provides tailored recommendations, such as project suggestions, certification courses, and custom cover letters, to enhance the resume's competitiveness.
Overall, it leverages AI to offer personalized guidance and optimize the job application experience.

## Is my data safe?
Yes, your data is safe with SmartATS.
We prioritize your privacy by not storing any of your uploaded documents or questions.
Once you close the browser tab, all uploaded data is automatically deleted, ensuring that your information remains secure and confidential. 
You can use the system with confidence, knowing that your data is handled responsibly and protected throughout your session.

## Why does it take so long to index my document?
Using a free Google Gemini API key may cause delays in document indexing due to strict rate limits imposed
on free accounts. These limits restrict the amount of processing that can be done within a given timeframe, 
resulting in longer processing times for document indexing.To speed up the indexing process, you can use a paid API key.

## What do the numbers mean under each source?
For a PDF document, you will see a citation number like this: 3-12. 
The first number is the page number and the second number is 
the chunk number on that page. For DOCS and TXT documents, 
the first number is set to 1 and the second number is the chunk number.

The numbers under each source indicate the location of information within the document.
In a PDF, the format is page number followed by chunk number (e.g., 3-12), where the first number represents the page and the second number represents the chunk on that page.
For DOCS and TXT documents, the page number is always 1, and the second number denotes the chunk number.

## Are the answers 100% accurate?
No, the answers aren't 100% accurate.
SmartATS employs Gemini to generate responses.
While Gemini is potent, it can err and sometimes produce irrelevant content.
Additionally, SmartATS employs semantic search, focusing on relevant chunks rather than the entire document, 
potentially missing some information, particularly for summary-type questions or those requiring extensive document context.

But for most use cases, SmartATS is very accurate and can answer
most questions. Always check with the sources to make sure that the answers
are correct.
"""
    )