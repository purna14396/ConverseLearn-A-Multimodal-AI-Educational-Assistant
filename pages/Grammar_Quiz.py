import csv  # === CSV Addition ===
import json
from datetime import datetime  # === CSV Addition ===

import google.generativeai as genai
import streamlit as st
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the Gemini API key securely from .env or Render
API_KEY = os.getenv("GEMINI_API_KEY")

# Configure Gemini API securely
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')


# Initialize session state for quiz
if 'current_quiz' not in st.session_state:
    st.session_state.current_quiz = None
if 'user_answers' not in st.session_state:
    st.session_state.user_answers = {}
if 'quiz_submitted' not in st.session_state:
    st.session_state.quiz_submitted = False
if 'score' not in st.session_state:
    st.session_state.score = 0

# Define grammar topics
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
        "Future Tense: Definition & Structure"
    ],
    "Advanced Grammar": [
        "Clauses: Definition and Types",
        "Conditionals: Definition and Types",
        "Modal Auxiliaries",
        "Subject Verb Agreement: Rules"
    ]
}

DIFFICULTY_DESCRIPTIONS = {
    "Easy": "Basic MCQs with simple concepts",
    "Medium": "More challenging questions with detailed concepts",
    "Hard": "Complex questions testing advanced understanding"
}

def generate_quiz(topic, difficulty, num_questions=5):
    """Generate quiz questions using Gemini API"""
    prompt = f"""
    Create a multiple choice quiz about {topic} with {num_questions} questions at {difficulty} difficulty level.
    
    Return the response in the following JSON format:
    {{
        "questions": [
            {{
                "question": "Question text here",
                "options": {{
                    "A": "First option",
                    "B": "Second option",
                    "C": "Third option",
                    "D": "Fourth option"
                }},
                "correct_answer": "A",
                "explanation": "Explanation of correct answer"
            }}
        ]
    }}
    
    Make sure:
    - Questions increase in complexity
    - Only one correct answer per question
    - Clear and concise explanations
    - For {difficulty} difficulty level
    - All related to {topic}
    """
    
    response = model.generate_content(prompt)
    try:
        import re

        # st.text(response.text)
        clean_json = re.sub(r'```json\s*([\s\S]+?)\s*```', r'\1', response.text).strip()
        # st.text(clean_json)
        return json.loads(clean_json)
    except:
        st.error("Error generating quiz. Please try again.")
        return None

def calculate_score(quiz_data, user_answers):
    """Calculate quiz score"""
    correct = 0
    total = len(quiz_data['questions'])
    results = []
    
    for i, question in enumerate(quiz_data['questions']):
        user_answer = user_answers.get(i)
        is_correct = user_answer == question['correct_answer']
        if is_correct:
            correct += 1
        results.append({
            'question_num': i + 1,
            'is_correct': is_correct,
            'correct_answer': question['correct_answer'],
            'explanation': question['explanation']
        })
    
    return {
        'score': correct,
        'total': total,
        'percentage': (correct / total) * 100,
        'results': results
    }



# Custom CSS
st.markdown("""
    <style>
    .quiz-question {
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
    }
    .correct-answer {
        color: #28a745;
        font-weight: bold;
    }
    .wrong-answer {
        color: #dc3545;
        font-weight: bold;
    }
    .explanation {
        padding: 10px;
        border-radius: 5px;
        margin-top: 10px;
    }
    .score-display {
        font-size: 24px;
        font-weight: bold;
        text-align: center;
        padding: 20px;
        border-radius: 10px;
        margin: 20px 0;
    }
    </style>
    """, unsafe_allow_html=True)

# App title
# Main container div
# Title div

st.markdown('''
<div style="text-align: center; margin-top:-30px; 
font-size: 40px; background-color: #343c42; 
font-weight: bold; color: white; padding:10px;
border-top-left-radius: 45px; border-bottom-right-radius: 45px; ">
                📚 English Grammar Quiz Generator
</div>

<div style=" font-size: 18px; color: white;  padding:5px; margin-bottom:30px;margin-top:5px;">
            Welcome to the English Grammar Quiz! Select a topic and difficulty level to test your knowledge.
            Each quiz will generate unique questions based on your selections.
</div>
''', unsafe_allow_html=True)



# Sidebar for quiz configuration
st.sidebar.title("Quiz Settings")

selected_category = st.sidebar.selectbox("Select Category", list(GRAMMAR_TOPICS.keys()))
selected_topic = st.sidebar.selectbox("Select Topic", GRAMMAR_TOPICS[selected_category])

st.sidebar.markdown("### Select Difficulty Level")
for level, desc in DIFFICULTY_DESCRIPTIONS.items():
    st.sidebar.markdown(f"**{level}:** {desc}")

