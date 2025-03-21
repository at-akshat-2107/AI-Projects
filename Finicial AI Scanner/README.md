# Financial AI Scanner 💹

A powerful AI-powered application that analyzes financial documents and images to extract insights, trends, and key metrics. Built with Streamlit and powered by Groq's LLM API, this tool helps financial professionals and decision-makers quickly understand complex financial documents.

## 🌟 Features

- **Document Analysis**: Upload and analyze financial document images (PNG, JPG, JPEG)
- **Text Extraction**: Automatically extract text from images using OCR
- **AI-Powered Insights**: Generate comprehensive financial analysis using Groq's LLM
- **Key Metrics Extraction**: Identify and highlight important financial metrics
- **Interactive UI**: User-friendly interface with real-time analysis
- **Analysis History**: Track and review previous analyses
- **Customizable Prompts**: Tailor analysis to specific needs
- **Export Capabilities**: Download analysis results in text format

## 📋 Table of Contents

- [Demo](#demo)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Configuration](#configuration)
- [Technologies Used](#technologies-used)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## 🎥 Demo

[Add your demo GIF or screenshot here]

## 🚀 Installation

### Prerequisites

1. **Python 3.8 or higher**
2. **Tesseract OCR**

#### Installing Tesseract OCR

##### Windows:
1. Download the Tesseract installer from: https://github.com/UB-Mannheim/tesseract/wiki
   - Choose the latest version (e.g., `tesseract-ocr-w64-setup-5.3.3.20231005.exe`)
2. Run the installer
3. During installation:
   - Remember the installation path (default is `C:\Program Files\Tesseract-OCR`)
   - Check "Add to system PATH" during installation
4. Add Tesseract to PATH manually if not done during installation:
   - Open System Properties (Win + Pause/Break)
   - Click "Advanced system settings"
   - Click "Environment Variables"
   - Under "System variables", find and select "Path"
   - Click "Edit"
   - Click "New"
   - Add the Tesseract installation path (e.g., `C:\Program Files\Tesseract-OCR`)
   - Click "OK" on all windows

##### Linux (Ubuntu/Debian):
```bash
sudo apt-get update
sudo apt-get install tesseract-ocr
```

##### macOS:
```bash
brew install tesseract
```

### Project Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/financial-ai-scanner.git
cd financial-ai-scanner
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
   - Create a `.env` file in the root directory
   - Add your Groq API key:
   ```
   GROQ_API_KEY=your_api_key_here
   ```

## 💻 Usage

1. Start the application:
```bash
streamlit run app.py
```

2. Open your web browser and navigate to the provided URL (usually http://localhost:8501)

3. Upload a financial document image:
   - Click "Choose a financial document image"
   - Select a PNG, JPG, or JPEG file
   - Wait for the image to be processed

4. View extracted text:
   - Expand the "Extracted Text" section to see OCR results

5. Analyze the document:
   - Click "Analyze Document"
   - Wait for the AI analysis to complete
   - View results in the right column

6. Download results:
   - Click "Download Analysis" to save the analysis as a text file

## 📁 Project Structure

```
financial-ai-scanner/
├── app.py                  # Main Streamlit application
├── utils/
│   ├── __init__.py
│   ├── image_processor.py  # Image processing utilities
│   ├── llm_handler.py      # LLM integration functions
│   └── financial_utils.py  # Financial analysis utilities
├── requirements.txt        # Project dependencies
├── .env                    # Environment variables
└── README.md              # Project documentation
```

## ⚙️ Configuration

### Customizing Analysis Prompts

You can customize the analysis prompt in the sidebar:
1. Locate the "Customize Analysis Prompt" section
2. Modify the prompt template
3. Click "Analyze Document" to apply changes

### Environment Variables

Required environment variables:
- `GROQ_API_KEY`: Your Groq API key for LLM access

## 🛠️ Technologies Used

- **Python 3.8+**: Core programming language
- **Streamlit**: Web application framework
- **Groq API**: LLM service for document analysis
- **Pillow**: Image processing
- **Pytesseract**: OCR for text extraction
- **python-dotenv**: Environment variable management
- **pandas & numpy**: Data processing
- **plotly**: Data visualization (if needed)

## 🔧 Troubleshooting

### Common Issues

1. **Tesseract not found**
   - Ensure Tesseract is installed and in PATH
   - Follow installation instructions in the Prerequisites section

2. **Groq API Error**
   - Verify your API key in the `.env` file
   - Check internet connectivity
   - Ensure the API key has sufficient credits

3. **Image Processing Error**
   - Verify image format (PNG, JPG, JPEG)
   - Check image size (should not be too large)
   - Ensure image is not corrupted

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Contact

Your Name - [@yourtwitter](https://twitter.com/yourtwitter) - email@example.com

Project Link: [https://github.com/yourusername/financial-ai-scanner](https://github.com/yourusername/financial-ai-scanner)

## 🙏 Acknowledgments

- Groq API for providing the LLM service
- Streamlit team for the excellent web framework
- Tesseract OCR team for the powerful text extraction tool
- All contributors and users of this project 