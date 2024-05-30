import os
import streamlit as st
import moviepy.editor as mp
import speech_recognition as sr
from pydub import AudioSegment
from pydub.silence import split_on_silence
from dotenv import load_dotenv
import google.generativeai as genai



# Function to convert video to audio
def video_to_audio(in_path):
    out_path = 'sample_audio.wav'  # Output audio file path
    video = mp.VideoFileClip(in_path)
    video.audio.write_audiofile(out_path)
    return out_path

# Function to transcribe large audio files to text
def large_audio_to_text(path):
    sound = AudioSegment.from_wav(path)
    chunks = split_on_silence(sound, min_silence_len=700, silence_thresh=sound.dBFS-14, keep_silence=700)
    folder_name = "audio-chunks"
    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)
    whole_text = ""
    for i, audio_chunk in enumerate(chunks, start=1):
        chunk_filename = os.path.join(folder_name, f"chunk{i}.wav")
        audio_chunk.export(chunk_filename, format="wav")
        with sr.AudioFile(chunk_filename) as source:
            audio_listened = r.record(source)
            try:
                text = r.recognize_google(audio_listened)
            except sr.UnknownValueError as e:
                print("Error:", str(e))
            else:
                text = f"{text.capitalize()}. "
                print(chunk_filename, ":", text)
                whole_text += text
    with open('result.txt', 'w') as file:
        file.write(whole_text)
    return whole_text

r = sr.Recognizer()

# Configure Google API key
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to get Gemini response
def get_gemini_response(input):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(input)
    return response.text

model=genai.GenerativeModel("gemini-pro") 
chat = model.start_chat(history=[])
def get_gemini_response_chat(question):
    
    response=chat.send_message(question,stream=True)
    return response

# Initialize session state for chat history if it doesn't exist
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []
    

# Streamlit app
st.title("Smart ATS")
st.text("Improve Your Resume ATS")
jd = st.text_area("Paste the Job Description")
uploaded_video = st.file_uploader("Upload Your Video Resume", help="Please upload the video file")
submit = st.button("Submit")

input=st.text_input("Input: ",key="input")
submit1=st.button("Ask the question")



if submit:
    if uploaded_video is not None:
        video_path = "uploaded_video.mp4"
        with open(video_path, 'wb') as f:
            f.write(uploaded_video.read())
        audio_path = video_to_audio(video_path)
        result_text = large_audio_to_text(audio_path)
        input_prompt = f"""
        Hey Act Like a skilled or very experienced ATS (Application Tracking System)
        with a deep understanding of the tech field, software engineering, data science, data analysis,
        and big data engineering. Your task is to evaluate the resume based on the given job description.
        You must consider the job market is very competitive and you should provide the best assistance 
        for improving the resumes. Assign the percentage matching based on JD and the missing keywords 
        with high accuracy. Resume: {result_text} Description: {jd}
        
        I want the response in one single string having the structure
        {{"JD Match":"%","MissingKeywords":[],"Profile Summary":""}}
        """
        response = get_gemini_response(input_prompt)
        st.subheader(response)
    

if submit1 and input:
    response=get_gemini_response_chat(input)
    # Add user query and response to session state chat history
    st.session_state['chat_history'].append(("You", input))
    st.subheader("The Response is")
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("Bot", chunk.text))
st.subheader("The Chat History is")
    
for role, text in st.session_state['chat_history']:
    st.write(f"{role}: {text}")