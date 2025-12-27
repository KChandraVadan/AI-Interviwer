import streamlit as st
import requests

st.title("🎓 AI Interviewer Demo")

audio = st.file_uploader("Upload Speech Audio")
image = st.file_uploader("Upload Screen Image")

if audio:
    r = requests.post("http://localhost:8000/transcribe", files={"audio": audio})
    st.write("Transcript:", r.json())

if image:
    r = requests.post("http://localhost:8000/ocr", files={"image": image})
    st.write("Screen Content:", r.json())

if st.button("Ask Question"):
    r = requests.get("http://localhost:8000/question")
    st.success(r.json()["question"])

if st.button("Generate Final Score"):
    r = requests.get("http://localhost:8000/final-score")
    st.json(r.json())
