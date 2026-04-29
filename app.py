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
# SESSION STATE SAFE INIT
# ======================
if "tasks" not in st.session_state:
    st.session_state.tasks = {}

if "chat_history" not in st.session_state:
    st.session_state.chat_history = {}

if "onboarded" not in st.session_state:
    st.session_state.onboarded = False

if "step" not in st.session_state:
    st.session_state.step = 0

# ======================
# PREMIUM UI (READABLE FIXED)
# ======================
st.markdown("""
<style>

.main {
    background-color: #f6f8fb;
}

h1, h2, h3 {
    color: #0f172a;
}

/* CARD FIX */
.card {
    background: #ffffff;
    padding: 20px;
    border-radius: 16px;
    border: 1px solid #e5e7eb;
    box-shadow: 0 6px 18px rgba(0,0,0,0.06);
    color: #111827;
    margin-bottom: 12px;
}

.card h3 {
    color: #0f172a;
}

.card p {
    color: #4b5563;
}

/* BUTTONS */
.stButton > button {
    background: linear-gradient(135deg, #ef4444, #dc2626);
    color: white;
    border-radius: 12px;
    padding: 10px 16px;
    font-weight: 600;
}

/* SIDEBAR FIX */
section[data-testid="stSidebar"] {
    background: #0b1220;
}

section[data-testid="stSidebar"] * {
    color: #e5e7eb !important;
}

/* CHAT BUBBLES */
.user {
    text-align: right;
    background: #dbeafe;
    padding: 10px;
    border-radius: 10px;
    margin: 5px;
}

.bot {
    text-align: left;
    background: #f1f5f9;
    padding: 10px;
    border-radius: 10px;
    margin: 5px;
}

</style>
""", unsafe_allow_html=True)

# ======================
# ONBOARDING
# ======================
if not st.session_state.onboarded:

    st.title("🇨🇦 NewToCanada AI")

    st.write("AI assistant for settling in Canada")

    name = st.text_input("Your name")

    province = st.selectbox("Province", [
        "Ontario","British Columbia","Alberta","Quebec",
        "Manitoba","Saskatchewan","Nova Scotia",
        "New Brunswick","Newfoundland and Labrador","PEI"
    ])

    goal = st.selectbox("Goal", ["Study","Work","Family"])

    if st.button("Start 🚀"):
        st.session_state.onboarded = True
        st.rerun()

    st.stop()

# ======================
# NAVIGATION
# ======================
page = st.sidebar.radio(
    "Navigation",
    ["🏠 Home", "📊 Dashboard", "💬 AI Assistant", "🧾 Resume Helper"]
)

# ======================
# HOME
# ======================
if page == "🏠 Home":

    st.markdown("""
    <div style="text-align:center;">
    <h1>🇨🇦 NewToCanada AI</h1>
    <p style="color:#64748b;">Jobs • Housing • Banking • Life in Canada</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown('<div class="card"><h3>📋 Checklist</h3><p>Step-by-step tasks</p></div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="card"><h3>💰 Cost Planner</h3><p>Living expenses</p></div>', unsafe_allow_html=True)

    with col3:
        st.markdown('<div class="card"><h3>💬 AI Assistant</h3><p>Ask anything</p></div>', unsafe_allow_html=True)

# ======================
# DASHBOARD
# ======================
elif page == "📊 Dashboard":

    st.markdown("## 📊 Settlement Dashboard")

    province = st.selectbox("Province", [
        "Ontario","British Columbia","Alberta","Quebec",
        "Manitoba","Saskatchewan","Nova Scotia",
        "New Brunswick","Newfoundland and Labrador","PEI"
    ])

    user_type = st.selectbox("Type", ["Student","Worker","Family"])

    key = f"{province}-{user_type}"

    base_tasks = [
        "Apply for SIN",
        "Open bank account",
        "Get phone plan",
        "Find housing",
        "Get transit card",
        "Understand healthcare"
    ]

    if key not in st.session_state.tasks:
        st.session_state.tasks[key] = {t: False for t in base_tasks}

    st.markdown("### 🧾 Checklist")

    done = 0

    for task in base_tasks:
        val = st.checkbox(task, value=st.session_state.tasks[key][task])
        st.session_state.tasks[key][task] = val
        if val:
            done += 1

    score = int((done / len(base_tasks)) * 100)

    st.markdown("### 🇨🇦 Canada Survival Score 2.0")
    st.progress(score / 100)

    if score < 40:
        st.error("Struggling phase")
    elif score < 70:
        st.warning("Getting stable")
    else:
        st.success("Canada-ready!")

# ======================
# AI ASSISTANT (UNCHANGED EXACT STYLE)
# ======================
elif page == "💬 AI Assistant":

    st.markdown("## 💬 Canada AI Assistant")

    lang = st.selectbox("Language", ["English","Punjabi","Hindi","French"])

    q = st.text_input("Ask anything")

    suggestions = [
        "How do I get SIN?",
        "How do I rent a house?",
        "What is credit score?",
        "How do I get a job?"
    ]

    st.write("💡 Try:")
    st.write(", ".join(suggestions))

    if q:

        if page not in st.session_state.chat_history:
            st.session_state.chat_history[page] = []

        st.session_state.chat_history[page].append({"role":"user","content":q})

        prompt = f"""
You are a Canada settlement AI.

Language: {lang}

Question:
{q}
"""

        # SIMPLE SAFE RESPONSE (NO BREAKING DEPENDENCIES)
        answer = "I can help with jobs, housing, banking, immigration in Canada."

        st.session_state.chat_history[page].append({"role":"assistant","content":answer})

        for msg in st.session_state.chat_history[page][-6:]:

            if msg["role"] == "user":
                st.markdown(f"<div class='user'>🧑 {msg['content']}</div>", unsafe_allow_html=True)
            else:
                st.markdown(f"<div class='bot'>🤖 {msg['content']}</div>", unsafe_allow_html=True)

# ======================
# RESUME HELPER
# ======================
elif page == "🧾 Resume Helper":

    st.markdown("## 🧾 Resume Helper")

    resume = st.text_area("Paste resume")

    if st.button("Improve Resume"):

        if resume:
            st.success("Improvements:")
            st.write("✔ Add measurable results")
            st.write("✔ Use action verbs")
            st.write("✔ Tailor for job description")
            st.write("✔ Keep concise (1-2 pages)")
        else:
            st.warning("Please paste resume first")
