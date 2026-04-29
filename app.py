import streamlit as st

# ======================
# PAGE CONFIG
# ======================
st.set_page_config(
    page_title="NewToCanada AI",
    page_icon="🇨🇦",
    layout="wide"
)

# ======================
# PREMIUM UI FIX (READABLE + STARTUP STYLE)
# ======================
st.markdown("""
<style>

/* Background */
.main {
    background-color: #f6f8fb;
}

/* Typography */
h1 {
    font-size: 44px !important;
    font-weight: 800;
    color: #0f172a;
}

h2 {
    font-weight: 700;
    color: #111827;
}

/* ======================
   FIXED CARD DESIGN (READABLE)
====================== */
.card {
    background: #f9fafb;
    padding: 22px;
    border-radius: 18px;
    border: 1px solid #e5e7eb;
    box-shadow: 0 10px 25px rgba(0,0,0,0.05);
    margin-bottom: 12px;
    color: #111827;
}

.card h3 {
    color: #0f172a !important;
    font-weight: 700;
}

.card p {
    color: #4b5563 !important;
}

/* Buttons */
.stButton > button {
    background: linear-gradient(135deg, #ef4444, #dc2626);
    color: white;
    border-radius: 12px;
    padding: 10px 18px;
    font-weight: 600;
}

/* ======================
   SIDEBAR FIX (READABLE)
====================== */
section[data-testid="stSidebar"] {
    background: #0b1220;
}

section[data-testid="stSidebar"] * {
    color: #e5e7eb !important;
}

section[data-testid="stSidebar"] label {
    color: #e5e7eb !important;
}

section[data-testid="stSidebar"] label:hover {
    background: rgba(255,255,255,0.08);
    border-radius: 8px;
    padding: 6px;
}

/* Progress bar */
.stProgress > div > div {
    background-color: #ef4444;
}

</style>
""", unsafe_allow_html=True)

# ======================
# SESSION STATE
# ======================
if "tasks" not in st.session_state:
    st.session_state.tasks = {}

if "onboarded" not in st.session_state:
    st.session_state.onboarded = False

if "step" not in st.session_state:
    st.session_state.step = 0

# ======================
# ONBOARDING (DUOLINGO STYLE)
# ======================
if not st.session_state.onboarded:

    st.markdown("## 🇨🇦 Welcome to NewToCanada AI")

    steps = [
        "Tell us about you",
        "Choose your province",
        "Set your goal",
        "You're ready!"
    ]

    st.progress(st.session_state.step / (len(steps)-1))

    st.markdown(f"### {steps[st.session_state.step]}")

    if st.session_state.step == 0:
        st.text_input("What is your name?")

    elif st.session_state.step == 1:
        st.selectbox("Province", [
            "Ontario", "British Columbia", "Alberta", "Quebec",
            "Manitoba", "Saskatchewan", "Nova Scotia",
            "New Brunswick", "Newfoundland and Labrador",
            "Prince Edward Island"
        ])

    elif st.session_state.step == 2:
        st.selectbox("Goal", ["Study", "Work", "Family Immigration"])

    elif st.session_state.step == 3:
        st.success("You're all set! 🎉")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("⬅ Back") and st.session_state.step > 0:
            st.session_state.step -= 1

    with col2:
        if st.button("Next ➡"):
            if st.session_state.step < 3:
                st.session_state.step += 1
            else:
                st.session_state.onboarded = True
                st.rerun()

    st.stop()

# ======================
# NAVIGATION
# ======================
page = st.sidebar.radio(
    "Navigation",
    ["🏠 Home", "📊 Dashboard", "💬 AI Chat", "🧾 Resume Helper"]
)

# ======================
# HOME
# ======================
if page == "🏠 Home":

    st.markdown("""
    <div style="text-align:center; padding:40px;">
        <h1>🇨🇦 NewToCanada AI</h1>
        <p style="font-size:18px; color:#475569;">
        AI-powered settlement assistant for Canada
        </p>
        <p style="color:#64748b;">
        Jobs • Housing • Budgeting • Documents • Life Setup
        </p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""<div class="card"><h3>📋 Checklists</h3><p>Personal tasks</p></div>""", unsafe_allow_html=True)

    with col2:
        st.markdown("""<div class="card"><h3>💰 Cost Planner</h3><p>City expenses</p></div>""", unsafe_allow_html=True)

    with col3:
        st.markdown("""<div class="card"><h3>💬 AI Assistant</h3><p>Ask questions</p></div>""", unsafe_allow_html=True)

