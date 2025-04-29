# progress_tracking.py
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

# App title
st.markdown('''
<div style="text-align: center; margin-top:-30px; 
font-size: 40px; background-color: #343c42; 
font-weight: bold; color: white; padding:10px;
border-top-left-radius: 45px; border-bottom-right-radius: 45px; ">
                📈 Progress Tracking
</div>
''', unsafe_allow_html=True)

st.markdown("""
### 📚 Your Quiz Progress Overview
""")

# Load CSV data
try:
    df = pd.read_csv("quiz_results.csv", header=None)
    df.columns = ["DateTime", "Topic", "Difficulty", "Score"]
    df["DateTime"] = pd.to_datetime(df["DateTime"])  # Parse datetime
    df["Score"] = df["Score"].str.replace('%', '').astype(float)
except FileNotFoundError:
    st.error("Quiz results file not found. Take some quizzes first!")
    st.stop()

# Raw Data Table
with st.expander("Show Raw Quiz Submissions"):
    st.dataframe(df)


# 1. Line Chart: Score Progress Over Week
st.markdown("### 📅 Weekly Score Progress")

# Extract week start date
df["Week"] = df["DateTime"].dt.to_period("W").apply(lambda r: r.start_time)

# Calculate average score per week
avg_score_by_week = df.groupby("Week")["Score"].mean().reset_index()

# Plot weekly average scores
fig1, ax1 = plt.subplots()
ax1.plot(avg_score_by_week["Week"], avg_score_by_week["Score"], marker='o', linestyle='-')
ax1.set_xlabel("Week")
ax1.set_ylabel("Average Score (%)")
ax1.set_title("Average Score per Week")
ax1.grid(True)
plt.xticks(rotation=45)
st.pyplot(fig1)



# 2. Bar Chart: Average Score per Topic
st.markdown("### 📚 Average Score per Topic")
avg_score_topic = df.groupby("Topic")["Score"].mean().sort_values()
fig2, ax2 = plt.subplots()
ax2.barh(avg_score_topic.index, avg_score_topic.values)
ax2.set_xlabel("Average Score (%)")
ax2.set_ylabel("Topic")
ax2.set_title("Average Score per Topic")
ax2.grid(True)
st.pyplot(fig2)

# 3. Pie Chart: Attempts per Difficulty Level
st.markdown("### 🎯 Quiz Attempts by Difficulty")
difficulty_counts = df["Difficulty"].value_counts()
fig3, ax3 = plt.subplots()
ax3.pie(difficulty_counts, labels=difficulty_counts.index, autopct='%1.1f%%', startangle=140)
ax3.set_title("Quiz Attempts Distribution (Easy/Medium/Hard)")
st.pyplot(fig3)

# 4. Extra: Summary Statistics
st.markdown("### 📊 Quick Stats")
col1, col2, col3 = st.columns(3)
col1.metric("Total Quizzes", len(df))
col2.metric("Average Score", f"{df['Score'].mean():.2f}%")
col3.metric("Best Score", f"{df['Score'].max():.2f}%")

st.success("Progress Tracking Loaded Successfully 🚀")
