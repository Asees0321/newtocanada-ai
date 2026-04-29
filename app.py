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
# CUSTOM UI STYLE
# ======================
st.markdown("""
<style>

.main {
    background-color: #f8fafc;
}

/* Titles */
h1 {
    font-size: 42px !important;
    font-weight: 800;
    color: #0f172a;
}

h2 {
    font-weight: 700;
    color: #1e293b;
}

/* Cards */
.card {
    background: white;
    padding: 20px;
    border-radius: 16px;
    box-shadow: 0 10px 25px rgba(0,0,0,0.06);
    border: 1px solid #eef2f7;
    margin-bottom: 15px;
}

/* Buttons */
.stButton > button {
    background: linear-gradient(90deg, #e63946, #d62828);
    color: white;
    border-radius: 10px;
    padding: 10px 18px;
    border: none;
    font-weight: 600;
}

.stButton > button:hover {
    transform: scale(1.02);
    transition: 0.2s;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #0f172a;
}

section[data-testid="stSidebar"] * {
    color: white;
}

</style>
""", unsafe_allow_html=True)

# ======================
# SESSION STATE
# ======================
if "tasks" not in st.session_state:
    st.session_state.tasks = {}

# ======================
# NAVIGATION
# ======================
page = st.sidebar.radio(
    "Navigate",
    ["🏠 Home", "📊 Dashboard", "💬 AI Chat", "🧾 Resume Helper"]
)

# ======================
# HOME PAGE (STARTUP LANDING)
# ======================
if page == "🏠 Home":

    st.markdown("""
    <div style="text-align:center; padding:40px;">
        <h1>🇨🇦 NewToCanada AI</h1>
        <p style="font-size:18px; color:#475569;">
        Your AI-powered settlement assistant for Canada
        </p>
        <p style="color:#64748b;">
        Jobs • Housing • Budgeting • Documents • Daily Life
        </p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="card">
        <h3>📋 Smart Checklists</h3>
        <p>Personalized tasks based on your profile</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
        <h3>💰 Cost Planner</h3>
        <p>Know living costs in Canadian cities</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="card">
        <h3>💬 AI Assistant</h3>
        <p>Ask anything about Canada</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.button("🚀 Get Started")

# ======================
# DASHBOARD
# ======================
elif page == "📊 Dashboard":

    st.markdown("""
    <div class="card">
    <h2>📊 Settlement Dashboard</h2>
    <p>Track your progress to becoming Canada-ready</p>
    </div>
    """, unsafe_allow_html=True)

    province = st.selectbox("Province", ["Ontario", "BC", "Alberta", "Quebec"])
    user_type = st.selectbox("You are a:", ["Student", "Worker", "Family"])

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
        st.session_state.tasks[key] = {t: False for t in base_tasks}

    st.markdown("### 🧾 Checklist")

    done = 0

    for task in base_tasks:
        st.session_state.tasks[key][task] = st.checkbox(
            task,
            value=st.session_state.tasks[key][task]
        )
        if st.session_state.tasks[key][task]:
            done += 1

    total = len(base_tasks)
    score = int((done / total) * 100)

    st.markdown("### 🇨🇦 Canada Readiness Score")
    st.progress(score / 100)

    if score < 40:
        st.error(f"{score}/100 — Just getting started")
    elif score < 70:
        st.warning(f"{score}/100 — Getting there")
    else:
        st.success(f"{score}/100 — Canada ready!")

    st.markdown("---")

    st.markdown("""
    <div class="card">
    <h3>💰 Cost of Living (Monthly)</h3>
    </div>
    """, unsafe_allow_html=True)

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

    st.metric("Rent", f"${rent}")
    st.metric("Food", f"${food}")
    st.metric("Transport", f"${transport}")
    st.metric("Phone", f"${phone}")
    st.success(f"Total: ${total_cost}")

# ======================
# AI CHAT
# ======================
elif page == "💬 AI Chat":

    st.markdown("""
    <div class="card">
    <h2>💬 Canada AI Assistant</h2>
    </div>
    """, unsafe_allow_html=True)

    user_input = st.text_input("Ask anything about Canada")

    if user_input:

        if "sin" in user_input.lower():
            response = "Apply for SIN at Service Canada with your passport and permit."
        elif "bank" in user_input.lower():
            response = "Best banks: RBC, TD, Scotiabank, CIBC (newcomer accounts available)."
        elif "rent" in user_input.lower():
            response = "You need income proof, references, and sometimes credit history."
        elif "job" in user_input.lower():
            response = "Start with Indeed, LinkedIn, and Canadian job boards."
        else:
            response = "I can help with housing, jobs, banking, taxes, and settling in Canada."

        st.info("🤖 " + response)

# ======================
# RESUME HELPER
# ======================
elif page == "🧾 Resume Helper":

    st.markdown("""
    <div class="card">
    <h2>🧾 Resume Helper</h2>
    </div>
    """, unsafe_allow_html=True)

    resume = st.text_area("Paste your resume")

    if st.button("Improve Resume"):

        if resume:
            st.success("Suggestions:")
            st.write("✔ Use action verbs (Led, Built, Managed)")
            st.write("✔ Add numbers (improved efficiency by 30%)")
            st.write("✔ Keep it 1–2 pages for Canada format")
            st.write("✔ Tailor for each job application")
        else:
            st.warning("Please paste resume first")
