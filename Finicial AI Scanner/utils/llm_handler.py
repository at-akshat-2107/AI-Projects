"""
LLM handler module for interacting with Groq API.
"""
import os
from dotenv import load_dotenv
import groq
import base64

# Load environment variables
load_dotenv()

class LLMHandler:
    """
    Handler class for LLM operations using Groq API.
    """
    
    def __init__(self):
        """Initialize the LLM handler with API credentials."""
        self.api_key = os.getenv('GROQ_API_KEY')
        if not self.api_key:
            raise ValueError("GROQ_API_KEY not found in environment variables")
        self.client = groq.Client(api_key=self.api_key)
        self.model = "llama-3.2-90b-vision-preview"

    def generate_financial_analysis(self, image_base64, prompt_template):
        """
        Generate financial analysis from image using Groq API.
        
        Args:
            image_base64 (str): Base64 encoded image string
            prompt_template (str): Template for analysis prompt
            
        Returns:
            str: Generated analysis text
        """
        try:
            # Prepare the prompt with the image
            messages = [
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/png;base64,{image_base64}"
                            }
                        },
                        {
                            "type": "text",
                            "text": prompt_template
                        }
                    ]
                }
            ]
            
            # Make API call
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=0.1,
                max_tokens=2000
            )
            
            return response.choices[0].message.content
            
        except Exception as e:
            raise Exception(f"Error in LLM analysis: {str(e)}")

    def get_default_prompt(self):
        """
        Get default prompt template for financial analysis.
        
        Returns:
            str: Default prompt template
        """
        return """Please analyze this financial document image and provide:
1. Key Financial Metrics
2. Income and Expenses Analysis
3. Balance Sheet Highlights
4. Credit Quality Indicators
5. Strategic and Operational Updates
6. Market Conditions and Outlook

Format the response in a clear, structured manner with bullet points and sections.""" 