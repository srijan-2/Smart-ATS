import streamlit as st
import google.generativeai as genai
import os
import PyPDF2 as pdf
from dotenv import load_dotenv
import json
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain 
from components.sidebar import sidebar
sidebar()
load_dotenv() ## load all our environment variables
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_repsonse(input):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content(input)
    return response.text

def input_pdf_text(uploaded_file):
    reader=pdf.PdfReader(uploaded_file)
    text=""
    for page in range(len(reader.pages)):
        page=reader.pages[page]
        text+=str(page.extract_text())
    return text

#Prompt Template

input_prompt="""
Hey Act Like a skilled or very experience ATS(Application Tracking System)
with a deep understanding of tech field,software engineering,data science ,data analyst
and big data engineer. Your task is to evaluate the resume based on the given job description.
You must consider the job market is very competitive and you should provide 
best assistance for improving their resumes. Assign the percentage Matching based 
on Jd and
the missing keywords with high accuracy
Resume:
{text}

Description:
{jd}

JD Match: {match_percentage}%
Missing Keywords: {missing_keywords}
Profile Summary: {profile_summary}


"""

## streamlit app
st.header("Smart ATS")

st.subheader('Improve your resume with AI', divider='rainbow')
jd=st.text_area("Paste the Job Description")
uploaded_file=st.file_uploader("Upload Your Resume",type="pdf",help="Please upload the pdf")

st.markdown('---')

submit = st.button("Match Percentage", type="primary",help="Click to check percentage match of your resume with JD", use_container_width= True)

projects = st.button("Projects Suggestions",help="Click to get projects ideas based on the JD",use_container_width= True)


certificate = st.button("Suggest Certification Courses", type="primary",help="Click to get certification courses link for the given JD",use_container_width= True)


cover = st.button("Write cover letter for me",help="Click here to write a custom cover letter for the given JD",use_container_width= True)
prompt = jd

# Prompt templates
project_template = PromptTemplate(
    input_variables = ['topic'], 
    template='Suggest me projects to improve my resume based on the job description {topic}'
)
certificate_template = PromptTemplate(
    input_variables = ['topic'], 
    template='Suggest me certificate course with link to improve my resume based on the job description {topic}'
)
cover_template = PromptTemplate(
    input_variables = ['topic', 'resume'], 
    template=' Write a cover letter with help of resume based on the job description {topic}'
)
llm = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=GOOGLE_API_KEY)
project_chain = LLMChain(llm=llm, prompt=project_template, verbose=True)
certificate_chain = LLMChain(llm=llm, prompt=certificate_template, verbose=True)
cover_chain = LLMChain(llm=llm, prompt=cover_template, verbose=True)

if submit:
    if uploaded_file is not None:
        text=input_pdf_text(uploaded_file)
        response=get_gemini_repsonse(input_prompt)
        st.subheader(response)
if projects:
    response = project_chain.run(topic = prompt)
    st.write(response)
    
if certificate:
    response = certificate_chain.run(topic = prompt)
    st.write(response)
    
if cover:
    response = cover_chain.run(topic = prompt)
    st.write(response)
    