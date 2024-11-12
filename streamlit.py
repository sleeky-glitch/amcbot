def generate_response(input_text):
    bot = get_chatbot()
    response = bot.rag_chain.invoke(input_text)

    # Clean special characters and format the response
    if isinstance(response, str):
        response = response.replace("\uf8e7", "")  # Remove special symbols
        response = response.replace("\\n", "\n")   # Replace newline codes with actual newlines
        response = response.replace("Guj", "Gujarat")  # Expand abbreviations if needed

        # Split response by numbered sections for better readability
        # Assuming sections start with "1", "2", etc., followed by a newline
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