# ======================
# DASHBOARD
# ======================
elif page == "📊 Dashboard":

    st.markdown("""
    <div class="card">
    <h2>📊 Settlement Dashboard</h2>
    <p>Track your Canada readiness progress</p>
    </div>
    """, unsafe_allow_html=True)

    province = st.selectbox("Province", [
        "Ontario", "British Columbia", "Alberta", "Quebec",
        "Manitoba", "Saskatchewan", "Nova Scotia",
        "New Brunswick", "Newfoundland and Labrador",
        "Prince Edward Island"
    ])

    user_type = st.selectbox("Type", ["Student", "Worker", "Family"])

    base_tasks = [
        "Apply for SIN",
        "Open bank account",
        "Get phone plan",
        "Find housing",
        "Get transit card",
        "Understand healthcare"
    ]

    key = f"{province}-{user_type}"

    if key not in st.session_state.tasks:
        st.session_state.tasks[key] = {}

    for t in base_tasks:
        if t not in st.session_state.tasks[key]:
            st.session_state.tasks[key][t] = False

    st.markdown("### 🧾 Checklist")

    done = 0

    for task in base_tasks:
        st.session_state.tasks[key][task] = st.checkbox(
            task,
            value=st.session_state.tasks[key].get(task, False)
        )
        if st.session_state.tasks[key][task]:
            done += 1

    total = len(base_tasks)
    score = int((done / total) * 100)

    st.markdown("### 🇨🇦 Canada Survival Score 2.0")
    st.progress(score / 100)

    if score < 40:
        st.error("You may struggle initially")
    elif score < 70:
        st.warning("You are getting stable")
    else:
        st.success("You are Canada-ready!")

    st.markdown("---")

    city = st.selectbox("City", ["Toronto", "Vancouver", "Calgary", "Montreal", "Ottawa"])

    costs = {
        "Toronto": [2000, 400, 150, 70],
        "Vancouver": [2200, 420, 140, 75],
        "Calgary": [1500, 350, 120, 60],
        "Montreal": [1300, 300, 100, 50],
        "Ottawa": [1600, 320, 110, 55]
    }

    rent, food, transport, phone = costs[city]
    total_cost = rent + food + transport + phone

    col1, col2 = st.columns(2)

    with col1:
        st.metric("City", city)
        st.metric("Rent", f"${rent}")
        st.metric("Food", f"${food}")

    with col2:
        st.metric("Transport", f"${transport}")
        st.metric("Phone", f"${phone}")
        st.success(f"Total: ${total_cost}")

# ======================
# AI CHAT (SIMPLE SMART MODE)
# ======================
elif page == "💬 AI Chat":

    st.markdown("""
    <div class="card">
    <h2>💬 Canada AI Assistant</h2>
    </div>
    """, unsafe_allow_html=True)

    q = st.text_input("Ask anything")

    if q:
        if "sin" in q.lower():
            ans = "Apply at Service Canada with passport and permit."
        elif "bank" in q.lower():
            ans = "Top banks: RBC, TD, Scotiabank, CIBC."
        elif "rent" in q.lower():
            ans = "Need income proof + references + credit history."
        else:
            ans = "I can help with jobs, housing, banking, immigration."

        st.info("🤖 " + ans)

# ======================
# RESUME HELPER
# ======================
elif page == "🧾 Resume Helper":

    st.markdown("""
    <div class="card">
    <h2>🧾 Resume Helper</h2>
    </div>
    """, unsafe_allow_html=True)

    resume = st.text_area("Paste resume")

    if st.button("Improve Resume"):
        if resume:
            st.success("Suggestions:")
            st.write("✔ Use action verbs")
            st.write("✔ Add measurable impact")
            st.write("✔ Keep it concise (1–2 pages)")
            st.write("✔ Tailor for each job")
        else:
            st.warning("Paste resume first")
