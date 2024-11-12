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

# Function to clean and format the response
def generate_response(input_text):
    bot = get_chatbot()
    response = bot.rag_chain.invoke(input_text)

    # Clean special characters and format the response
    if isinstance(response, str):
        response = response.replace("\uf8e7", "")  # Remove special symbols
        response = response.replace("\\n", "\n")   # Replace newline codes with actual newlines
        response = response.replace("Guj", "Gujarat")  # Expand abbreviations if needed

        # Split long responses into bullet points for readability
        if len(response) > 100:
            response_parts = response.split(". ")
            formatted_response = "\n".join(f"- {part.strip()}" for part in response_parts if part.strip())
            return formatted_response
    return response

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

            # Display the formatted response
            if isinstance(response, str) and len(response) > 100:
                st.markdown(response)
            else:
                st.write(response)

        # Append assistant's response to session state
        st.session_state.messages.append({"role": "assistant", "content": response})




