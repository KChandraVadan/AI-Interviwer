import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="AI Interviewer", layout="centered")

st.title("🎤 AI-Based Project Interview System")

st.markdown(
    "This demo simulates an automated technical interview based on a student's project presentation."
)

# -------------------------------
# Step A: Upload Presentation
# -------------------------------
st.header("📄 Step A: Upload Presentation (Screen Content)")

image = st.file_uploader("Upload project slide / code screenshot", type=["png", "jpg", "jpeg"])

if image and st.button("Analyze Presentation"):
    files = {"image": image}
    res = requests.post(f"{API_URL}/ocr", files=files)
    st.success("Presentation analyzed")
    st.json(res.json())

# -------------------------------
# Step B: Upload Explanation
# -------------------------------
st.header("🗣️ Step B: Upload Explanation (Speech)")

audio = st.file_uploader("Upload audio explanation", type=["wav", "mp3", "m4a"])

if audio and st.button("Transcribe Explanation"):
    files = {"audio": audio}
    res = requests.post(f"{API_URL}/transcribe", files=files)
    st.success("Explanation captured")
    st.json(res.json())

# -------------------------------
# Step C: Adaptive Question
# -------------------------------
st.header("❓ Step C: Interview Question")

if st.button("Generate Question"):
    res = requests.get(f"{API_URL}/question")
    st.info(res.json()["question"])

# -------------------------------
# Step D: Evaluation
# -------------------------------
st.header("📊 Step D: Final Evaluation")

if st.button("Get Final Score"):
    res = requests.get(f"{API_URL}/final-score")
    st.success("Evaluation Complete")
    st.json(res.json())
