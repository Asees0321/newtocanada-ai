import streamlit as st

# ======================
# PAGE CONFIG
# ======================
st.set_page_config(
    page_title="NewToCanada AI",
    page_icon="🇨🇦",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ======================
# SESSION STATE
# ======================
if "tasks" not in st.session_state:
    st.session_state.tasks = {}

if "chat_history" not in st.session_state:
    st.session_state.chat_history = {}

if "onboarded" not in st.session_state:
    st.session_state.onboarded = False

if "user_name" not in st.session_state:
    st.session_state.user_name = ""

if "user_province" not in st.session_state:
    st.session_state.user_province = "Ontario"

if "user_goal" not in st.session_state:
    st.session_state.user_goal = "Study"

PROVINCES = [
    "Ontario",
    "British Columbia",
    "Alberta",
    "Quebec",
    "Manitoba",
    "Saskatchewan",
    "Nova Scotia",
    "New Brunswick",
    "Newfoundland and Labrador",
    "Prince Edward Island",
]

# ======================
# PREMIUM UI
# ======================
st.markdown("""
<style>

.stApp {
    background-color: #0f172a;
    color: white;
}

/* HIDE STREAMLIT */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* SIDEBAR */
section[data-testid="stSidebar"] {
    background: #111827;
}

section[data-testid="stSidebar"] * {
    color: white !important;
}

/* TITLES */
h1, h2, h3 {
    color: white !important;
}

/* TEXT */
p, label, span {
    color: #d1d5db !important;
}

/* INPUTS */
div[data-baseweb="input"] input,
textarea,
div[data-baseweb="select"] > div {
    background-color: #1e293b !important;
    color: white !important;
    border: 1px solid #334155 !important;
    border-radius: 12px !important;
}

/* BUTTONS */
.stButton > button {
    background: linear-gradient(135deg, #ef4444, #dc2626);
    color: white;
    border-radius: 12px;
    border: none;
    padding: 12px 18px;
    font-weight: 700;
    width: 100%;
}

/* CARDS */
.grid-card {
    background: #1e293b;
    border: 1px solid #334155;
    border-radius: 18px;
    padding: 24px;
    min-height: 200px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.25);
}

.grid-card h3 {
    color: white;
}

.grid-card p {
    color: #cbd5e1;
}

/* ICONS */
.icon {
    width: 54px;
    height: 54px;
    border-radius: 14px;
    background: #dc2626;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 26px;
    margin-bottom: 18px;
}

/* METRICS */
.metric-row {
    display: grid;
    grid-template-columns: repeat(3,1fr);
    gap: 18px;
    margin-top: 20px;
    margin-bottom: 20px;
}

.metric {
    background: #1e293b;
    border: 1px solid #334155;
    border-radius: 18px;
    padding: 22px;
}

.metric strong {
    font-size: 30px;
    color: white;
}

.metric span {
    color: #cbd5e1;
}

/* CHAT */
.user {
    background: #2563eb;
    color: white;
    padding: 12px 16px;
    border-radius: 16px;
    margin: 10px 0;
    margin-left: auto;
    max-width: 75%;
}

.bot {
    background: #1e293b;
    color: white;
    padding: 12px 16px;
    border-radius: 16px;
    margin: 10px 0;
    max-width: 75%;
    border: 1px solid #334155;
}

/* ALERTS */
div[data-testid="stAlert"] {
    border-radius: 12px;
}

/* MOBILE */
@media (max-width: 768px) {

    .metric-row {
        grid-template-columns: 1fr;
    }

    .user, .bot {
        max-width: 100%;
    }
}

</style>
""", unsafe_allow_html=True)

# ======================
# ONBOARDING
# ======================
if not st.session_state.onboarded:

    left, right = st.columns([1.3, 1])

    with left:

        st.markdown("""
        # 🇨🇦 NewToCanada AI

        ### Your AI-powered settlement assistant for Canada

        Jobs • Housing • Banking • Healthcare • Resume • Daily Life
        """)

        c1, c2, c3 = st.columns(3)

        with c1:
            st.markdown("""
            <div class="grid-card">
                <div class="icon">📋</div>
                <h3>Checklist</h3>
                <p>Track essential newcomer tasks.</p>
            </div>
            """, unsafe_allow_html=True)

        with c2:
            st.markdown("""
            <div class="grid-card">
                <div class="icon">💬</div>
                <h3>AI Assistant</h3>
                <p>Ask questions about Canada anytime.</p>
            </div>
            """, unsafe_allow_html=True)

        with c3:
            st.markdown("""
            <div class="grid-card">
                <div class="icon">💼</div>
                <h3>Resume Helper</h3>
                <p>Improve resumes for Canadian jobs.</p>
            </div>
            """, unsafe_allow_html=True)

    with right:

        st.markdown("## Create Profile")

        name = st.text_input("Your Name")

        province = st.selectbox(
            "Province",
            PROVINCES
        )

        goal = st.selectbox(
            "Goal",
            ["Study", "Work", "Family"]
        )

        if st.button("Start Your Journey 🚀"):

            st.session_state.user_name = name
            st.session_state.user_province = province
            st.session_state.user_goal = goal
            st.session_state.onboarded = True

            st.rerun()

    st.stop()

# ======================
# SIDEBAR NAVIGATION
# ======================
page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Home",
        "📊 Dashboard",
        "💬 AI Assistant",
        "🧾 Resume Helper"
    ]
)

