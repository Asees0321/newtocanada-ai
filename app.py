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
    "PEI",
]


# ======================
# YOUTUBE-STYLE UI
# ======================
st.markdown(
    """
<style>
    :root {
    --surface: #1e1e2e;
    --soft: #181825;
    --line: #313244;
    --text: #cdd6f4;
    --muted: #a6adc8;
    --accent: #f38ba8;
    --accent-dark: #d6668a;
    --blue: #89b4fa;
}

.stApp {
    background: #11111b;
    color: var(--text);
}


    header[data-testid="stHeader"] {
        background: transparent;
        height: 0;
    }

    #MainMenu, footer {
        visibility: hidden;
    }

    section.main > div {
        padding-top: 1.2rem;
        max-width: 1220px;
    }

    h1, h2, h3, p, label, span {
        letter-spacing: 0;
    }

    h1, h2, h3 {
        color: var(--text);
    }

    .topbar {
        position: sticky;
        top: 0;
        z-index: 20;
        display: grid;
        grid-template-columns: auto minmax(220px, 540px) auto;
        align-items: center;
        gap: 16px;
        padding: 10px 4px 18px;
        background: #f8fafc;
        border-bottom: 1px solid rgba(229, 231, 235, 0.72);
        margin-bottom: 20px;
    }

    .brand {
        display: flex;
        align-items: center;
        gap: 10px;
        min-width: 210px;
        font-weight: 800;
        color: #0f172a;
        font-size: 1.08rem;
        white-space: nowrap;
    }

    .brand-badge {
        width: 38px;
        height: 38px;
        display: grid;
        place-items: center;
        border-radius: 50%;
        background: #ef4444;
        color: #ffffff;
        font-size: 1.1rem;
        box-shadow: 0 8px 18px rgba(220, 38, 38, 0.24);
    }

    .search-shell {
        height: 42px;
        border: 1px solid var(--line);
        background: #ffffff;
        border-radius: 999px;
        display: flex;
        align-items: center;
        overflow: hidden;
        box-shadow: 0 1px 2px rgba(15, 23, 42, 0.04);
    }

    .search-shell span {
        color: #94a3b8;
        padding-left: 18px;
        font-size: 0.94rem;
    }
        
    .search-icon {
        margin-left: auto;
        width: 54px;
        align-self: stretch;
        display: grid;
        place-items: center;
        border-left: 1px solid var(--line);
        background: #f8fafc;
        color: #334155;
    }

    .profile-pill {
        justify-self: end;
        display: flex;
        align-items: center;
        gap: 10px;
        min-width: 0;
        padding: 7px 11px 7px 7px;
        border: 1px solid var(--line);
        background: #ffffff;
        border-radius: 999px;
        color: #334155;
        font-weight: 700;
        box-shadow: 0 1px 2px rgba(15, 23, 42, 0.04);
    }

    .avatar {
        width: 30px;
        height: 30px;
        border-radius: 50%;
        background: #0f172a;
        color: #ffffff;
        display: grid;
        place-items: center;
        font-size: 0.85rem;
    }

    section[data-testid="stSidebar"] {
        background: #ffffff;
        border-right: 1px solid var(--line);
        width: 250px !important;
    }

    section[data-testid="stSidebar"] > div {
        padding: 18px 12px;
    }

    section[data-testid="stSidebar"] label {
        color: #64748b !important;
        font-weight: 800;
        text-transform: uppercase;
        font-size: 0.72rem;
    }

    section[data-testid="stSidebar"] [role="radiogroup"] {
        gap: 6px;
    }

    section[data-testid="stSidebar"] [role="radiogroup"] label {
        min-height: 46px;
        padding: 0 12px;
        border-radius: 10px;
        color: #111827 !important;
        text-transform: none;
        font-size: 0.96rem;
        font-weight: 700;
    }

    section[data-testid="stSidebar"] [role="radiogroup"] label:hover {
        background: #f1f5f9;
    }

    section[data-testid="stSidebar"] [role="radiogroup"] label:has(input:checked) {
        background: #fee2e2;
        color: #991b1b !important;
    }

    .section-title {
        display: flex;
        align-items: end;
        justify-content: space-between;
        gap: 16px;
        margin-bottom: 16px;
    }

    .section-title h1,
    .section-title h2 {
        margin: 0;
        line-height: 1.1;
    }

    .section-title p {
        margin: 6px 0 0;
        color: var(--muted);
    }

    .grid-card {
        background: var(--surface);
        border: 1px solid var(--line);
        border-radius: 8px;
        padding: 18px;
        min-height: 148px;
        box-shadow: 0 1px 3px rgba(15, 23, 42, 0.06);
        transition: transform 140ms ease, box-shadow 140ms ease;
    }

    .grid-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 24px rgba(15, 23, 42, 0.08);
    }

    .grid-card .icon {
        width: 42px;
        height: 42px;
        display: grid;
        place-items: center;
        border-radius: 50%;
        background: #f1f5f9;
        margin-bottom: 18px;
        font-size: 1.28rem;
    }

    .grid-card h3 {
        margin: 0 0 6px;
        font-size: 1.02rem;
    }

    .grid-card p {
        margin: 0;
        color: var(--muted);
        font-size: 0.92rem;
    }
    
    .metric-row {
        display: grid;
        grid-template-columns: repeat(3, minmax(0, 1fr));
        gap: 14px;
        margin-bottom: 18px;
    }

    .metric {
        background: #ffffff;
        border: 1px solid var(--line);
        border-radius: 8px;
        padding: 16px;
    }

    .metric strong {
        display: block;
        font-size: 1.5rem;
        color: #0f172a;
        line-height: 1;
    }

    .metric span {
        color: var(--muted);
        font-size: 0.88rem;
    }

    .user, .bot {
        max-width: 74%;
        padding: 12px 14px;
        border-radius: 14px;
        margin: 8px 0;
        color: #111827;
        line-height: 1.45;
    }

    .user {
        margin-left: auto;
        background: #dcfce7;
        border-bottom-right-radius: 4px;
    }

    .bot {
        margin-right: auto;
        background: #ffffff;
        border: 1px solid var(--line);
        border-bottom-left-radius: 4px;
    }

    div[data-testid="stButton"] > button {
        width: 100%;
        border: 0;
        border-radius: 999px;
        padding: 0.68rem 1rem;
        background: #dc2626;
        color: white;
        font-weight: 800;
        box-shadow: 0 8px 18px rgba(220, 38, 38, 0.18);
    }

    div[data-testid="stButton"] > button:hover {
        background: #b91c1c;
        color: white;
        border: 0;
    }

    div[data-baseweb="input"] input,
    div[data-baseweb="select"] > div,
    textarea {
        border-radius: 10px !important;
    }

    @media (max-width: 760px) {
        .topbar {
            grid-template-columns: 1fr;
            gap: 10px;
        }

        .brand,
        .profile-pill {
            justify-self: start;
        }

        .metric-row {
            grid-template-columns: 1fr;
        }

        .user, .bot {
            max-width: 100%;
        }
    }
</style>
""",
    unsafe_allow_html=True,
)


