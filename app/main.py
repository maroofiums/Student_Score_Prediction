# app.py

import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Load the saved model
model = joblib.load("best_student_score_model.pkl")

# App title
st.title("📊 Student Exam Score Predictor")

st.write("""
Predict a student's exam score based on study hours, sleep hours, attendance, and previous scores.
""")

# User Inputs
hours_studied = st.slider("Hours Studied per Day", 0, 12, 6)
sleep_hours = st.slider("Sleep Hours per Day", 4, 12, 7)
attendance_percent = st.slider("Attendance Percent", 0, 100, 75)
previous_scores = st.slider("Previous Exam Scores", 0, 100, 65)

# Create DataFrame for prediction
input_df = pd.DataFrame({
    "hours_studied": [hours_studied],
    "sleep_hours": [sleep_hours],
    "attendance_percent": [attendance_percent],
    "previous_scores": [previous_scores]
})

# Predict button
if st.button("Predict Exam Score"):
    prediction = model.predict(input_df)
    st.success(f"Predicted Exam Score: {round(prediction[0], 2)}")
