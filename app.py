import streamlit as st
from src.ai_service import ask_gemini

st.set_page_config(
    page_title="Smart Student Buddy",
    page_icon="🎓",
    layout="wide"
)

# ==========================================
# SHARED APP STATE
# ==========================================

if "goals" not in st.session_state:
    st.session_state.goals = []

if "subjects" not in st.session_state:
    st.session_state.subjects = [
        "Python",
        "Java",
        "Data Structures",
        "AI / ML"
    ]

if "resources" not in st.session_state:
    st.session_state.resources = []

if "focus_sessions" not in st.session_state:
    st.session_state.focus_sessions = 0

if "quizzes_completed" not in st.session_state:
    st.session_state.quizzes_completed = 0

if "flashcard_decks" not in st.session_state:
    st.session_state.flashcard_decks = 0



# ==========================================
# CINEMATIC APP STYLING
# ==========================================

st.markdown(
    """
    <style>

    /* Main background */
    .stApp {
        background:
            radial-gradient(
                circle at 10% 10%,
                rgba(99, 102, 241, 0.12),
                transparent 30%
            ),
            radial-gradient(
                circle at 90% 20%,
                rgba(168, 85, 247, 0.10),
                transparent 30%
            ),
            linear-gradient(
                135deg,
                #070b14 0%,
                #0f172a 45%,
                #111827 100%
            );
    }

    /* Main content */
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 4rem;
        max-width: 1400px;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background:
            linear-gradient(
                180deg,
                #080b14 0%,
                #111827 55%,
                #17142b 100%
            );
        border-right: 1px solid rgba(255,255,255,0.08);
    }

    section[data-testid="stSidebar"] * {
        color: #e5e7eb;
    }

    /* Headings */
    h1, h2, h3 {
        color: #f8fafc !important;
    }

    /* Normal text */
    p, label {
        color: #cbd5e1 !important;
    }

    /* Hero */
    .hero {
        padding: 42px;
        border-radius: 28px;
        margin-bottom: 28px;

        background:
            linear-gradient(
                135deg,
                rgba(30, 41, 59, 0.95),
                rgba(49, 46, 129, 0.80),
                rgba(88, 28, 135, 0.70)
            );

        border: 1px solid rgba(255,255,255,0.12);

        box-shadow:
            0 25px 80px rgba(0,0,0,0.45),
            inset 0 1px 0 rgba(255,255,255,0.08);
    }

    .hero-title {
        font-size: 46px;
        font-weight: 800;
        letter-spacing: -1px;
        margin-bottom: 8px;
        color: white;
    }

    .hero-subtitle {
        font-size: 20px;
        color: #c7d2fe;
        margin-bottom: 12px;
    }

    .hero-tagline {
        font-size: 15px;
        color: #a5b4fc;
        letter-spacing: 2px;
    }

    /* Glass cards */
    .glass-card {
        padding: 25px;
        border-radius: 22px;

        background:
            rgba(15, 23, 42, 0.72);

        border:
            1px solid rgba(255,255,255,0.08);

        box-shadow:
            0 15px 45px rgba(0,0,0,0.25);

        min-height: 150px;

        transition:
            transform 0.25s ease,
            border-color 0.25s ease;
    }

    .glass-card:hover {
        transform: translateY(-5px);
        border-color: rgba(129,140,248,0.45);
    }

    .card-icon {
        font-size: 30px;
        margin-bottom: 8px;
    }

    .card-title {
        font-size: 19px;
        font-weight: 700;
        color: #f8fafc;
        margin-bottom: 6px;
    }

    .card-text {
        font-size: 14px;
        color: #94a3b8;
    }

    /* Section labels */
    .section-label {
        color: #a5b4fc;
        font-size: 13px;
        letter-spacing: 2px;
        text-transform: uppercase;
        margin-bottom: 8px;
    }

    /* Metric cards */
    div[data-testid="stMetric"] {
        background: rgba(15, 23, 42, 0.72);
        border: 1px solid rgba(255,255,255,0.08);
        padding: 18px;
        border-radius: 18px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.20);
    }

    div[data-testid="stMetricLabel"] {
        color: #94a3b8 !important;
    }

    div[data-testid="stMetricValue"] {
        color: #f8fafc !important;
    }

    /* Buttons */
    .stButton > button {
        border-radius: 12px;
        border: 1px solid rgba(129,140,248,0.30);
        background: rgba(79,70,229,0.18);
        color: #eef2ff;
        font-weight: 600;
        transition: all 0.2s ease;
    }

    .stButton > button:hover {
        border-color: rgba(165,180,252,0.70);
        background: rgba(79,70,229,0.35);
        transform: translateY(-2px);
    }

    /* Text inputs */
    .stTextInput input,
    .stTextArea textarea,
    .stNumberInput input {
        background: rgba(15,23,42,0.75) !important;
        color: #f8fafc !important;
        border: 1px solid rgba(255,255,255,0.10) !important;
        border-radius: 12px !important;
    }

    /* Select boxes */
    div[data-baseweb="select"] > div {
        background: rgba(15,23,42,0.75) !important;
        border-radius: 12px !important;
    }

    /* Divider */
    hr {
        border-color: rgba(255,255,255,0.08) !important;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ==========================================
# MAIN TITLE
# ==========================================

st.title("🎓 Smart Student Buddy")
st.write("Your AI-powered college assistant")


# ==========================================
# SIDEBAR MENU
# ==========================================

st.sidebar.title("📚 Smart Student Buddy")

st.sidebar.caption(
    "Your personal AI study command center"
)

option = st.sidebar.radio(
    "Choose a feature:",
    [
    "Home",
    "AI Doubt Solver",
    "Study Planner",
    "Notes Assistant",
    "Quiz Generator",
    "College Assistant",
    "My Goals",
    "Focus Room",
    "Progress Tracker",
    "Subject Hub",
    "Flashcards",
    "Achievements",
    "Exam Countdown",
    "AI Study Coach",
    "My Resources",
    "Settings"
]
)

st.sidebar.divider()

st.sidebar.caption(
    "Learn • Plan • Practice • Improve"
)


# ==========================================
# HOME / DASHBOARD
# ==========================================

if option == "Home":

    st.markdown(
        """
        <div class="hero">
            <div class="hero-title">👋 Welcome back, Student</div>
            <div class="hero-subtitle">Your personal AI-powered study command center.</div>
            <div class="hero-tagline">LEARN • PLAN • PRACTICE • IMPROVE</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown('<div class="section-label">YOUR DASHBOARD</div>', unsafe_allow_html=True)
    st.subheader("📊 Study Overview")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("🎯 Goals", len(st.session_state.goals))

    with col2:
        st.metric("📚 Subjects", len(st.session_state.subjects))

    with col3:
        st.metric("🔥 Focus Sessions", st.session_state.focus_sessions)

    with col4:
        st.metric("🧠 Quizzes", st.session_state.quizzes_completed)

    st.divider()

    st.markdown('<div class="section-label">QUICK ACCESS</div>', unsafe_allow_html=True)
    st.subheader("⚡ Your Study Tools")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            """
            <div class="glass-card">
                <div class="card-icon">🤖</div>
                <div class="card-title">AI Doubt Solver</div>
                <div class="card-text">Ask academic questions and get simple AI-powered explanations.</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            """
            <div class="glass-card">
                <div class="card-icon">📅</div>
                <div class="card-title">Study Planner</div>
                <div class="card-text">Create personalized study plans based on your goals and time.</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            """
            <div class="glass-card">
                <div class="card-icon">🧠</div>
                <div class="card-title">Quiz Generator</div>
                <div class="card-text">Generate practice questions and test your understanding.</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.write("")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            """
            <div class="glass-card">
                <div class="card-icon">📝</div>
                <div class="card-title">Notes Assistant</div>
                <div class="card-text">Turn your notes into summaries, explanations and exam points.</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            """
            <div class="glass-card">
                <div class="card-icon">🏫</div>
                <div class="card-title">College Assistant</div>
                <div class="card-text">Get practical help with college-related questions.</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            """
            <div class="glass-card">
                <div class="card-icon">🚀</div>
                <div class="card-title">Focus & Progress</div>
                <div class="card-text">Track goals, focus sessions, subjects and study progress.</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.divider()

    st.markdown('<div class="section-label">TODAY</div>', unsafe_allow_html=True)
    st.subheader("🎯 Today's Focus")

    if st.session_state.goals:
        latest_goal = st.session_state.goals[-1]
        st.write(f"**Current goal:** {latest_goal['title']}")
        st.progress(latest_goal["progress"] / 100)
        st.caption(f"Progress: {latest_goal['progress']}% • Target: {latest_goal['target_date']}")
    else:
        st.info("🌱 Create your first goal in My Goals to see it here.")

    st.divider()

    st.markdown('<div class="section-label">ABOUT YOUR STUDY COMPANION</div>', unsafe_allow_html=True)
    st.subheader("✨ Smart Student Buddy")

    st.write(
        "Smart Student Buddy brings your study tools into one intelligent workspace "
        "designed to make studying simpler, more organized and more interactive."
    )

    st.success("💡 Tip: Start with one small study task and build momentum.")


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

            st.session_state.quizzes_completed += 1

            st.success(
                f"🧠 Quiz #{st.session_state.quizzes_completed} generated!"
            )

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

            # ==========================================
# MY GOALS
# ==========================================

elif option == "My Goals":

    st.markdown(
        """
        <div class="hero">
            <h1>🎯 My Goals</h1>
            <p>Set your academic goals and track your progress.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    # ------------------------------------------
    # CREATE NEW GOAL
    # ------------------------------------------

    st.subheader("✨ Create a New Goal")

    goal = st.text_input(
        "What do you want to achieve?",
        placeholder="Example: Complete Python DSA"
    )

    target_date = st.date_input(
        "🎯 Target Date"
    )

    progress = st.slider(
        "📊 Current Progress",
        min_value=0,
        max_value=100,
        value=0,
        step=5
    )

    st.write("")

    if st.button("Save Goal 🎯"):

        if goal.strip():

            st.session_state.goals.append(
                {
                    "title": goal.strip(),
                    "target_date": target_date,
                    "progress": progress
                }
            )

            st.success("🎯 Goal saved successfully!")

        else:

            st.warning("Please enter a goal first.")


    # ------------------------------------------
    # SHOW SAVED GOALS
    # ------------------------------------------

    st.divider()

    st.subheader("📋 My Saved Goals")

    if st.session_state.goals:

        for index, saved_goal in enumerate(
            st.session_state.goals,
            start=1
        ):

            st.markdown(
                f"""
                <div class="glass-card">

                    <h3>
                        🎯 {index}. {saved_goal['title']}
                    </h3>

                    <p>
                        📅 Target Date:
                        {saved_goal['target_date']}
                    </p>

                    <p>
                        📊 Progress:
                        {saved_goal['progress']}%
                    </p>

                </div>
                """,
                unsafe_allow_html=True
            )

            st.progress(
                saved_goal["progress"] / 100
            )

            st.write("")

    else:

        st.info(
            "🌱 No goals yet. Create your first goal above!"
        )

  
# FOCUS ROOM
# ==========================================

elif option == "Focus Room":

    st.header("🧘 Focus Room")
    st.write("Enter a focused study session and work without distractions.")

    st.markdown('<div class="section-label">FOCUS SESSION</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        focus_task = st.text_input(
            "🎯 What are you working on?",
            placeholder="Example: Complete Java inheritance"
        )

    with col2:
        focus_subject = st.text_input(
            "📚 Subject",
            placeholder="Example: Java"
        )

    duration = st.select_slider(
        "⏱️ Focus duration",
        options=[15, 25, 30, 45, 60, 90],
        value=25
    )

    st.divider()

    st.markdown(
        f"""
        <div class="hero">
            <div class="hero-title">🧘 Deep Focus</div>
            <div class="hero-subtitle">{duration} minute study session</div>
            <div class="hero-tagline">ONE TASK • ZERO DISTRACTIONS • FULL FOCUS</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("⏱️ Session", f"{duration} min")

    with col2:
        st.metric("🎯 Task", focus_task if focus_task else "Not set")

    with col3:
        st.metric("📚 Subject", focus_subject if focus_subject else "Not set")

    st.metric("🔥 Sessions Completed", st.session_state.focus_sessions)

    st.divider()

    if st.button("Start Focus Session 🚀"):

        if focus_task.strip():

            st.session_state.focus_sessions += 1

            st.success(
                f"🔥 Focus session #{st.session_state.focus_sessions} started!"
            )

            st.progress(0)

            st.info(
                """
                📵 Put your phone away.

                🎯 Work only on your selected task.

                💧 Keep water nearby.

                🧠 If you get distracted, return to the task.

                ✅ When finished, take a short break.
                """
            )

            st.subheader("💡 Focus Reminder")

            st.write(
                "You don't need to finish everything right now. "
                "Just focus on the task in front of you."
            )

        else:

            st.warning("Please enter a task before starting your session.")


# ==========================================
# PROGRESS TRACKER
# ==========================================

elif option == "Progress Tracker":

    st.header("📈 Progress Tracker")

    st.write(
        "Track your study activity and see how you are progressing."
    )

    # ------------------------------------------
    # OVERVIEW
    # ------------------------------------------

    st.markdown(
        '<div class="section-label">YOUR PROGRESS</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "🔥 Study Streak",
            "0 Days"
        )

    with col2:
        st.metric(
            "⏱️ Study Hours",
            "0 hrs"
        )

    with col3:
        st.metric(
            "📝 Quizzes",
            st.session_state.quizzes_completed
        )

    with col4:
        st.metric(
            "🎯 Goals",
            len(st.session_state.goals)
        )

    st.divider()

    # ------------------------------------------
    # OVERALL PROGRESS
    # ------------------------------------------

    st.markdown(
        '<div class="section-label">OVERALL PERFORMANCE</div>',
        unsafe_allow_html=True
    )

    st.subheader("🚀 Overall Study Progress")

    overall_progress = st.slider(
        "Set your overall progress:",
        min_value=0,
        max_value=100,
        value=35,
        step=5
    )

    st.progress(overall_progress / 100)

    st.caption(
        f"You have completed {overall_progress}% of your current study goals."
    )

    st.divider()

    # ------------------------------------------
    # SUBJECT PROGRESS
    # ------------------------------------------

    st.markdown(
        '<div class="section-label">SUBJECT BREAKDOWN</div>',
        unsafe_allow_html=True
    )

    st.subheader("📚 Subject Progress")

    col1, col2 = st.columns(2)

    with col1:

        st.write("🐍 Python")

        python_progress = st.slider(
            "Python progress",
            0,
            100,
            60,
            5,
            key="python_progress"
        )

        st.progress(python_progress / 100)

        st.caption(f"{python_progress}% completed")

    with col2:

        st.write("☕ Java")

        java_progress = st.slider(
            "Java progress",
            0,
            100,
            45,
            5,
            key="java_progress"
        )

        st.progress(java_progress / 100)

        st.caption(f"{java_progress}% completed")

    col1, col2 = st.columns(2)

    with col1:

        st.write("🧠 Data Structures")

        dsa_progress = st.slider(
            "DSA progress",
            0,
            100,
            30,
            5,
            key="dsa_progress"
        )

        st.progress(dsa_progress / 100)

        st.caption(f"{dsa_progress}% completed")

    with col2:

        st.write("🤖 AI / ML")

        ai_progress = st.slider(
            "AI progress",
            0,
            100,
            25,
            5,
            key="ai_progress"
        )

        st.progress(ai_progress / 100)

        st.caption(f"{ai_progress}% completed")

    st.divider()

    # ------------------------------------------
    # MOTIVATION
    # ------------------------------------------

    st.markdown(
        '<div class="section-label">KEEP GOING</div>',
        unsafe_allow_html=True
    )

    st.subheader("💡 Your Progress Matters")

    st.info(
        "Small progress every day becomes a big achievement over time. "
        "Keep learning, keep practicing, and keep building."
    )
    # ==========================================
# SUBJECT HUB
# ==========================================

elif option == "Subject Hub":

    st.header("📚 Subject Hub")
    st.write("Organize your subjects and quickly access your study tools.")

    st.markdown('<div class="section-label">YOUR SUBJECTS</div>', unsafe_allow_html=True)

    subject_details = {
        "Python": ("🐍", "Programming & Problem Solving"),
        "Java": ("☕", "Object-Oriented Programming"),
        "Data Structures": ("🧠", "Algorithms & Problem Solving"),
        "AI / ML": ("🤖", "Artificial Intelligence & Machine Learning")
    }

    for subject_name in st.session_state.subjects:

        icon, description = subject_details.get(
            subject_name,
            ("📚", "Custom study subject")
        )

        st.markdown(
            f"""
            <div class="glass-card">
                <div class="card-icon">{icon}</div>
                <div class="card-title">{subject_name}</div>
                <div class="card-text">{description}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.write("")

    st.divider()

    st.markdown('<div class="section-label">STUDY ACTIONS</div>', unsafe_allow_html=True)
    st.subheader("⚡ Quick Study Actions")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.info("🤖 **AI Doubt Solver**\n\nAsk questions about any subject and get an AI explanation.")

    with col2:
        st.info("📝 **Notes Assistant**\n\nTurn difficult topics into simple exam-friendly notes.")

    with col3:
        st.info("🧠 **Quiz Generator**\n\nPractice your subject with AI-generated questions.")

    st.divider()

    st.markdown('<div class="section-label">ADD A SUBJECT</div>', unsafe_allow_html=True)

    new_subject = st.text_input(
        "Enter a new subject:",
        placeholder="Example: Computer Networks"
    )

    if st.button("➕ Add Subject"):

        if new_subject.strip():

            subject_name = new_subject.strip()

            if subject_name not in st.session_state.subjects:

                st.session_state.subjects.append(subject_name)

                st.success(
                    f"📚 {subject_name} has been added to your study workspace."
                )

            else:

                st.warning("That subject is already in your workspace.")

        else:

            st.warning("Please enter a subject first.")


# ==========================================
# FLASHCARDS
# ==========================================

elif option == "Flashcards":

    st.header("🗂️ Flashcards")
    st.write("Turn any topic into quick revision flashcards using AI.")

    st.markdown('<div class="section-label">CREATE FLASHCARDS</div>', unsafe_allow_html=True)

    topic = st.text_input(
        "📚 Enter your topic:",
        placeholder="Example: Java Inheritance"
    )

    number_of_cards = st.slider(
        "🗂️ Number of flashcards:",
        min_value=3,
        max_value=15,
        value=5
    )

    difficulty = st.selectbox(
        "🎯 Difficulty:",
        ["Easy", "Medium", "Hard"]
    )

    if st.button("Generate Flashcards 🧠"):

        if topic.strip():

            prompt = f"""
You are an AI study assistant.

Create {number_of_cards} useful flashcards for a college student.

Topic: {topic}
Difficulty: {difficulty}

For each flashcard provide:

CARD 1
Question:
Answer:
Explanation:

CARD 2
Question:
Answer:
Explanation:

Continue until all flashcards are generated.

Keep the answers concise and exam-friendly.
Use simple language.
Focus on important concepts, definitions, formulas, examples,
and common exam points where appropriate.
"""

            with st.spinner("Creating your flashcards..."):

                answer = ask_gemini(prompt)

            st.session_state.flashcard_decks += 1

            st.success(
                f"🧠 Flashcard deck #{st.session_state.flashcard_decks} created!"
            )

            st.divider()

            st.markdown(
                '<div class="section-label">YOUR REVISION DECK</div>',
                unsafe_allow_html=True
            )

            st.markdown(answer)

        else:

            st.warning("Please enter a topic first.")


# ==========================================
# ACHIEVEMENTS
# ==========================================

elif option == "Achievements":

    st.header("🏆 Achievements")
    st.write("Build your study journey and unlock milestones along the way.")

    first_session = st.session_state.focus_sessions >= 1
    first_goal = len(st.session_state.goals) >= 1
    first_quiz = st.session_state.quizzes_completed >= 1
    five_subjects = len(st.session_state.subjects) >= 5
    first_flashcards = st.session_state.flashcard_decks >= 1

    achievements = [
        ("🔥", "First Study Session", "Complete your first focused study session.", first_session),
        ("🎯", "First Goal", "Create your first academic goal.", first_goal),
        ("🧠", "Quiz Starter", "Generate your first practice quiz.", first_quiz),
        ("📚", "Knowledge Builder", "Add five different subjects.", five_subjects),
        ("🗂️", "Flashcard Master", "Create your first flashcard deck.", first_flashcards),
        ("🚀", "Consistency", "Maintain a 7-day study streak.", False)
    ]

    unlocked_count = sum(item[3] for item in achievements)

    st.markdown(
        '<div class="section-label">YOUR MILESTONES</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    for index, achievement in enumerate(achievements):

        icon, title, description, unlocked = achievement
        target_column = col1 if index % 2 == 0 else col2

        with target_column:

            if unlocked:

                st.markdown(
                    f"""
                    <div class="glass-card">
                        <div class="card-icon">{icon}</div>
                        <div class="card-title">{title} ✅</div>
                        <div class="card-text">{description}</div>
                        <br>
                        <div class="card-text">🟢 UNLOCKED</div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            else:

                st.markdown(
                    f"""
                    <div class="glass-card">
                        <div class="card-icon">🔒</div>
                        <div class="card-title">{title}</div>
                        <div class="card-text">{description}</div>
                        <br>
                        <div class="card-text">🔒 LOCKED</div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            st.write("")

    st.divider()

    st.markdown(
        '<div class="section-label">YOUR JOURNEY</div>',
        unsafe_allow_html=True
    )

    st.subheader("🌟 Keep Building")

    st.progress(unlocked_count / len(achievements))

    st.caption(
        f"{unlocked_count} of {len(achievements)} achievements currently unlocked."
    )

    st.info(
        "Every small study session contributes to your larger journey. "
        "Keep learning, practicing, and improving."
    )


# ==========================================
# EXAM COUNTDOWN
# ==========================================

elif option == "Exam Countdown":

    st.header("⏳ Exam Countdown")

    st.write(
        "Keep your upcoming exams visible and stay prepared."
    )

    st.markdown(
        '<div class="section-label">SET YOUR EXAM</div>',
        unsafe_allow_html=True
    )

    exam_name = st.text_input(
        "📚 Exam name:",
        placeholder="Example: Data Structures Mid-Sem"
    )

    exam_date = st.date_input(
        "📅 Exam date:"
    )

    if st.button("🚀 Start Countdown"):

        from datetime import date

        today = date.today()

        days_remaining = (exam_date - today).days

        if not exam_name.strip():

            st.warning(
                "Please enter your exam name."
            )

        elif days_remaining > 0:

            st.divider()

            st.markdown(
                f"""
                <div class="hero">

                    <div class="hero-title">
                        ⏳ {days_remaining}
                    </div>

                    <div class="hero-subtitle">
                        Days remaining
                    </div>

                    <div class="hero-tagline">
                        UNTIL {exam_name.upper()}
                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )

            col1, col2, col3 = st.columns(3)

            with col1:

                st.metric(
                    "📅 Exam Date",
                    str(exam_date)
                )

            with col2:

                st.metric(
                    "⏳ Days Left",
                    days_remaining
                )

            with col3:

                if days_remaining <= 7:
                    status = "⚠️ Final Week"
                elif days_remaining <= 30:
                    status = "🔥 Prepare"
                else:
                    status = "🌱 Start Early"

                st.metric(
                    "🎯 Status",
                    status
                )

            st.divider()

            st.subheader("📖 Preparation Reminder")

            if days_remaining <= 7:

                st.warning(
                    "Your exam is close. Focus on revision, "
                    "practice questions, and important topics."
                )

            elif days_remaining <= 30:

                st.info(
                    "You have time to prepare. Build a consistent "
                    "study routine and revise regularly."
                )

            else:

                st.success(
                    "You have plenty of preparation time. "
                    "Start early and build strong foundations."
                )

        elif days_remaining == 0:

            st.error(
                "🚨 Your exam is today! Stay calm and focus on your preparation."
            )

        else:

            st.warning(
                "That exam date has already passed. "
                "Choose a future exam date."
            )
            # ==========================================
# AI STUDY COACH
# ==========================================

elif option == "AI Study Coach":

    st.header("🤖 AI Study Coach")

    st.write(
        "Tell your AI coach what you're studying and get a practical study strategy."
    )

    st.markdown(
        '<div class="section-label">YOUR STUDY SITUATION</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:

        subject = st.text_input(
            "📚 What subject are you studying?",
            placeholder="Example: Data Structures"
        )

    with col2:

        topic = st.text_input(
            "🧠 What topic?",
            placeholder="Example: Trees"
        )

    col1, col2 = st.columns(2)

    with col1:

        available_time = st.slider(
            "⏱️ Available study time (hours)",
            min_value=1,
            max_value=12,
            value=2
        )

    with col2:

        confidence = st.slider(
            "📊 How confident are you?",
            min_value=0,
            max_value=100,
            value=50,
            step=10
        )

    exam_soon = st.selectbox(
        "📅 Is an exam coming soon?",
        [
            "No",
            "Yes — within 7 days",
            "Yes — within 30 days"
        ]
    )

    study_problem = st.text_area(
        "💬 What's your biggest study problem?",
        placeholder=(
            "Example: I understand the theory but "
            "I struggle to solve questions."
        )
    )

    if st.button("🚀 Ask My AI Coach"):

        if subject.strip() and topic.strip():

            prompt = f"""
You are an AI study coach helping a college student.

Create a practical study strategy based on the student's situation.

Subject: {subject}
Topic: {topic}
Available study time: {available_time} hours
Confidence level: {confidence}%
Exam situation: {exam_soon}
Study problem: {study_problem}

Give the student:

1. What to study first
2. A realistic study schedule for today
3. What concepts to focus on
4. What type of practice to do
5. A short revision strategy
6. Common mistakes to avoid
7. One small task to complete immediately
8. A short encouraging message

Keep the advice practical, simple, and exam-friendly.
Do not overwhelm the student with unnecessary information.
"""

            with st.spinner("Your AI coach is creating your strategy..."):

                answer = ask_gemini(prompt)

            st.divider()

            st.markdown(
                '<div class="section-label">YOUR PERSONAL STUDY STRATEGY</div>',
                unsafe_allow_html=True
            )

            st.subheader("🧠 AI Coach Response")

            st.markdown(answer)

        else:

            st.warning(
                "Please enter both a subject and topic."
            )
            # ==========================================
# MY RESOURCES
# ==========================================

elif option == "My Resources":

    st.header("📦 My Resources")

    st.write(
        "Keep your useful study links and learning resources organized."
    )

    st.markdown(
        '<div class="section-label">ADD A RESOURCE</div>',
        unsafe_allow_html=True
    )

    resource_name = st.text_input(
        "📚 Resource name:",
        placeholder="Example: Java DSA Practice"
    )

    resource_link = st.text_input(
        "🔗 Resource link:",
        placeholder="https://example.com"
    )

    resource_type = st.selectbox(
        "🏷️ Resource type:",
        [
            "Course",
            "Documentation",
            "Practice",
            "Video",
            "Website",
            "Reference",
            "Other"
        ]
    )

    resource_description = st.text_area(
        "📝 Description:",
        placeholder="What is this resource useful for?"
    )

    if st.button("➕ Add Resource"):

        if resource_name.strip() and resource_link.strip():

            st.session_state.resources.append(
                {
                    "name": resource_name.strip(),
                    "link": resource_link.strip(),
                    "type": resource_type,
                    "description": resource_description.strip()
                }
            )

            st.success(
                f"📦 {resource_name} added successfully!"
            )

        else:

            st.warning(
                "Please enter both a resource name and link."
            )

    if st.session_state.resources:

        st.divider()

        st.markdown(
            '<div class="section-label">SAVED RESOURCES</div>',
            unsafe_allow_html=True
        )

        for resource in st.session_state.resources:

            st.markdown(
                f"""
                <div class="glass-card">
                    <div class="card-icon">📚</div>
                    <div class="card-title">{resource['name']}</div>
                    <div class="card-text">Type: {resource['type']}</div>
                    <br>
                    <div class="card-text">{resource['description']}</div>
                </div>
                """,
                unsafe_allow_html=True
            )

            st.link_button(
                "🔗 Open Resource",
                resource["link"]
            )

            st.write("")

    st.divider()

    st.markdown(
        '<div class="section-label">RESOURCE IDEAS</div>',
        unsafe_allow_html=True
    )

    st.subheader("💡 What you can save here")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.info(
            """
            📖 **Learning**

            Courses, tutorials,
            documentation and guides.
            """
        )

    with col2:

        st.info(
            """
            💻 **Practice**

            Coding platforms,
            problem sets and quizzes.
            """
        )

    with col3:

        st.info(
            """
            🎥 **Media**

            Useful videos,
            lectures and references.
            """
        )
        # ==========================================
# SETTINGS
# ==========================================

elif option == "Settings":

    st.header("⚙️ Settings")

    st.write(
        "Customize your Smart Student Buddy experience."
    )

    # ------------------------------------------
    # STUDENT PROFILE
    # ------------------------------------------

    st.markdown(
        '<div class="section-label">STUDENT PROFILE</div>',
        unsafe_allow_html=True
    )

    st.subheader("👤 Your Profile")

    student_name = st.text_input(
        "Your name:",
        placeholder="Enter your name"
    )

    study_level = st.selectbox(
        "🎓 Study level:",
        [
            "First Year",
            "Second Year",
            "Third Year",
            "Fourth Year",
            "Other"
        ]
    )

    preferred_style = st.selectbox(
        "🧠 Preferred learning style:",
        [
            "Simple explanations",
            "Detailed explanations",
            "Examples first",
            "Exam-focused"
        ]
    )

    st.divider()

    # ------------------------------------------
    # STUDY PREFERENCES
    # ------------------------------------------

    st.markdown(
        '<div class="section-label">STUDY PREFERENCES</div>',
        unsafe_allow_html=True
    )

    st.subheader("📚 Study Preferences")

    daily_goal = st.slider(
        "⏱️ Daily study goal (hours):",
        min_value=1,
        max_value=12,
        value=2
    )

    reminder_enabled = st.toggle(
        "🔔 Enable study reminders",
        value=True
    )

    st.divider()

    # ------------------------------------------
    # APP PREFERENCES
    # ------------------------------------------

    st.markdown(
        '<div class="section-label">APP PREFERENCES</div>',
        unsafe_allow_html=True
    )

    st.subheader("🎨 App Preferences")

    compact_mode = st.toggle(
        "📱 Compact interface",
        value=False
    )

    animations = st.toggle(
        "✨ Enable visual effects",
        value=True
    )

    st.divider()

    # ------------------------------------------
    # SAVE SETTINGS
    # ------------------------------------------

    if st.button("💾 Save Settings"):

        st.success(
            "✅ Your settings have been saved for this session."
        )

        st.write(
            f"Welcome, {student_name if student_name.strip() else 'Student'}!"
        )

        st.caption(
            f"Daily study goal: {daily_goal} hour(s) • "
            f"Learning style: {preferred_style}"
        )

        if reminder_enabled:

            st.info(
                "🔔 Study reminders are enabled."
            )

        else:

            st.info(
                "🔕 Study reminders are disabled."
            )