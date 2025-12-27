def score_student(context):
    responses = " ".join(context["responses"]).lower()
    content = context["content"].lower()

    score = {
        "technical_depth": 5,
        "clarity": 5,
        "originality": 5,
        "implementation": 5
    }

    if "model" in responses or "training" in responses:
        score["technical_depth"] += 2

    if "architecture" in responses or "pipeline" in responses:
        score["implementation"] += 2

    if len(responses.split()) > 40:
        score["clarity"] += 1

    if "custom" in responses or "designed" in responses:
        score["originality"] += 1

    final_score = round(sum(score.values()) / len(score), 2)

    return {
        "score_breakdown": score,
        "final_score": final_score,
        "feedback": [
            "Good technical understanding.",
            "Clear explanation of core ideas.",
            "Can improve depth with more metrics and trade-offs."
        ]
    }
