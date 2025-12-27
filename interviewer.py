def generate_questions(context):
    """
    Generates adaptive interview questions based on:
    1. Screen content (OCR output)
    2. Previous student responses (STT output)
    """

    content = context.get("content", "").lower()
    responses = " ".join(context.get("responses", [])).lower()

    # --- Adaptive logic based on responses ---
    if "model" in responses or "algorithm" in responses:
        return (
            "You mentioned a model in your explanation. "
            "Why did you choose this model over other alternatives?"
        )

    if "accuracy" in responses or "metric" in responses:
        return (
            "What evaluation metrics did you use, and "
            "what trade-offs did you consider while optimizing them?"
        )

    if "dataset" in responses or "data" in responses:
        return (
            "Can you explain how the data was collected and "
            "what preprocessing steps were applied?"
        )

    # --- Adaptive logic based on screen content ---
    if "api" in content or "fastapi" in content or "backend" in content:
        return (
            "How does your backend architecture handle scalability "
            "and error handling?"
        )

    if "architecture" in content or "pipeline" in content:
        return (
            "Can you walk me through the end-to-end architecture "
            "of your system?"
        )

    # --- Fallback question ---
    return (
        "Can you explain the overall idea of your project and "
        "what problem it is solving?"
    )
