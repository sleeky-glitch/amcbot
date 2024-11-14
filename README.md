# GPMC Chatbot

A chatbot application built for the Ahmedabad Municipal Corporation to handle queries related to the GPMC (Gujarat Provincial Municipal Corporations) Act. The chatbot uses advanced natural language processing to provide accurate, step-by-step responses to procedural questions.

## Features

- RAG (Retrieval Augmented Generation) based responses
- Interactive Streamlit web interface  
- PDF document processing capability
- Vector storage using Pinecone
- Powered by Mixtral-8x7B-Instruct model

## Prerequisites

- Python 3.8+
- Hugging Face API key
- Pinecone API key

## Installation

1. Clone the repository:
```bash
git clone https://github.com/sleeky-glitch/amcbot.git
cd amcbot
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
Create a `.env` file with:
```
HUGGINGFACE_API_KEY=your_huggingface_api_key
PINECONE_API_KEY=your_pinecone_api_key
```

## Usage

1. Run the Streamlit application:
```bash
streamlit run streamlit.py
```

2. Access the web interface through your browser at `http://localhost:8501`

## Project Structure

- `main.py`: Core chatbot implementation with RAG chain setup
- `streamlit.py`: Web interface implementation
- `requirements.txt`: Project dependencies
- `gpmc.pdf`: Source document for GPMC Act (not included in repository)

## Features

- Document processing with PyMuPDF
- Text embedding using HuggingFace
- Vector storage with Pinecone
- RAG-based response generation
- Clean and user-friendly web interface

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