selected_difficulty = st.sidebar.selectbox(
    "Choose Difficulty",
    ["Easy", "Medium", "Hard"]
)

# Number of questions selection
num_questions = st.sidebar.slider("Number of Questions", min_value=3, max_value=10, value=5)

# Generate new quiz button with spinner
if st.sidebar.button("Generate New Quiz"):
    with st.spinner("Generating quiz..."):
        st.session_state.current_quiz = generate_quiz(selected_topic, selected_difficulty, num_questions)
    st.session_state.user_answers = {}
    st.session_state.quiz_submitted = False
    st.session_state.score = 0

# Display quiz if available
if st.session_state.current_quiz:
    # Apply background color to quiz questions before submission
    st.markdown("""
    <style>
    .quiz-card {
        background-color: #343c42;
        padding: 20px;
        margin-bottom: 15px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }
    .grey-bg {
        background-color: #343c42 !important;
    }
    .correct-answer {
        color: #27ae60;
        font-weight: bold;
    }
    .wrong-answer {
        color: #e74c3c;
        font-weight: bold;
    }
    .explanation {
        margin-top: 10px;
        font-size: 16px;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

    if not st.session_state.quiz_submitted:
        st.markdown(f"### Quiz: {selected_topic} ({selected_difficulty})")

        for i, question in enumerate(st.session_state.current_quiz['questions']):
            st.markdown(f"""
            <div class="quiz-card">
                <h4>Question {i + 1}</h4>
                {question['question']}
            </div>
            """, unsafe_allow_html=True)

            answer = st.radio(
                "Select your answer:",
                list(question['options'].items()),
                format_func=lambda x: f"{x[0]}) {x[1]}",
                key=f"q_{i}"
            )

            if answer:
                st.session_state.user_answers[i] = answer[0]

            st.markdown("---")
        
        # Submit button
        if st.button("Submit Quiz", use_container_width=True):
            if len(st.session_state.user_answers) == len(st.session_state.current_quiz['questions']):
                st.session_state.quiz_submitted = True
                results = calculate_score(st.session_state.current_quiz, st.session_state.user_answers)
                st.session_state.score = results

                # === CSV Addition: Save to CSV on Submit ===
                now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                csv_data = [now, selected_topic, selected_difficulty, f"{results['percentage']:.2f}%"]

                try:
                    with open("quiz_results.csv", mode='a', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerow(csv_data)
                except Exception as e:
                    st.error(f"Error saving to CSV: {e}")
                # === CSV Addition End ===

            else:
                st.warning("Please answer all questions before submitting.")

    # Display results after submission
    if st.session_state.quiz_submitted and st.session_state.score:
        results = st.session_state.score

        st.markdown(f"""
        <style>
        .score-display {{
            background-color: #2c3e50;
            color: #ecf0f1;
            padding: 15px;
            border-radius: 10px;
            text-align: center;
            font-size: 18px;
            margin-bottom: 20px;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.3);
        }}
        </style>
        <div class="score-display">
        🎯 Score: {results['score']}/{results['total']} ({results['percentage']:.1f}%)
        </div>
        """, unsafe_allow_html=True)

        # Display detailed results with grey background cards
        st.markdown("### Detailed Results")
        for result in results['results']:
            question = st.session_state.current_quiz['questions'][result['question_num'] - 1]
            user_answer = st.session_state.user_answers[result['question_num'] - 1]

            answer_class = 'correct-answer' if result['is_correct'] else 'wrong-answer'
            st.markdown(f"""
            <div class="quiz-card grey-bg">
                <h4>Question {result['question_num']}</h4>
                {question['question']}<br>
                Your answer: <span class="{answer_class}">{user_answer}) {question['options'][user_answer]}</span><br>
                Correct answer: <span class="correct-answer">{question['correct_answer']}) {question['options'][question['correct_answer']]}</span>
                <div class="explanation">
                    <strong>Explanation:</strong><br>{question['explanation']}
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        # Option to generate new quiz with spinner
        if st.button("Generate Another Quiz"):
            with st.spinner("Generating quiz..."):
                for key in ['current_quiz', 'user_answers', 'quiz_submitted', 'score']:
                    if key in st.session_state:
                        del st.session_state[key]

                st.session_state.current_quiz = generate_quiz(selected_topic, selected_difficulty, num_questions)
                st.session_state.user_answers = {}
                st.session_state.quiz_submitted = False
                st.session_state.score = 0
                st.rerun()

st.sidebar.markdown("---")
st.sidebar.markdown("### 💡 Quiz Tips")
st.sidebar.markdown("""
- Read each question carefully
- Consider all options before selecting
- Review explanations for wrong answers
- Try different difficulty levels
- Practice regularly
""")