def render_topbar(title_hint="Search settlement help"):
    name = st.session_state.user_name.strip() or "Guest"
    initials = "".join(part[0] for part in name.split()[:2]).upper() or "G"
    st.markdown(
        f"""
        <div class="topbar">
            <div class="brand">
                <div class="brand-badge">▶</div>
                <span>NewToCanada AI</span>
            </div>
            <div class="search-shell">
                <span>{title_hint}</span>
                <div class="search-icon">⌕</div>
            </div>
            <div class="profile-pill">
                <div class="avatar">{initials}</div>
                <span>{name}</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


# ======================
# ONBOARDING
# ======================
if not st.session_state.onboarded:
    render_topbar("Start with your province, goal, and first settlement steps")

    left, right = st.columns([1.05, 0.95], vertical_alignment="center")

    with left:
        st.markdown(
            """
            <div class="section-title">
                <div>
                    <h1>Settle in Canada with a clear plan</h1>
                    <p>Jobs, housing, banking, healthcare, and daily life in one simple dashboard.</p>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        a, b, c = st.columns(3)
        with a:
            st.markdown('<div class="grid-card"><div class="icon">🧾</div><h3>Checklist</h3><p>Track essentials from SIN to healthcare.</p></div>', unsafe_allow_html=True)
        with b:
            st.markdown('<div class="grid-card"><div class="icon">💬</div><h3>Ask AI</h3><p>Get quick answers for common newcomer questions.</p></div>', unsafe_allow_html=True)
        with c:
            st.markdown('<div class="grid-card"><div class="icon">💼</div><h3>Resume</h3><p>Improve your resume for Canadian employers.</p></div>', unsafe_allow_html=True)

    with right:
        st.markdown("### Create your profile")
        name = st.text_input("Your name", placeholder="Asees")
        province = st.selectbox("Province", PROVINCES)
        goal = st.selectbox("Goal", ["Study", "Work", "Family"])

        if st.button("Start"):
            st.session_state.user_name = name
            st.session_state.user_province = province
            st.session_state.user_goal = goal
            st.session_state.onboarded = True
            st.rerun()

    st.stop()


# ======================
# NAVIGATION
# ======================
page = st.sidebar.radio(
    "Navigation",
    ["🏠 Home", "📊 Dashboard", "💬 AI Assistant", "🧾 Resume Helper"],
)

render_topbar()


# ======================
# HOME
# ======================
if page == "🏠 Home":
    st.markdown(
        """
        <div class="section-title">
            <div>
                <h1>Home</h1>
                <p>Choose a tool and keep your Canada settlement progress moving.</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown('<div class="grid-card"><div class="icon">📋</div><h3>Settlement Checklist</h3><p>Step-by-step tasks for your first weeks in Canada.</p></div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="grid-card"><div class="icon">💰</div><h3>Cost Planner</h3><p>Prepare for rent, food, transit, and phone expenses.</p></div>', unsafe_allow_html=True)

    with col3:
        st.markdown('<div class="grid-card"><div class="icon">💬</div><h3>AI Assistant</h3><p>Ask about jobs, housing, banking, and daily life.</p></div>', unsafe_allow_html=True)

    st.markdown("### Recommended next steps")
    n1, n2 = st.columns(2)
    with n1:
        st.info("Open the Dashboard and complete your first three settlement tasks.")
    with n2:
        st.info("Use the Resume Helper before applying to jobs in Canada.")


# ======================
# DASHBOARD
# ======================
elif page == "📊 Dashboard":
    st.markdown(

"""
        <div class="section-title">
            <div>
                <h1>Settlement Dashboard</h1>
                <p>Your checklist, score, and essentials in one place.</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    province = st.selectbox("Province", PROVINCES, index=PROVINCES.index(st.session_state.user_province))
    user_type = st.selectbox("Type", ["Student", "Worker", "Family"])

    key = f"{province}-{user_type}"

    base_tasks = [
        "Apply for SIN",
        "Open bank account",
        "Get phone plan",
        "Find housing",
        "Get transit card",
        "Understand healthcare",
    ]

    if key not in st.session_state.tasks:
        st.session_state.tasks[key] = {task: False for task in base_tasks}

    done = 0
    for task in base_tasks:
        if st.session_state.tasks[key][task]:
            done += 1

    score = int((done / len(base_tasks)) * 100)

    st.markdown(
        f"""
        <div class="metric-row">
            <div class="metric"><strong>{score}%</strong><span>Survival score</span></div>
            <div class="metric"><strong>{done}/{len(base_tasks)}</strong><span>Tasks complete</span></div>
            <div class="metric"><strong>{province}</strong><span>Selected province</span></div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("### Checklist")

    done = 0
    for task in base_tasks:
        val = st.checkbox(task, value=st.session_state.tasks[key][task])
        st.session_state.tasks[key][task] = val
        if val:
            done += 1

    score = int((done / len(base_tasks)) * 100)

    st.markdown("### Canada Survival Score 2.0")
    st.progress(score / 100)

    if score < 40:
        st.error("Struggling phase")
    elif score < 70:
        st.warning("Getting stable")
    else:
        st.success("Canada-ready!")


# ======================
# AI ASSISTANT
# ======================
elif page == "💬 AI Assistant":
    st.markdown(
        """
        <div class="section-title">
            <div>
                <h1>Canada AI Assistant</h1>
                <p>Ask quick questions about settling in Canada.</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    lang = st.selectbox("Language", ["English", "Punjabi", "Hindi", "French"])

    suggestions = [
        "How do I get SIN?",
        "How do I rent a house?",
        "What is credit score?",
        "How do I get a job?",
    ]

    st.caption("Try: " + " • ".join(suggestions))
    q = st.text_input("Ask anything", placeholder="Example: How do I open a bank account?")

    if q:
        if page not in st.session_state.chat_history:
            st.session_state.chat_history[page] = []

        st.session_state.chat_history[page].append({"role": "user", "content": q})

        answer = "I can help with jobs, housing, banking, immigration, healthcare, and daily life in Canada."

        st.session_state.chat_history[page].append({"role": "assistant", "content": answer})

    for msg in st.session_state.chat_history.get(page, [])[-6:]:
        if msg["role"] == "user":
            st.markdown(f"<div class='user'>🧑 {msg['content']}</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div class='bot'>🤖 {msg['content']}</div>", unsafe_allow_html=True)


# ======================
# RESUME HELPER
# ======================
elif page == "🧾 Resume Helper":
    st.markdown(
        """
        <div class="section-title">
            <div>
                <h1>Resume Helper</h1>
                <p>Make your resume clearer for Canadian job applications.</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    resume = st.text_area("Paste resume", height=220, placeholder="Paste your resume text here...")

    if st.button("Improve Resume"):
        if resume:
            st.success("Improvements:")
            st.write("✔ Add measurable results")
            st.write("✔ Use action verbs")
            st.write("✔ Tailor for job description")
            st.write("✔ Keep concise, ideally 1-2 pages")
        else:
            st.warning("Please paste resume first")




