# Business Card Scanner

A web application that extracts contact information from business card images using OCR technology. Built with Streamlit and EasyOCR for easy and efficient business card data digitization.

## 🌟 Features

- **Image Upload**: Support for PNG, JPG and JPEG formats
- **Text Extraction**: Powered by EasyOCR for accurate text recognition
- **Information Parsing**: Automatically extracts and categorizes:
  - Name
  - Phone number 
  - Email address
  - Website URL
  - Company name
  - Physical address
- **Export Functionality**: Download extracted data as Excel files
- **User-Friendly Interface**: Clean and intuitive Streamlit UI
- **Real-Time Processing**: Instant results display

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/business-card-scanner.git
cd business-card-scanner
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

### Local Development

Run the app locally:
```bash
streamlit run streamlit_app.py
```

## 📖 Usage Guide

1. Launch the application
2. Click "Choose a business card image" to upload your image
3. Wait for the OCR processing to complete
4. Review the extracted information
5. Click "Export to Excel" to download the data

## 🔧 Configuration

The application uses the following key dependencies:
- streamlit==1.29.0
- easyocr==1.7.1
- pandas==2.1.3
- Pillow==10.1.0
- torch>=2.2.0
- torchvision>=0.17.0
- opencv-python-headless==4.8.0.76

## ☁️ Deployment

### Deploying to Streamlit Cloud

1. Push your code to GitHub
2. Log in to [Streamlit Cloud](https://streamlit.io/cloud)
3. Click "New app" and select your repository
4. Choose the main branch and streamlit_app.py
5. Click "Deploy"

### Environment Variables

No environment variables are required for basic functionality.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

Distributed under the MIT License. See `LICENSE` for more information.

## 🙏 Acknowledgments

- [Streamlit](https://streamlit.io/) for the amazing framework
- [EasyOCR](https://github.com/JaidedAI/EasyOCR) for the OCR functionality
- [OpenCV](https://opencv.org/) for image processing capabilities

## 📧 Contact

Your Name - [@yourtwitter](https://twitter.com/yourtwitter)

Project Link: [https://github.com/yourusername/business-card-scanner](https://github.com/yourusername/business-card-scanner)