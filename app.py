
import streamlit as st
from textblob import TextBlob
import pandas as pd
import random

st.title("WellnessWise: Mood and Health Tracker")

# Mood Tracker
st.header("🧠 Mood Tracker")
mood_input = st.text_area("How are you feeling today?")
if st.button("Analyze Mood"):
    blob = TextBlob(mood_input)
    polarity = blob.sentiment.polarity
    if polarity > 0:
        mood = "😊 Positive"
    elif polarity < 0:
        mood = "😟 Negative"
    else:
        mood = "😐 Neutral"
    st.success(f"Detected Mood: {mood}")

# Symptom Checker
st.header("🩺 Symptom Checker")
fever = st.checkbox("Fever")
cough = st.checkbox("Cough")
fatigue = st.checkbox("Fatigue")

if st.button("Check Condition"):
    if fever and cough and fatigue:
        st.warning("Possible Flu. Please consult a doctor.")
    elif cough and not fever:
        st.info("Mild cold symptoms. Stay hydrated.")
    else:
        st.success("You seem fine. Keep taking care!")

# Wellness Tips
st.header("🌱 Daily Wellness Tip")
tips = [
    "Take a 5-minute breathing break.",
    "Drink 2L of water today.",
    "Avoid screens 30 minutes before bed.",
    "Go for a short walk.",
    "Practice gratitude — write 3 good things."
]

if st.button("Get a Tip"):
    st.info(random.choice(tips))

# Progress Tracker
st.header("📊 Progress Tracker")
if 'mood_data' not in st.session_state:
    st.session_state.mood_data = []

if st.button("Save Mood"):
    blob = TextBlob(mood_input)
    polarity = blob.sentiment.polarity
    st.session_state.mood_data.append({'text': mood_input, 'mood': polarity})

if st.session_state.mood_data:
    df = pd.DataFrame(st.session_state.mood_data)
    st.line_chart(df['mood'])
