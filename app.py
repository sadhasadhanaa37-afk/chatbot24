import streamlit as st
import google.generativeai as genai

genai.configure(api_key="AIzaSyD2eIEUDFkNi-GYsXqBAgjPuO_aawhCEhg")

model = genai.GenerativeModel("gemini-2.5-flash")

st.title("Gemini Chatbot")

if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat()
    st.session_state.messages = []

user_input = st.text_input("You:")

if st.button("Send") and user_input:
    st.session_state.messages.append(("You", user_input))
    
    response = st.session_state.chat.send_message(user_input)
    bot_reply = response.text
    
    st.session_state.messages.append(("Bot", bot_reply))

# Display chat history
for role, msg in st.session_state.messages:
    st.write(f"**{role}:** {msg}")