import streamlit as st
import google.generativeai as genai
import speech_recognition as sr
import os
import time
import base64
import tempfile
import shutil
import random
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Securely get the Gemini API key
API_KEY = os.getenv("GEMINI_API_KEY")

# Configure Gemini API securely
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')


# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

if "audio_dir" not in st.session_state:
    st.session_state.audio_dir = tempfile.mkdtemp()

if "topic" not in st.session_state:
    st.session_state.topic = ""

TOPICS = [
    "Is online education better than traditional education?",
    "Future of electric vehicles",
    "Social media: Connecting or isolating people?",
    "Cryptocurrency: Hype or future?",
    "Space exploration: Worth the cost?",
    "The impact of globalization on culture",
    "Should plastic be completely banned?",
    "Is remote work the future?",
    "Privacy vs Security in the digital age",
    "Role of youth in nation-building",
    "Can renewable energy replace fossil fuels?",
    "Impact of Artificial Intelligence on healthcare",
    "Is social media a reliable source of news?",
    "The importance of financial literacy",
    "Will robots replace humans in jobs?",
    "Importance of physical fitness in daily life",
    "Can gaming be a career option?",
    "Does technology make life easier or complicated?",
    "Effects of fast food on health",
    "Does social media influence elections?",
    "Impact of automation on employment",
    "Importance of gender equality in society",
    "Should voting be made mandatory?",
    "Is climate change reversible?",
    "Impact of digital payments on society",
    "Role of media in shaping public opinion",
    "Importance of work-life balance",
    "Do video games promote violence?",
    "Is time travel possible?",
    "Can money buy happiness?",
    "Impact of movies on society",
    "Is artificial intelligence a threat to humanity?",
    "Should education be free for all?",
    "Does technology disconnect us from nature?",
    "Can renewable energy solve the energy crisis?",
    "Is space tourism ethical?",
    "The rise of influencer marketing",
    "Impact of fast fashion on the environment",
    "Should animal testing be banned?",
    "Importance of cybersecurity awareness",
    "Is nuclear energy a sustainable option?",
    "Role of youth in environmental conservation",
    "Are self-driving cars safe?",
    "Should junk food advertisements be banned?",
    "Impact of virtual reality on society",
    "Are electric cars really eco-friendly?",
    "Should social media have age restrictions?",
    "The future of online shopping",
    "Is technology making us lazy?",
    "Role of Artificial Intelligence in crime prevention",
    "Should we colonize Mars?"
]


# Function to generate random topic
def generate_random_topic():
    st.session_state.topic = random.choice(TOPICS)

if not st.session_state.topic:
    generate_random_topic()

# Function to analyze grammar
def analyze_grammar(text):
    prompt = f"""
    Analyze the following text for grammar, sentence formation, and provide a score out of 10.
    Format your response exactly like this:

    Grammar Analysis :
    [Your analysis of grammar errors and correctness]

    Sentence Formation :
    [Your analysis of sentence structure and formation]

    Score : [X]/10

    Suggestions :
    1. &emsp; [Suggestion 1]
    2. &emsp; [Suggestion 2]
    3. &emsp; [Suggestion 3]

    Text to analyze: "{text}"
    """
    response = model.generate_content(prompt)
    return response.text

# Custom CSS for Sidebar & Animation
st.markdown("""
    <style>
    .custom-topic-container {
        background-color: #3f5b6a;
        color: white;
        padding: 20px;
        border-radius: 40px;
        text-align: center;
        margin-bottom: 20px;
    }
    .custom-topic-container h3{
        text-align: center;
    }
    .custom-topic-container h4{
        text-align: center;
        padding-left:40px;
    }
    .Heading{
        text-align: center;
        margin-top: -50px;
    }
    .sidebar  .stButton > button {
        margin-bottom: 5px;
    }
    .listening-bar {
        width: 80%;
        height: 10px;
        background: linear-gradient(90deg,  #2196F3,#2196F3);
        border-radius: 10px;
        animation: move 1.5s infinite;
    }
    @keyframes move {
        0% { transform: translateX(-100%); opacity: 0.8; }
        100% { transform: translateX(100%); opacity: 0.2; }
    }
    .response-card {
        
        border-radius: 10px;
        margin-bottom: 10px;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
    }
    .response-card h4 {
        color: #2196F3;
        margin-bottom: 5px;

    }
    .metric-heading {
        min-width:20%;
        max-width:28%;
        font-weight: bold;
        color: #f4f4f4;
        margin-top: 5px;
        background: #343c42 ;
        border-left: 5px solid #3f5b6a;
        border-right: 5px solid #3f5b6a;
        padding: 10px;
        border-radius: 10px;
        margin-bottom: 5px;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
    }
    
    .metric-content {
        
        color: #f4f4f4;
        padding-left: 20px;

    }
    </style>
    """, unsafe_allow_html=True)

st.markdown(f"<div class='Heading'><h1>🎙️ AI Speech Analysis</h1></div>", unsafe_allow_html=True)
st.markdown(f"<div class='custom-topic-container'><h3>🗣️Give Speech on Topic:</h3><h4>{st.session_state.topic} .</h4></div>", unsafe_allow_html=True)


if st.button("New Topic"):
    st.session_state.messages = []
    generate_random_topic()
    st.rerun()

with st.sidebar:
    st.header("Input Controls")
    text_input = st.text_area("Type your message here...", height=100, key="text_input")
    submit_button = st.button("Send Message", key="submit")
    st.subheader("Voice Input")
    record_button = st.button("🎤 Start Recording", key="record_button")
    if st.button("Clear Chat History", key="clear"):
        st.session_state.messages = []
        st.rerun()

# Display messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        if message["role"] == "assistant":
            content = message["content"].split("\n")
            st.markdown(f"<div class='response-card'><h4>AI Response:</h4>", unsafe_allow_html=True)
            for line in content:
                if line.startswith("Grammar Analysis :") or line.startswith("Sentence Formation :") or line.startswith("Score :") or line.startswith("Suggestions :"):
                    st.markdown(f"<div class='metric-heading'>{line}</div>", unsafe_allow_html=True)
                else:
                    st.markdown(f"<div class='metric-content'>{line}</div>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)
        else:
            st.markdown(message["content"])

# Audio Input Function
def get_audio_input():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.sidebar.markdown("<div class='listening-bar'></div>", unsafe_allow_html=True)
        st.sidebar.write("Listening... Speak now!")
        audio = r.listen(source)
        try:
            return r.recognize_google(audio)
        except sr.UnknownValueError:
            st.sidebar.error("Could not understand audio")
            return None
        except sr.RequestError:
            st.sidebar.error("Could not request results")
            return None

if record_button:
    user_input = get_audio_input()
    if user_input:
        st.sidebar.success("Speech Recorded Successfully ✅")
        st.session_state.messages.append({"role": "user", "content": user_input})
        grammar_analysis = analyze_grammar(user_input)
        st.session_state.messages.append({"role": "assistant", "content": grammar_analysis})
        st.rerun()

if submit_button and text_input.strip():
    with st.spinner("Analyzing... Please wait"):
        st.session_state.messages.append({"role": "user", "content": text_input})
        grammar_analysis = analyze_grammar(text_input)
        st.session_state.messages.append({"role": "assistant", "content": grammar_analysis})
        st.rerun()

import atexit

# Cleanup Function
def cleanup():
    if hasattr(st.session_state, 'audio_dir') and os.path.exists(st.session_state.audio_dir):
        shutil.rmtree(st.session_state.audio_dir)

atexit.register(cleanup)
