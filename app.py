import streamlit as st
from datetime import datetime

st.set_page_config(page_title="NewToCanada AI", page_icon="🇨🇦", layout="wide")

# -----------------------------
# SESSION STATE
# -----------------------------
if "tasks" not in st.session_state:
    st.session_state.tasks = {}

# -----------------------------
# HEADER
# -----------------------------
st.title("🇨🇦 NewToCanada AI")
st.subheader("Your AI assistant for settling in Canada faster")

st.markdown("---")

# -----------------------------
# SIDEBAR NAVIGATION
# -----------------------------
page = st.sidebar.radio(
    "Navigate",
    ["🏠 Home", "📊 Dashboard", "💬 AI Chat", "🧾 Resume Helper"]
)

# -----------------------------
# HOME PAGE
# -----------------------------
if page == "🏠 Home":
    st.header("Moving to Canada? Start Smart.")

    st.write("""
    NewToCanada AI helps newcomers, students, and workers:
    
    ✔ Build settlement checklists  
    ✔ Estimate living costs  
    ✔ Ask Canada-related questions  
    ✔ Improve resumes for Canadian jobs  
    """)

    st.button("Get Started")

# -----------------------------
# DASHBOARD
# -----------------------------
elif page == "📊 Dashboard":
    st.header("📊 Your Settlement Dashboard")

    province = st.selectbox("Select Province", ["Ontario", "British Columbia", "Alberta", "Quebec"])
    user_type = st.selectbox("You are a:", ["Student", "Worker", "Family"])
    month = st.date_input("Arrival Date")

    st.markdown("### 🧾 Arrival Checklist")

    base_tasks = [
        "Apply for SIN",
        "Open bank account",
        "Get phone plan",
        "Find housing",
        "Get transit card",
        "Understand healthcare system"
    ]

    key = f"{province}-{user_type}"

    if key not in st.session_state.tasks:
        st.session_state.tasks[key] = {task: False for task in base_tasks}

    for task in base_tasks:
        st.session_state.tasks[key][task] = st.checkbox(
            task,
            value=st.session_state.tasks[key][task]
        )

    done = sum(st.session_state.tasks[key].values())
    total = len(base_tasks)

    st.progress(done / total)
    st.write(f"Progress: {done}/{total} tasks completed")

    st.markdown("---")

    st.header("💰 Cost of Living (Monthly Estimate)")

    city = st.selectbox("Select City", ["Toronto", "Vancouver", "Calgary", "Montreal", "Ottawa"])

    costs = {
        "Toronto": [2000, 400, 150, 70],
        "Vancouver": [2200, 420, 140, 75],
        "Calgary": [1500, 350, 120, 60],
        "Montreal": [1300, 300, 100, 50],
        "Ottawa": [1600, 320, 110, 55]
    }

    rent, groceries, transport, phone = costs[city]
    total_cost = rent + groceries + transport + phone

    st.metric("Rent", f"${rent}")
    st.metric("Groceries", f"${groceries}")
    st.metric("Transport", f"${transport}")
    st.metric("Phone", f"${phone}")
    st.success(f"Total Monthly Estimate: ${total_cost}")

# -----------------------------
# AI CHAT (MOCK OR SIMPLE LOGIC)
# -----------------------------
elif page == "💬 AI Chat":
    st.header("💬 Ask Canada AI Assistant")

    user_input = st.text_input("Ask a question about Canada")

    if user_input:
        response = "🤖 "

        if "sin" in user_input.lower():
            response += "You can apply for SIN online or at a Service Canada office."
        elif "bank" in user_input.lower():
            response += "Best beginner banks: RBC, TD, Scotiabank, CIBC."
        elif "rent" in user_input.lower():
            response += "You’ll need credit history, income proof, and references."
        elif "tax" in user_input.lower():
            response += "Canada has federal + provincial taxes. You file yearly in April."
        else:
            response += "That’s a great question! Canada has many newcomer resources depending on your situation."

        st.info(response)

# -----------------------------
# RESUME HELPER
# -----------------------------
elif page == "🧾 Resume Helper":
    st.header("🧾 Canadian Resume Helper")

    text = st.text_area("Paste your resume here")

    if st.button("Improve Resume"):
        if text:
            st.success("Improved Resume Suggestions:")
            st.write("✔ Use action verbs like 'Developed', 'Managed', 'Led'")
            st.write("✔ Quantify achievements (e.g., improved efficiency by 30%)")
            st.write("✔ Keep it 1–2 pages for Canada standards")
        else:
            st.warning("Please paste your resume first")
