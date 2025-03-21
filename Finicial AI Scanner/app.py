"""
Financial AI Scanner - Main Application
A Streamlit application for analyzing financial document images using AI.
"""
import streamlit as st
from utils.image_processor import (
    load_image, 
    image_to_base64, 
    preprocess_image,
    DocumentProcessor
)
from utils.llm_handler import LLMHandler
from utils.financial_utils import extract_financial_metrics, format_financial_summary

def initialize_session_state():
    """Initialize session state variables."""
    if 'llm_handler' not in st.session_state:
        st.session_state.llm_handler = LLMHandler()
    if 'analysis_history' not in st.session_state:
        st.session_state.analysis_history = []
    if 'document_processor' not in st.session_state:
        st.session_state.document_processor = DocumentProcessor()

def main():
    """Main application function."""
    st.set_page_config(
        page_title="Financial AI Scanner",
        page_icon="💹",
        layout="wide"
    )
    
    initialize_session_state()
    
    # Application header
    st.title("Financial AI Scanner 💹")
    st.markdown("""
    Upload financial document images for AI-powered analysis and insights.
    Get quick summaries of key metrics, trends, and important information.
    """)
    
    # Sidebar for settings and history
    with st.sidebar:
        st.header("Settings")
        custom_prompt = st.text_area(
            "Customize Analysis Prompt",
            value=st.session_state.llm_handler.get_default_prompt(),
            height=200
        )
        
        st.header("Analysis History")
        for idx, analysis in enumerate(st.session_state.analysis_history):
            with st.expander(f"Analysis {idx + 1}"):
                st.write(analysis)
    
    # Main content area
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.header("Upload Image")
        uploaded_file = st.file_uploader(
            "Choose a financial document image",
            type=['png', 'jpg', 'jpeg'],
            help="Upload financial statements, reports, or charts"
        )
        
        if uploaded_file:
            try:
                # Process image
                images, extracted_text = st.session_state.document_processor.process_document(uploaded_file)
                
                # Display extracted text
                with st.expander("Extracted Text"):
                    st.text_area("", extracted_text, height=200)
                
                # Display image
                st.subheader("Document Image")
                st.image(images[0], caption="Uploaded Document", use_column_width=True)
                
                # Process button
                if st.button("Analyze Document"):
                    with st.spinner("Analyzing document..."):
                        # Preprocess image
                        processed_image = preprocess_image(images[0])
                        image_b64 = image_to_base64(processed_image)
                        
                        # Generate analysis
                        analysis = st.session_state.llm_handler.generate_financial_analysis(
                            image_b64,
                            custom_prompt
                        )
                        
                        # Extract and format metrics
                        metrics = extract_financial_metrics(analysis)
                        formatted_summary = format_financial_summary(metrics)
                        
                        # Store in history
                        st.session_state.analysis_history.append(analysis)
                        
                        # Display results in second column
                        with col2:
                            st.header("Analysis Results")
                            st.markdown(analysis)
                            
                            st.header("Key Metrics Summary")
                            st.markdown(formatted_summary)
                            
                            # Download button
                            st.download_button(
                                "Download Analysis",
                                analysis,
                                file_name="financial_analysis.txt",
                                mime="text/plain"
                            )
                
            except Exception as e:
                st.error(f"Error processing image: {str(e)}")
    
    # Instructions when no file is uploaded
    if not uploaded_file:
        with col2:
            st.info("""
            👈 Start by uploading a financial document image on the left.
            
            Supported image formats:
            - PNG (.png)
            - JPEG (.jpg, .jpeg)
            
            The AI will:
            1. Extract text from the image
            2. Analyze the content for financial insights
            3. Provide key metrics and trends
            4. Generate structured summaries
            """)

if __name__ == "__main__":
    main() 