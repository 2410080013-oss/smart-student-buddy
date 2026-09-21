import streamlit as st
from src.ai_service import ask_gemini


# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="Smart Student Buddy",
    page_icon="🎓",
    layout="wide"
)


# ==========================================
# MAIN TITLE
# ==========================================

st.title("🎓 Smart Student Buddy")
st.write("Your AI-powered college assistant")


# ==========================================
# SIDEBAR MENU
# ==========================================

st.sidebar.title("📚 Menu")

option = st.sidebar.radio(
    "Choose a feature:",
    [
        "Home",
        "AI Doubt Solver",
        "Study Planner",
        "Notes Assistant",
        "Quiz Generator",
        "College Assistant"
    ]
)


# ==========================================
# HOME
# ==========================================

if option == "Home":

    st.header("Welcome to Smart Student Buddy! 👋")

    st.write(
        """
        Smart Student Buddy is your personal AI assistant
        designed to help college students with learning,
        planning, notes, quizzes, and college activities.
        """
    )

    st.info(
        "Select a feature from the sidebar to get started."
    )

    st.subheader("✨ Available Features")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.write("🤖 **AI Doubt Solver**")
        st.write("Ask questions and get simple explanations.")

    with col2:
        st.write("📅 **Study Planner**")
        st.write("Create a personalized study plan.")

    with col3:
        st.write("📝 **Notes Assistant**")
        st.write("Get help organizing your notes.")


# ==========================================
# AI DOUBT SOLVER
# ==========================================

elif option == "AI Doubt Solver":

    st.header("🤖 AI Doubt Solver")

    st.write(
        "Ask any academic question and Gemini will help you."
    )

    question = st.text_area(
        "Enter your question:",
        placeholder="Example: Explain inheritance in Java simply."
    )

    if st.button("Ask Gemini 🚀"):

        if question.strip():

            with st.spinner("Gemini is thinking..."):

                answer = ask_gemini(question)

            st.subheader("📖 Answer")

            st.markdown(answer)

        else:

            st.warning("Please enter a question first.")


# ==========================================
# STUDY PLANNER
# ==========================================

elif option == "Study Planner":

    st.header("📅 Study Planner")

    st.write(
        "Create a study plan based on your subject and available time."
    )

    subject = st.text_input(
        "Enter subject:"
    )

    hours = st.number_input(
        "How many hours can you study per day?",
        min_value=1,
        max_value=12,
        value=2
    )

    exam_date = st.date_input(
        "Select your exam date:"
    )

    learning_level = st.selectbox(
        "Select your learning level:",
        [
            "Beginner",
            "Intermediate",
            "Advanced"
        ]
    )

    additional_requirements = st.text_area(
        "Additional requirements:",
        placeholder="Example: Include revision and practice questions."
    )

    if st.button("Create Study Plan"):

        if subject.strip():

            prompt = f"""
Create a simple and realistic study plan for a college student.

Subject: {subject}
Available study hours per day: {hours}
Exam date: {exam_date}
Learning level: {learning_level}
Additional requirements: {additional_requirements}

Include:
1. Topics to study
2. Time distribution
3. Short breaks
4. Practice questions
5. Revision time
6. A simple daily schedule

Use clear headings and easy language.
"""

            with st.spinner("Creating your study plan..."):

                answer = ask_gemini(prompt)

            st.subheader("📚 Your Study Plan")

            st.markdown(answer)

        else:

            st.warning("Please enter a subject.")


# ==========================================
# NOTES ASSISTANT
# ==========================================

elif option == "Notes Assistant":

    st.header("📝 Notes Assistant")

    st.write(
        "Convert your topics or notes into simple explanations."
    )

    notes = st.text_area(
        "Enter your notes or topic:",
        placeholder="Paste your notes here..."
    )

    note_type = st.selectbox(
        "What do you want?",
        [
            "Simple Explanation",
            "Short Summary",
            "Important Exam Points",
            "Question and Answers"
        ]
    )

    if st.button("Process Notes"):

        if notes.strip():

            prompt = f"""
You are a helpful college study assistant.

Process the following notes.

Requested format: {note_type}

Notes:
{notes}

Use simple, clear, exam-friendly language.
"""

            with st.spinner("Processing your notes..."):

                answer = ask_gemini(prompt)

            st.subheader("📖 Processed Notes")

            st.markdown(answer)

        else:

            st.warning("Please enter your notes first.")


# ==========================================
# QUIZ GENERATOR
# ==========================================

elif option == "Quiz Generator":

    st.header("🧠 Quiz Generator")

    st.write(
        "Generate practice questions to test your knowledge."
    )

    topic = st.text_input(
        "Enter quiz topic:"
    )

    number_of_questions = st.slider(
        "Number of questions:",
        min_value=1,
        max_value=15,
        value=5
    )

    difficulty = st.selectbox(
        "Difficulty level:",
        [
            "Easy",
            "Medium",
            "Hard"
        ]
    )

    if st.button("Generate Quiz"):

        if topic.strip():

            prompt = f"""
Create a practice quiz for a college student.

Topic: {topic}
Number of questions: {number_of_questions}
Difficulty: {difficulty}

Include:
- Clearly numbered questions
- Multiple-choice options where suitable
- Correct answers
- Short explanations

Use simple and accurate language.
"""

            with st.spinner("Generating your quiz..."):

                answer = ask_gemini(prompt)

            st.subheader("📝 Your Quiz")

            st.markdown(answer)

        else:

            st.warning("Please enter a quiz topic.")


# ==========================================
# COLLEGE ASSISTANT
# ==========================================

elif option == "College Assistant":

    st.header("🏫 College Assistant")

    st.write(
        "Get help with general college-related questions."
    )

    college_question = st.text_area(
        "Ask your college-related question:",
        placeholder="Example: How can I prepare for a college presentation?"
    )

    if st.button("Ask College Assistant"):

        if college_question.strip():

            prompt = f"""
You are a helpful college assistant.

Answer the following question clearly and practically.
Do not invent official college rules or policies.

College-related question:
{college_question}
"""

            with st.spinner("Preparing your answer..."):

                answer = ask_gemini(prompt)

            st.subheader("🏫 Assistant Response")

            st.markdown(answer)

        else:

            st.warning("Please enter a question.")