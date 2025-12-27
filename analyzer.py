def analyze_content(text):
    insights = {
        "tech_stack": [],
        "complexity": "medium",
        "topics": []
    }

    if "API" in text or "FastAPI" in text:
        insights["tech_stack"].append("Backend API")

    if "model" in text or "training" in text:
        insights["topics"].append("Machine Learning")

    return insights
