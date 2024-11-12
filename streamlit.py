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

        # Split response by numbered sections for better readability
        response_parts = response.split("\n")
        formatted_response = []
        current_part = ""
        
        for part in response_parts:
            # Check if the line starts with a number followed by space (indicating a new section)
            if part.strip().isdigit() and len(part.strip()) == 1:
                if current_part:  # Append the previous part before starting a new one
                    formatted_response.append(current_part.strip())
                current_part = f"{part.strip()} "  # Start a new numbered section
            else:
                current_part += part.strip() + " "  # Continue the current section
        
        # Append the last accumulated section if there's any leftover
        if current_part:
            formatted_response.append(current_part.strip())
        
        # Join each section with a newline and bullet point format
        return "\n\n".join(f"- {part}" for part in formatted_response)
    
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






