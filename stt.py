def transcribe_audio(audio_file):
    """
    STT abstraction layer.
    Demo uses mocked transcription.
    In production: Whisper / Vosk / Cloud STT.
    """
    return (
        "This project is an AI interviewer system. "
        "It analyzes a student's presentation, "
        "asks adaptive questions, and evaluates responses."
    )
