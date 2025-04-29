import streamlit as st
import google.generativeai as genai
import re

# Configure Gemini API
genai.configure(api_key="AIzaSyCH5foXWnw35EWPs9PHOStSRwt6rb-bD5I")
model = genai.GenerativeModel('gemini-1.5-flash')

# Define grammar topics from your list
GRAMMAR_TOPICS = {
    "Basic Concepts": [
        "Word definition criteria",
        "Sentence: Definition & Types",
        "Parts of Speech Overview"
    ],
    "Parts of Speech": [
        "Noun: Definition & types",
        "Pronoun: Definition & Types",
        "Adjective: Definition & Types",
        "Verb: Definition & Types",
        "Adverb: Definition & Types",
        "Preposition: definition & Types",
        "Conjunction: Definition & Types",
        "Interjection: Definition & Types",
        "Article: Definition & Types"
    ],
    "Tenses": [
        "Present Tense: Definition & Structure",
        "Past Tense: Definition & Structure",
        "Future Tense: Definition & Structure",
        "Present Simple (Indefinite) Tense",
        "Present Progressive (Continuous) Tense",
        "Present Perfect Tense",
        "Present Perfect Progressive Tense",
        "Past Simple Tense",
        "Past Progressive Tense",
        "Past Perfect Tense",
        "Future Simple Tense",
        "Future Progressive Tense",
        "Future Perfect Tense"
    ],
    "Advanced Grammar": [
        "Clauses: Definition and Types",
        "Conditionals: Definition and Types",
        "Modal Auxiliaries",
        "Subject Verb Agreement: Rules",
        "Transformation of sentences",
        "Punctuation: Definition, Types & Usage Rules"
    ]
}

DIFFICULTY_DESCRIPTIONS = {
    "Easy": "Basic concepts and simple examples suitable for beginners",
    "Medium": "More detailed explanations with varied examples for intermediate learners",
    "Hard": "Advanced concepts, complex examples, and detailed technical explanations"
}


def get_grammar_content(topic, difficulty):
    """Get grammar explanation from Gemini API based on difficulty level"""
    difficulty_prompts = {
        "Easy": f"""
            Explain {topic} in simple terms for beginners.
            Use basic vocabulary and simple examples.
            
            Include:
            1. Simple Definition (3-4 sentences)
            2. Basic Examples (3-4 easy examples)
            3. Simple Practice Tips (3 tips)
            4. Remember Points (3 key points)
            
            Keep it concise and beginner-friendly.
        """,
        "Medium": f"""
            Provide a comprehensive explanation of {topic} for intermediate learners.
            
            Include:
            1. Detailed Definition
            2. Key Concepts (3-4 points)
            3. Multiple Examples (4-5 varied examples)
            4. Common Usage Patterns
            5. Practice Tips (3-4 tips)
            6. Common Mistakes to Avoid
            
            Use more detailed examples and explanations.
        """,
        "Hard": f"""
            Provide an advanced, detailed analysis of {topic}.
            
            Include:
            1. Comprehensive Technical Definition
            2. Detailed Theoretical Background
            3. Complex Concepts and Rules
            4. Advanced Examples (including exceptions)
            5. Technical Usage Notes
            6. Common Errors in Advanced Usage
            7. Expert Tips and Tricks
            8. Related Advanced Topics
            
            Include complex cases and exceptions.
        """
    }
    
    response = model.generate_content(difficulty_prompts[difficulty])
    content = response.text
    content = content.replace("**", "<strong>").replace("**", "</strong>")
    return content

# Custom CSS
st.markdown("""
    <style>
    .topic-section {
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
        background-color: #f0f2f6;
    }
    .main-content {
        padding: 20px;
    }
    .sidebar .sidebar-content {
        background-color: #f0f2f6;
    }
    h1 {
        color: #1f77b4;
    }
    h2 {
        color: #1f77b4;
        margin-top: 20px;
    }
    .stButton>button {
        width: 100%;
        margin: 5px 0;
    }
    .difficulty-info {
        padding: 10px;
        border-radius: 5px;
        margin: 10px 0;
        background-color: #e8f4f8;
    }
    .generated-content {
        background-color: #343c42;
        color: white;
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
    }
    </style>
    """, unsafe_allow_html=True)

