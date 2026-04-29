elif page == "💬 AI Assistant":

    st.markdown("## 💬 Canada AI Assistant")

    lang = st.selectbox("Language", ["English","Punjabi","Hindi","French"])

    suggestions = [
        "How do I get SIN?",
        "How do I rent a house?",
        "What is credit score?",
        "How do I get a job?"
    ]

    st.write("💡 Try:")
    st.write(", ".join(suggestions))

    # INIT CHAT HISTORY
    if page not in st.session_state.chat_history:
        st.session_state.chat_history[page] = []

    # INPUT ROW (TEXT + BUTTON)
    col1, col2 = st.columns([5,1])

    with col1:
        q = st.text_input("Ask anything", key="ai_input")

    with col2:
        search_clicked = st.button("🔍 Search")

    # TRIGGER ONLY ON BUTTON OR ENTER
    trigger = search_clicked and q

    if trigger:

        st.session_state.chat_history[page].append({"role":"user","content":q})

        # SIMPLE INTELLIGENCE LOGIC
        if "sin" in q.lower():
            answer = "Apply for SIN at Service Canada with passport + study/work permit."
        elif "bank" in q.lower():
            answer = "Best banks: RBC, TD, Scotiabank, CIBC. You need ID + address proof."
        elif "rent" in q.lower():
            answer = "You need income proof, references, and sometimes credit history."
        elif "job" in q.lower():
            answer = "Use Indeed, LinkedIn, and walk-in hiring for entry-level jobs."
        else:
            answer = "I can help with jobs, housing, banking, immigration in Canada."

        st.session_state.chat_history[page].append({"role":"assistant","content":answer})

    # DISPLAY CHAT
    for msg in st.session_state.chat_history[page][-6:]:

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
