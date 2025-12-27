def extract_text_from_image(image_file):
    """
    OCR abstraction layer.
    For demo: mocked OCR output.
    In production: Tesseract / EasyOCR / Cloud OCR.
    """
    return """
    Project: AI Interviewer System
    Description:
    An AI system that analyzes a student's project presentation,
    generates adaptive interview questions, and evaluates responses.

    Tech Stack:
    - Python
    - FastAPI
    - Whisper (STT)
    - LLM-based analysis

    Components:
    - Speech transcription
    - Content understanding
    - Dynamic questioning
    - Scoring and feedback
    """
