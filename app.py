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
