import streamlit as st
from generator import generate_answer

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Medical RAG Chatbot",
    page_icon="",
    layout="centered"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
    <style>
        .main {
            background-color: #f5f7fa;
        }

        .stTextInput > div > div > input {
            border-radius: 10px;
            padding: 10px;
        }

        .answer-box {
            background-color: white;
            padding: 20px;
            border-radius: 10px;
            border: 1px solid #ddd;
            margin-top: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.title(" Medical RAG Chatbot")

st.write(
    """
    Ask medical-related questions from your uploaded medical documents.

    ### Example Questions:
    - What are symptoms of diabetes?
    - Side effects of aspirin?
    - What is hypertension?
    """
)

# ---------------- SESSION STATE ----------------
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ---------------- USER INPUT ----------------
query = st.text_input(
    " Enter your medical question"
)

# ---------------- BUTTON ----------------
if st.button("Get Answer"):

    if query.strip() == "":
        st.warning("Please enter a question.")

    else:

        with st.spinner(" Searching medical knowledge..."):

            answer = generate_answer(query)

            # Store chat history
            st.session_state.chat_history.append(
                {
                    "question": query,
                    "answer": answer
                }
            )

# ---------------- DISPLAY CHAT HISTORY ----------------
if st.session_state.chat_history:

    st.subheader(" Chat History")

    for chat in reversed(st.session_state.chat_history):

        st.markdown(
            f"""
            <div class="answer-box">

            <b> Question:</b><br>
            {chat['question']}

            <br><br>

            <b> Answer:</b><br>
            {chat['answer']}

            </div>
            """,
            unsafe_allow_html=True
        )