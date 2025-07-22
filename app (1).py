
import streamlit as st
import random
from datetime import datetime

st.set_page_config(page_title="WellnessWise", layout="centered")

st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    .stTextInput>div>div>input { background-color: #1e222d; color: white; }
    .stButton>button { background-color: #4CAF50; color: white; }
    </style>
""", unsafe_allow_html=True)

st.title("💖 WellnessWise: Mood, Health, and Wellness Companion")

# Mood Tracker
st.header("🧠 Mood Tracker")
mood_input = st.text_area("How are you feeling today?", placeholder="e.g., I'm feeling stressed and tired.")

if st.button("Analyze Mood"):
    if any(word in mood_input.lower() for word in ["sad", "not well", "stress", "tired", "angry"]):
        st.error("You seem to be feeling low. Try to take some rest or talk to a friend ❤️")
    else:
        st.success("Glad to hear you're doing okay! Keep it up 🌟")

# Symptom Checker
st.header("🩺 Symptom Checker")
symptoms = st.multiselect("Select symptoms:", 
    ["Fever", "Cough", "Headache", "Fatigue", "Nausea", "Shortness of breath"])

if symptoms:
    if {"Fever", "Cough"} <= set(symptoms):
        st.warning("Possible flu or COVID-19 symptoms. Consider visiting a healthcare provider.")
    elif {"Headache", "Fatigue"} <= set(symptoms):
        st.info("Could be stress or dehydration. Drink water and rest.")
    else:
        st.info("Monitor your symptoms. Stay hydrated and rest.")

# Smart Wellness Tips
st.header("💡 Smart Wellness Tip")
if st.button("Get a Tip"):
    tips = [
        "Take a short walk to reset your mood.",
        "Stay hydrated – have a glass of water.",
        "Try 4-7-8 breathing for relaxation.",
        "Write down 3 things you're grateful for.",
        "Get some sunlight for 10 minutes!"
    ]
    st.success(random.choice(tips))

# Progress Tracker
st.header("📈 Daily Wellness Log")
if "log" not in st.session_state:
    st.session_state.log = []

entry = st.text_input("Write a short log for today:")
if st.button("Add Entry"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    st.session_state.log.append(f"[{timestamp}] {entry}")
    st.success("Log added!")

if st.session_state.log:
    st.subheader("📝 Your Entries:")
    for log in reversed(st.session_state.log):
        st.text(log)
