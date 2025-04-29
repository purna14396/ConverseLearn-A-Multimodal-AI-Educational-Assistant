import base64
import os
import shutil
import tempfile
import time

import google.generativeai as genai
import speech_recognition as sr
import streamlit as st
from dotenv import load_dotenv  # 👈 Add this to load .env
from gtts import gTTS

# Load environment variables from .env file
load_dotenv()

# Get Gemini API key securely from environment
API_KEY = os.getenv("GEMINI_API_KEY")

# Configure Gemini API securely
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')


# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Create a persistent directory for audio files
if "audio_dir" not in st.session_state:
    st.session_state.audio_dir = tempfile.mkdtemp()


def autoplay_audio(file_path):
    """Function to create an HTML audio player with autoplay"""
    if not file_path or not os.path.exists(file_path):
        return

    with open(file_path, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        md = f"""
            <audio autoplay>
                <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
            """
        st.markdown(md, unsafe_allow_html=True)


def get_audio_input():
    """Function to capture audio input from user"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.sidebar.write("🎤 Listening... Speak now!")
        progress_bar = st.sidebar.progress(0)
        for i in range(100):
            time.sleep(0.01)
            progress_bar.progress(i + 1)
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            st.sidebar.success("Successfully recorded!")
            return text
        except sr.UnknownValueError:
            st.sidebar.error("Could not understand audio")
            return None
        except sr.RequestError:
            st.sidebar.error("Could not request results")
            return None


def get_conversation_response(text):
    """Function to get conversational response from Gemini"""
    prompt = f"""You are a friendly and helpful voice assistant. 
    Respond to this message naturally and conversationally: {text}
    Keep your response concise and friendly."""
    response = model.generate_content(prompt)
    return response.text


def text_to_speech(text, filename=None):
    """Function to convert text to speech"""
    try:
        tts = gTTS(text=text, lang='en')
        if filename is None:
            filename = os.path.join(st.session_state.audio_dir, f"audio_{int(time.time())}.mp3")
        tts.save(filename)
        return filename
    except Exception as e:
        st.error(f"Error in text-to-speech conversion: {str(e)}")
        return None


st.markdown("""
    <style>
    .stChatMessage {
        padding: 5px;
        border-radius: 15px;

        margin-bottom: 5px;
        
    }
    .css-1d391kg {
        padding-top: 3rem;
    }
    .stButton>button {
        width: 100%;
        margin-top: 20px;
    }
    .record-button {
        background-color: #FF4B4B;
        color: white;
        padding: 15px;
        border-radius: 50%;
        text-align: center;
        margin: 10px 0;
    }
    .chat-container {
        height: 250px;
        overflow-y: scroll;
        padding: 10px;
        border: 1px solid #ccc;
        border-radius: 10px;
        background-color: #3f5b6a;
        margin-bottom: -130px;
    }
    </style>
    """, unsafe_allow_html=True)


# Custom CSS Styling with Interactive Image
st.markdown("""
    <style>
    body {
        background-color: #021129;
    }
    .container {
        text-align: center;
        margin-top: -55px;
        margin-bottom: 15px;
        margin-left: -20px;
        z-index: 1000;
    }
    .robo img {
        height: 250px;
        border-radius: 40%;
        box-shadow: 0 0 10px rgba(0, 0, 255, 0.7);
        animation: pulse 2s infinite;
    }
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.05); }
        100% { transform: scale(1); }
    }
    </style>
    """, unsafe_allow_html=True)


# robo image 
st.markdown("""
    <div class="container">
            <div class="robo">
                <img src="https://i.postimg.cc/DZfqqQ5T/AI-Bot-image.png" alt="Bot Image">
            </div>
    </div>
    """, unsafe_allow_html=True)


with st.sidebar:
    st.header("Voice Controls")
    record_button = st.button("🎤 Start Recording", key="record_button", help="Click to start voice recording")
    st.markdown("---")
    if st.button("🗑️ Clear Chat History", key="clear"):
        st.session_state.messages = []
        st.rerun()

st.markdown("### Conversational AI")
chat_container = st.container()

with chat_container:
    messages_html = ""
    for message in st.session_state.messages:
        messages_html += f"<div class='stChatMessage'>{message['content']}</div>"
    st.markdown(f"""
        <div class="chat-container">
            {messages_html}
        </div>
        """, unsafe_allow_html=True)

if record_button:
    user_input = get_audio_input()
    if user_input:
        st.session_state.messages.append({"role": "user", "content": f"🎤 You said: {user_input}"})
        conversation_response = get_conversation_response(user_input)
        audio_file = text_to_speech(conversation_response)
        st.session_state.messages.append({"role": "assistant", "content": f"🤖 {conversation_response}", "audio": audio_file})
        st.rerun()



if len(st.session_state.messages) > 0 and "audio" in st.session_state.messages[-1] and st.session_state.messages[-1]["audio"]:
    autoplay_audio(st.session_state.messages[-1]["audio"])


import atexit


def cleanup():
    if hasattr(st.session_state, 'audio_dir') and os.path.exists(st.session_state.audio_dir):
        shutil.rmtree(st.session_state.audio_dir)

atexit.register(cleanup)
