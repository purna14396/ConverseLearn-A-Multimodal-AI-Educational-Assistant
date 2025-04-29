
# 📚 ConverseLearn: A Multimodal AI Educational Assistant
**Enhancing Communication Skills with Real-Time Feedback and Adaptive Learning**

---

## 🚀 Live App

👉 [Click here to try it out](https://converselearn-a-multimodal-ai.onrender.com)

---


## 🎥 Demo

👉 [Click here to watch the demo](demo/Final_Demo_Updated.mp4)


## 🛠 Project Description
ConverseLearn is an AI-driven educational platform that enhances communication skills through dynamic, multimodal learning.  
It integrates **text**, **voice**, and **visual modes** to simulate real-world conversation practice, role-play, grammar correction, and personalized quizzes with instant feedback.

Learners can practice:
- 🎙️ **Speaking** (Voice Interaction & Grammar Analysis)
- 🎧 **Listening** (Speech Recognition Feedback)
- ✍️ **Grammar Mastery** (AI Grammar Tutorials + Adaptive Quizzes)
- 📈 **Real-Time Performance Tracking** (Progress Dashboard)

Powered by **Google Gemini AI**, **SpeechRecognition**, **gTTS**, and **Streamlit**.

---

## 🎯 Problem Statement
Traditional language learning methods face several limitations:
- Lack interactive, real-world communication practice.
- Are generic and not adaptive to each learner’s progress or skill level.
- Do not offer instant feedback to correct mistakes, making it harder to self-correct.
- Miss engagement features like gamification and adaptive challenges, reducing learner motivation.
- Rigidly fix the same theory and practical exercises for all learners, irrespective of individual expertise.
- Struggle to prepare learners for dynamic challenges such as **Svar Exams**, where adaptive thinking and real-time performance are crucial.

---

## 💡 Proposed Solution
ConverseLearn addresses these issues by offering:
- **Multimodal Interaction**: Text + Voice + Visuals.
- **Personalized Learning**: User can adjust difficulty based on their proficiency.
- **Real-Time Feedback**: Instant grammar, pronunciation, and fluency analysis.
- **Gamified Practice**: Quizzes, topic generation, conversational practice.
- **Progress Tracking**: Detailed performance dashboards.

---

## 🖼️ System Architecture

<p align="center">
  <img src="https://github.com/user-attachments/assets/cb35bc2d-b34f-44ad-a969-d21e42b03d2b" alt="System Architecture Part 1" width="700">
</p>

<p align="center">
  <img src="https://github.com/user-attachments/assets/44bb7503-9917-480a-9402-9140d98ffabf" alt="System Architecture Part 2" width="700">
</p>


---

## 🔥 Key Features
- 🎙️ **Voice Interaction & Grammar Analysis**  
  Record speeches on random topics, analyze grammar, sentence formation, and receive AI feedback instantly.

- 🧠 **Conversational AI Chatbot**  
  Practice natural conversation with a friendly AI, receive both spoken and written responses.

- 📚 **Interactive English Grammar Tutorial**  
  Learn topics like Tenses, Parts of Speech, Clauses, and more, at Easy, Medium, or Hard levels with Gemini AI explanations.

- 📝 **Grammar Quiz Generator**  
  Adaptive quizzes based on selected topics and difficulty. Instant scoring + detailed explanations.

- 📈 **Progress Tracking Dashboard**  
  Visualize your performance over time with line graphs, bar charts, and pie charts (based on stored quiz results).

---

## 🏗️ Tech Stack

| Category             | Tools/Libraries                                  |
|----------------------|--------------------------------------------------|
| Frontend              | Streamlit, Html, Css                            |
| AI/NLP Models         | Google Gemini AI (gemini-1.5-flash)             |
| Speech Recognition    | SpeechRecognition, Google TTS (gTTS)            |
| Backend & Logic       | Python                                          |
| Data Storage          | CSV File (quiz results)                         |
| Visualization         | Matplotlib, Pandas (for analytics)              |

---

## 📋 File Structure

| File                              | Description                                      |
|-----------------------------------|--------------------------------------------------|
| `Home.py`                         | Main landing page (navigation + overview)       |
| `English_Tutorial.py`             | Grammar tutorial generator                      |
| `Grammar_Quiz.py`                 | Grammar quiz creation and evaluation            |
| `Progress_Tracking.py`            | Progress tracking dashboard                     |
| `Voice_Interaction_&_Grammar_Analysis.py` | Speech recording, analysis, grammar feedback |
| `Voice_Interaction_Chatbot.py`    | Conversational AI chatbot with voice response   |
| `quiz_results.csv`                | CSV file storing past quiz results              |

---


## 📊 Progress Tracking Visualizations
- **Score Over Time** (Line Chart)
- **Average Score per Topic** (Bar Chart)
- **Quiz Attempts by Difficulty Level** (Pie Chart)
- **Quick Stats** (Total Quizzes, Avg Score, Best Score)

---

## ⚙️ Future Enhancements

- Add voice-to-voice direct conversations.
- Integrate gamification elements (badges, levels, rewards) to boost user engagement.
- Expand support for various languages beyond English.
- Introduce difficulty prediction and adaptive learning paths using Machine Learning.
- Extend topic coverage into professional English, business communication, and other specialized domains.
- Enable integration with educational institutions for official learning programs and certifications.

---

## ✍️ Authors
- **Potu Purna Sai** (41731092)
- **S S Nivetha** (41731082)


**Guided by**: Dr. S Nivetha, M.E., Ph.D., Associate Professor, CSE

---

## 🏅 Publications and Conferences

- 📄 **Published Paper:**  
  [ConverseLearn: A Multimodal AI Educational Assistant](https://www.iosrjournals.org/iosr-jce/papers/Vol26-issue6/Ser-3/C2606031020.pdf)  
  Published in **IOSR Journal of Computer Engineering (IOSR-JCE)**, Volume 26, Issue 6, Series 3.

- 🎤 **Conference Presentation:**  
  Presented at **ICASET 2025** (International Conference on Advances in Science, Engineering & Technology) organized by **IFERP**.


