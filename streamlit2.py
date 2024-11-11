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

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Process user input and generate response
if input_text := st.chat_input("Type your question here..."):
    # Append user message to session state
    st.session_state.messages.append({"role": "user", "content": input_text})
    with st.chat_message("user"):
        st.write(input_text)

    # Generate response
    with st.chat_message("assistant"):
        with st.spinner("Generating response..."):
            response = generate_response(input_text)

            # Check if the response is a string
            if isinstance(response, str):
                # If it's a long string, format as bullet points for readability
                if len(response) > 100:
                    response_parts = response.split(". ")
                    formatted_response = "\n".join(f"- {part.strip()}" for part in response_parts if part.strip())
                    st.markdown(formatted_response)
                else:
                    st.write(response)

            # If the response is a list (e.g., multiple pieces of information), handle it properly
            elif isinstance(response, list):
                formatted_response = "\n".join(f"- {item.strip()}" for item in response if item.strip())
                st.markdown(formatted_response)

            # If the response is a dictionary or other complex structure, display it nicely
            else:
                st.write(str(response))

        # Append assistant's response to session state
        st.session_state.messages.append({"role": "assistant", "content": response})