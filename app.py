import streamlit as st
st.title("Streamlit Chatbot")
import os
os.environ["GOOGLE_API_KEY"]=st.screat["GOOGLE_API_KEY"]
# streamlit_chatbot.py

import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

# Initialize model
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

# Initialize chat history in Streamlit session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [SystemMessage(content="You are a helpful assistant.")]
if "messages_display" not in st.session_state:
    st.session_state.messages_display = []

# Streamlit UI
st.title("💬 Gemini 2.0 Chatbot with LangChain")
st.write("Talk to your AI assistant. Type 'quit' to end the session.")

# Input box
user_input = st.text_input("You:", key="input")

if user_input:
    if user_input.strip().lower() == "quit":
        st.write("👋 Goodbye!")
        st.stop()

    # Add user message
    st.session_state.chat_history.append(HumanMessage(content=user_input))
    st.session_state.messages_display.append(("You", user_input))

    # Get response from model
    result = llm.invoke(st.session_state.chat_history)
    st.session_state.chat_history.append(AIMessage(content=result.content))
    st.session_state.messages_display.append(("AI", result.content))

# Display chat history
for sender, msg in st.session_state.messages_display:
    with st.chat_message(sender):
        st.markdown(msg)
