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
# GPT SETUP (OPTIONAL)
# ======================
try:
    from openai import OpenAI
    client = OpenAI(api_key=st.secrets.get("OPENAI_API_KEY", ""))
    GPT_ENABLED = True
except:
    GPT_ENABLED = False

# ======================
# PREMIUM UI
# ======================
st.markdown("""
<style>

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

/* Cards */
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
    color: #0f172a;
}

/* Buttons */
.stButton > button {
    background: linear-gradient(135deg, #ef4444, #dc2626);
    color: white;
    border-radius: 12px;
    padding: 10px 18px;
    font-weight: 600;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: #0b1220;
}

section[data-testid="stSidebar"] * {
    color: #e5e7eb !important;
}

/* Progress */
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
# ONBOARDING FLOW
# ======================
if not st.session_state.onboarded:

    st.markdown("## 🇨🇦 Welcome to NewToCanada AI")

    steps = [
        "Tell us about you",
        "Choose province",
        "Set goal",
        "Ready!"
    ]

    st.progress(st.session_state.step / (len(steps)-1))

    st.markdown(f"### {steps[st.session_state.step]}")

    if st.session_state.step == 0:
        st.text_input("Your name")

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
        st.success("You're ready 🎉")

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
    ["🏠 Home", "📊 Dashboard", "🧾 Job Engine"]
)

# ======================
# HOME
# ======================
if page == "🏠 Home":

    st.markdown("""
    <div style="text-align:center; padding:40px;">
        <h1>🇨🇦 NewToCanada AI</h1>
        <p style="font-size:18px;">AI-powered settlement assistant for Canada</p>
        <p>Jobs • Housing • Budgeting • Career Growth</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""<div class="card"><h3>📋 Checklists</h3></div>""", unsafe_allow_html=True)

    with col2:
        st.markdown("""<div class="card"><h3>💰 Cost Planner</h3></div>""", unsafe_allow_html=True)

    with col3:
        st.markdown("""<div class="card"><h3>🧾 Job Engine</h3></div>""", unsafe_allow_html=True)

# ======================
# DASHBOARD
# ======================
elif page == "📊 Dashboard":

    st.markdown("""
    <div class="card">
    <h2>📊 Settlement Dashboard</h2>
    <p>Track your Canada readiness</p>
    </div>
    """, unsafe_allow_html=True)

    province = st.selectbox("Province", [
        "Ontario","BC","Alberta","Quebec",
        "Manitoba","Saskatchewan","Nova Scotia",
        "New Brunswick","Newfoundland and Labrador","PEI"
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

    done = 0

    for task in base_tasks:
        st.session_state.tasks[key][task] = st.checkbox(
            task,
            value=st.session_state.tasks[key].get(task, False)
        )
        if st.session_state.tasks[key][task]:
            done += 1

    score = int((done / len(base_tasks)) * 100)

    st.markdown("### 🇨🇦 Canada Survival Score 2.0")
    st.progress(score / 100)

    if score < 40:
        st.error("Early stage settlement")
    elif score < 70:
        st.warning("Getting stable")
    else:
        st.success("Canada-ready!")

# ======================
# JOB READINESS ENGINE (MAIN FEATURE)
# ======================
elif page == "🧾 Job Engine":

    st.markdown("""
    <div class="card">
    <h2>🏆 AI Job Readiness Engine</h2>
    <p>Resume • ATS Score • Jobs • Cover Letter • Interview Prep</p>
    </div>
    """, unsafe_allow_html=True)

    uploaded_file = st.file_uploader("Upload Resume (PDF/TXT)", type=["pdf","txt"])
    job_desc = st.text_area("Paste Job Description (optional)")

    resume_text = ""

    # extract file
    if uploaded_file:

        if uploaded_file.type == "text/plain":
            resume_text = str(uploaded_file.read(), "utf-8")

        elif uploaded_file.type == "application/pdf":
            import PyPDF2
            reader = PyPDF2.PdfReader(uploaded_file)
            for p in reader.pages:
                resume_text += p.extract_text() or ""

        st.success("Resume loaded!")

    else:
        resume_text = st.text_area("Or paste resume")

    if st.button("🚀 Analyze Resume"):

        if resume_text.strip():

            prompt = f"""
You are a Canadian career AI.

TASK:
1. Rewrite resume professionally
2. Improve bullet points
3. Give ATS score (0-100)
4. Suggest jobs in Canada
5. Write cover letter
6. Interview tips

RESUME:
{resume_text}

JOB:
{job_desc}
"""

            if GPT_ENABLED:
                try:
                    res = client.chat.completions.create(
                        model="gpt-4o-mini",
                        messages=[
                            {"role":"system","content":"You are a Canadian career expert"},
                            {"role":"user","content":prompt}
                        ]
                    )

                    st.markdown("## ✨ AI Career Report")
                    st.write(res.choices[0].message.content)

                except:
                    st.error("GPT error — fallback mode")

            else:
                st.warning("GPT not configured — fallback mode")

                st.markdown("### 💼 Jobs")
                st.write("- Customer Service")
                st.write("- Retail Associate")
                st.write("- Admin Assistant")

                st.markdown("### 🧠 Tips")
                st.write("- Add measurable results")
                st.write("- Use action verbs")
                st.write("- Keep concise")

        else:
            st.warning("Upload or paste resume")
