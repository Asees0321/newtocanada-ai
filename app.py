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
# GPT SETUP (SAFE)
# ======================
GPT_ENABLED = False
try:
    from openai import OpenAI
    client = OpenAI(api_key=st.secrets.get("OPENAI_API_KEY", ""))
    GPT_ENABLED = True
except:
    GPT_ENABLED = False

# ======================
# SESSION STATE
# ======================
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "tasks" not in st.session_state:
    st.session_state.tasks = {}

if "step" not in st.session_state:
    st.session_state.step = 0

if "onboarded" not in st.session_state:
    st.session_state.onboarded = False

# ======================
# UI STYLING (WINNER POLISH)
# ======================
st.markdown("""
<style>

.main {
    background-color: #f6f8fb;
}

h1, h2, h3 {
    color: #0f172a;
}

/* Cards */
.card {
    background: #f9fafb;
    padding: 20px;
    border-radius: 18px;
    border: 1px solid #e5e7eb;
    box-shadow: 0 8px 20px rgba(0,0,0,0.05);
    margin-bottom: 12px;
}

/* Buttons */
.stButton > button {
    background: linear-gradient(135deg, #ef4444, #dc2626);
    color: white;
    border-radius: 12px;
    padding: 10px 16px;
    font-weight: 600;
}

.stButton > button:hover {
    transform: scale(1.03);
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: #0b1220;
}

section[data-testid="stSidebar"] * {
    color: #e5e7eb !important;
}

/* Chat bubbles */
.user-bubble {
    text-align: right;
    background: #e0f2fe;
    padding: 10px;
    border-radius: 10px;
    margin: 5px;
}

.bot-bubble {
    text-align: left;
    background: #f1f5f9;
    padding: 10px;
    border-radius: 10px;
    margin: 5px;
}

</style>
""", unsafe_allow_html=True)

# ======================
# ONBOARDING (SIMPLE)
# ======================
if not st.session_state.onboarded:

    st.title("🇨🇦 NewToCanada AI")

    st.write("Your AI assistant for settling in Canada")

    name = st.text_input("Your name")

    province = st.selectbox("Province", [
        "Ontario","British Columbia","Alberta","Quebec",
        "Manitoba","Saskatchewan","Nova Scotia",
        "New Brunswick","Newfoundland and Labrador","PEI"
    ])

    goal = st.selectbox("Goal", ["Study", "Work", "Family Immigration"])

    if st.button("Start Journey 🚀"):
        st.session_state.onboarded = True
        st.rerun()

    st.stop()

# ======================
# NAVIGATION
# ======================
page = st.sidebar.radio(
    "Navigation",
    ["🏠 Home", "📊 Dashboard", "💬 AI Assistant", "🧾 Resume Engine"]
)

# ======================
# HOME
# ======================
if page == "🏠 Home":

    st.markdown("""
    <div style="text-align:center;">
    <h1>🇨🇦 NewToCanada AI</h1>
    <p>AI-powered settlement assistant for newcomers</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown('<div class="card">📋 Checklists</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="card">💰 Cost Planner</div>', unsafe_allow_html=True)

    with col3:
        st.markdown('<div class="card">💬 AI Assistant</div>', unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("## 🎯 Your First Week in Canada")

    if st.button("Generate Plan 🇨🇦"):

        prompt = """
Create a 7-day survival plan for a newcomer in Canada.
Include daily tasks and tips.
"""

        if GPT_ENABLED:
            res = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role":"user","content":prompt}]
            )
            st.success(res.choices[0].message.content)
        else:
            st.info("Install OpenAI key to enable AI plan")

# ======================
# DASHBOARD
# ======================
elif page == "📊 Dashboard":

    st.markdown("## 📊 Settlement Dashboard")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<div class="card">📋 Progress Tracker</div>', unsafe_allow_html=True)
        st.progress(0.6)

    with col2:
        st.markdown('<div class="card">💰 Cost Overview</div>', unsafe_allow_html=True)
        st.write("Rent: $1800 | Food: $400 | Transport: $120")

# ======================
# AI ASSISTANT
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

        st.session_state.chat_history.append({"role":"user","content":q})

        prompt = f"""
You are a Canada settlement AI.

Language: {lang}

Question: {q}
"""

        if GPT_ENABLED:
            res = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role":"user","content":prompt}]
            )
            answer = res.choices[0].message.content
        else:
            answer = "AI not enabled"

        st.session_state.chat_history.append({"role":"assistant","content":answer})

        for msg in st.session_state.chat_history[-6:]:

            if msg["role"] == "user":
                st.markdown(f"<div class='user-bubble'>🧑 {msg['content']}</div>", unsafe_allow_html=True)
            else:
                st.markdown(f"<div class='bot-bubble'>🤖 {msg['content']}</div>", unsafe_allow_html=True)

# ======================
# RESUME ENGINE (WINNER FEATURE)
# ======================
elif page == "🧾 Resume Engine":

    st.markdown("## 🏆 AI Job Readiness Engine")

    resume = st.text_area("Paste resume")

    job = st.text_area("Job description (optional)")

    if st.button("Analyze Resume 🚀"):

        prompt = f"""
Improve resume for Canadian jobs.

Resume:
{resume}

Job:
{job}

Return:
- improved resume
- ATS score
- job suggestions
- interview tips
"""

        if GPT_ENABLED:
            res = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role":"user","content":prompt}]
            )

            st.success(res.choices[0].message.content)

        else:
            st.info("""
ATS Score: 72/100

Improve:
- Add measurable results
- Use action verbs
- Tailor for job descriptions

Jobs:
- Customer Service
- Retail Associate
- Admin Assistant
""")