# ======================
# HOME
# ======================
if page == "🏠 Home":

    st.markdown(f"""
    # Welcome, {st.session_state.user_name} 👋

    Your personalized newcomer dashboard for Canada.
    """)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="grid-card">
            <div class="icon">📋</div>
            <h3>Settlement Checklist</h3>
            <p>Track important newcomer steps.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="grid-card">
            <div class="icon">💰</div>
            <h3>Cost Planner</h3>
            <p>Estimate your monthly expenses.</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="grid-card">
            <div class="icon">💬</div>
            <h3>AI Assistant</h3>
            <p>Get instant newcomer guidance.</p>
        </div>
        """, unsafe_allow_html=True)

# ======================
# DASHBOARD
# ======================
elif page == "📊 Dashboard":

    st.markdown("# 📊 Settlement Dashboard")

    province = st.selectbox(
        "Province",
        PROVINCES,
        index=PROVINCES.index(st.session_state.user_province)
    )

    user_type = st.selectbox(
        "Type",
        ["Student", "Worker", "Family"]
    )

    key = f"{province}-{user_type}"

    tasks = [
        "Apply for SIN",
        "Open bank account",
        "Get phone plan",
        "Find housing",
        "Get transit card",
        "Understand healthcare",
    ]

    if key not in st.session_state.tasks:
        st.session_state.tasks[key] = {
            task: False for task in tasks
        }

    done = 0

    st.markdown("## Checklist")

    for task in tasks:

        checked = st.checkbox(
            task,
            value=st.session_state.tasks[key][task]
        )

        st.session_state.tasks[key][task] = checked

        if checked:
            done += 1

    score = int((done / len(tasks)) * 100)

    st.markdown(f"""
    <div class="metric-row">

        <div class="metric">
            <strong>{score}%</strong>
            <span>Canada Survival Score</span>
        </div>

        <div class="metric">
            <strong>{done}/{len(tasks)}</strong>
            <span>Tasks Completed</span>
        </div>

        <div class="metric">
            <strong>{province}</strong>
            <span>Selected Province</span>
        </div>

    </div>
    """, unsafe_allow_html=True)

    st.progress(score / 100)

    if score < 40:
        st.error("You are still in the early settlement stage.")

    elif score < 70:
        st.warning("You are getting settled.")

    else:
        st.success("You are Canada-ready!")

# ======================
# AI ASSISTANT
# ======================
elif page == "💬 AI Assistant":

    st.markdown("# 💬 Canada AI Assistant")

    lang = st.selectbox(
        "Language",
        ["English", "Punjabi", "Hindi", "French"]
    )

    st.caption(
        "Try: How do I get SIN? • How do I rent a house? • What is credit score?"
    )

    left, right = st.columns([5,1])

    with left:
        q = st.text_input(
            "Ask anything",
            placeholder="Type your question here..."
        )

    with right:
        search = st.button("🔍 Search")

    if search and q:

        if page not in st.session_state.chat_history:
            st.session_state.chat_history[page] = []

        st.session_state.chat_history[page].append({
            "role": "user",
            "content": q
        })

        q_lower = q.lower()

        if "sin" in q_lower:
            answer = "You can apply for a SIN number at Service Canada using your passport and permit."

        elif "bank" in q_lower:
            answer = "Popular newcomer-friendly banks include RBC, TD, Scotiabank, and CIBC."

        elif "rent" in q_lower:
            answer = "Most landlords ask for ID, proof of income, references, and sometimes credit history."

        elif "health" in q_lower:
            answer = "Healthcare registration depends on your province. Ontario uses OHIP."

        else:
            answer = "I can help with jobs, housing, banking, immigration, healthcare, and newcomer life in Canada."

        st.session_state.chat_history[page].append({
            "role": "assistant",
            "content": answer
        })

    for msg in st.session_state.chat_history.get(page, [])[-8:]:

        if msg["role"] == "user":

            st.markdown(
                f"<div class='user'>🧑 {msg['content']}</div>",
                unsafe_allow_html=True
            )

        else:

            st.markdown(
                f"<div class='bot'>🤖 {msg['content']}</div>",
                unsafe_allow_html=True
            )

# ======================
# RESUME HELPER
# ======================
elif page == "🧾 Resume Helper":

    st.markdown("# 🧾 Resume Helper")

    resume = st.text_area(
        "Paste your resume",
        height=250,
        placeholder="Paste your resume text here..."
    )

    if st.button("Improve Resume"):

        if resume:

            st.success("AI Resume Suggestions")

            st.write("✔ Add measurable achievements")
            st.write("✔ Use strong action verbs")
            st.write("✔ Tailor resume for each job")
            st.write("✔ Keep resume concise (1-2 pages)")
            st.write("✔ Add technical and soft skills clearly")

        else:
            st.warning("Please paste your resume first.")