# App title and introduction
st.markdown('''
<div style="text-align: center; margin-top:-30px; 
font-size: 40px; background-color: #343c42; 
font-weight: bold; color: white; padding:10px;
border-top-left-radius: 45px; border-bottom-right-radius: 45px; ">
                📚 English Grammar Tutorial
</div>

<div style=" font-size: 18px; color: white;  padding:5px;margin-top:15px;">
            Welcome to your interactive English Grammar tutor! This application will help you master English grammar 
            through comprehensive explanations, examples, and practice tips.
</div>
''', unsafe_allow_html=True)

# Sidebar for topic selection
st.sidebar.title("Grammar Topics")

# Category selection
selected_category = st.sidebar.selectbox(
    "Select Category",
    list(GRAMMAR_TOPICS.keys())
)

# Topic selection within category
selected_topic = st.sidebar.selectbox(
    "Select Topic",
    GRAMMAR_TOPICS[selected_category]
)

# Difficulty selection with descriptions
st.sidebar.markdown("### Select Difficulty Level")
for level, desc in DIFFICULTY_DESCRIPTIONS.items():
    st.sidebar.markdown(f"**{level}:** {desc}")

selected_difficulty = st.sidebar.selectbox(
    "Choose Difficulty",
    ["Easy", "Medium", "Hard"]
)

# Main content area
if selected_topic:
    st.markdown("---")
    st.header(f"📖 {selected_topic}")
    st.markdown(f"**Difficulty Level:** {selected_difficulty}")
    
    # Show loading message
    with st.spinner("Generating content..."):
        content = get_grammar_content(selected_topic, selected_difficulty)
        content = content.replace("##", "<strong>").replace("**", "<strong>").replace("**", "</strong>")
        st.markdown(f"<div class='generated-content'>{content}</div>", unsafe_allow_html=True)
    
    # Additional features
    st.markdown("---")
    st.subheader("📝 Study Tools")
    
    

    

    # CSS Styling
    st.markdown(
        """
        <style>
        .generated-content h3 {
            color: #007BFF; /* Blue color */
            font-size: 20px;
            font-weight: bold;
            margin-top: 10px;
            margin-bottom: 5px;
        }
        .generated-content .section {
            padding: 10px;
            margin-bottom: 15px;
            border: 1px solid #ccc;
            border-radius: 10px;
            background-color: #343c42;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)
    content = ""

    # Function to format content
    def format_content(text):
        text = re.sub(r"\*\*(.*?)\*\*", r"<strong>\1</strong>", text)  # Bold text
        text = text.replace("Easy:", "<h3>Easy</h3><div class='section'>")
        text = text.replace("Medium:", "</div><h3>Medium</h3><div class='section'>")
        text = text.replace("Hard:", "</div><h3>Hard</h3><div class='section'>")
        return text + "</div>"

    with col1:
        if st.button("Generate Practice Questions"):
            with st.spinner("Creating practice questions..."):
                practice_prompt = f"""
                Generate {selected_difficulty.lower()}-level practice questions about {selected_topic}.
                Start with 
                Easy: Create 2 simple questions
                Medium: Create 2 moderate questions
                Hard: Create 2 complex questions
                Include answers and explanations.
                """
                practice_content = model.generate_content(practice_prompt).text
                content = format_content(practice_content)

    with col2:
        if st.button("Show Common Mistakes"):
            with st.spinner("Analyzing common mistakes..."):
                mistakes_prompt = f"""
                List common mistakes people make when using {selected_topic} at {selected_difficulty.lower()} level.
                As a Table 
                Include:
                1. The mistake
                2. Why it's wrong
                3. The correct usage
                Adjust complexity based on the difficulty level selected.
                """
                mistakes_content = model.generate_content(mistakes_prompt).text
                mistakes_content = mistakes_content.replace("##", "<strong>").replace("**", "<strong>").replace("**", "</strong>")
                content = format_content(mistakes_content)

    if content:
        st.markdown(f"<div class='generated-content'>{content}</div>", unsafe_allow_html=True)


# Tips in sidebar
st.sidebar.markdown("---")
st.sidebar.markdown("### 💡 Study Tips")
st.sidebar.markdown("""
- Start with Easy level if you're new to the topic
- Progress to Medium once comfortable
- Try Hard level for mastery
- Practice regularly with examples
- Review common mistakes
""")
