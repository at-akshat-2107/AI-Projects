"""
Image processing utilities for handling financial document images.
"""
from PIL import Image
import io
import base64
import os
import pytesseract
from typing import List, Tuple
import platform

class DocumentProcessor:
    """Class to handle document processing for images."""
    
    def __init__(self):
        """Initialize the document processor."""
        self.temp_dir = "temp"
        if not os.path.exists(self.temp_dir):
            os.makedirs(self.temp_dir)
        
        # Check Tesseract installation
        self._check_tesseract_installation()

    def _check_tesseract_installation(self):
        """Check if Tesseract is installed and accessible."""
        try:
            pytesseract.get_tesseract_version()
        except Exception as e:
            if "tesseract" in str(e).lower():
                system = platform.system().lower()
                if system == "windows":
                    raise Exception(
                        "Tesseract is not installed or not in PATH. Please:\n"
                        "1. Download Tesseract from: https://github.com/UB-Mannheim/tesseract/wiki\n"
                        "2. Run the installer and check 'Add to system PATH'\n"
                        "3. If not added to PATH, add manually:\n"
                        "   - Open System Properties (Win + Pause/Break)\n"
                        "   - Click 'Advanced system settings'\n"
                        "   - Click 'Environment Variables'\n"
                        "   - Under 'System variables', find 'Path'\n"
                        "   - Add Tesseract installation path (e.g., C:\\Program Files\\Tesseract-OCR)"
                    )
                elif system == "linux":
                    raise Exception(
                        "Tesseract is not installed. Please install it using:\n"
                        "sudo apt-get update\n"
                        "sudo apt-get install tesseract-ocr"
                    )
                elif system == "darwin":  # macOS
                    raise Exception(
                        "Tesseract is not installed. Please install it using:\n"
                        "brew install tesseract"
                    )
                else:
                    raise Exception("Tesseract is not installed or not in PATH")

    def process_document(self, uploaded_file) -> Tuple[List[Image.Image], str]:
        """
        Process uploaded image and extract text.
        
        Args:
            uploaded_file: StreamlitUploadedFile object
            
        Returns:
            Tuple[List[Image.Image], str]: List containing single image and extracted text
        """
        try:
            # Load and process image
            image = Image.open(uploaded_file)
            
            # Extract text using OCR
            text = pytesseract.image_to_string(image)
            
            return [image], text
            
        except Exception as e:
            raise Exception(f"Error processing image: {str(e)}")

def load_image(uploaded_file):
    """
    Load and process an uploaded image file.
    
    Args:
        uploaded_file: StreamlitUploadedFile object
        
    Returns:
        PIL.Image: Processed image object
    """
    try:
        image = Image.open(uploaded_file)
        return image
    except Exception as e:
        raise Exception(f"Error loading image: {str(e)}")

def image_to_base64(image):
    """
    Convert PIL image to base64 string.
    
    Args:
        image: PIL.Image object
        
    Returns:
        str: Base64 encoded image string
    """
    buffered = io.BytesIO()
    image.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()

def preprocess_image(image):
    """
    Preprocess image for analysis.
    
    Args:
        image: PIL.Image object
        
    Returns:
        PIL.Image: Preprocessed image
    """
    # Convert to RGB if necessary
    if image.mode != 'RGB':
        image = image.convert('RGB')
    
    # Resize if too large (maintain aspect ratio)
    max_size = 1600
    if max(image.size) > max_size:
        ratio = max_size / max(image.size)
        new_size = tuple(int(dim * ratio) for dim in image.size)
        image = image.resize(new_size, Image.Resampling.LANCZOS)
    
    return image 