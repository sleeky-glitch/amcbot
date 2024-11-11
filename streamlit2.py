from main import Chatbot
import streamlit as st

# Page configuration
st.set_page_config(page_title="GPMC BOT")

# Sidebar configuration
with st.sidebar:
    st.title("Chatbot for the Ahmedabad Municipal Corporation GPMC Act")

# Cache the Chatbot instance
@st.cache_resource
def get_chatbot():
    return Chatbot()

# Lazy-load the bot and create it only if called
def generate_response(input_text):
    bot = get_chatbot()
    return bot.rag_chain.invoke(input_text)

# Initialize session state for messages only once
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Welcome! Ask me questions about the GPMC of AMC."}
    ]

# Display chat messages with markdown support and truncated responses
def display_message(role, content):
    if role == "assistant" and len(content) > 500:  # Example length threshold
        content = content[:500] + "...\n\n*Response truncated. Please ask for more details if needed.*"
    with st.chat_message(role):
        st.markdown(content)

# Display initial messages
for message in st.session_state.messages:
    display_message(message["role"], message["content"])

# Process user input and generate response
if input_text := st.chat_input("Type your question here..."):
    # Append user message to session state
    st.session_state.messages.append({"role": "user", "content": input_text})
    display_message("user", input_text)

    # Generate response
    with st.chat_message("assistant"):
        with st.spinner("Generating response..."):
            response = generate_response(input_text)
            display_message("assistant", str(response))

            # Append assistant's response to session state
            st.session_state.messages.append({"role": "assistant", "content": response})

