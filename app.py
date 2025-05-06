import streamlit as st
import numpy as np
import joblib

# Load the trained model
model = joblib.load("student_performance_model.pkl")

st.title("🎓 Student Performance Predictor")

# User inputs
math = st.number_input("Math Score", 0, 100)
reading = st.number_input("Reading Score", 0, 100)
writing = st.number_input("Writing Score", 0, 100)

gender = st.selectbox("Gender", ["female", "male"])
lunch = st.selectbox("Lunch Type", ["free/reduced", "standard"])
prep = st.selectbox("Test Preparation", ["none", "completed"])
edu = st.selectbox("Parental Education", ["some high school", "high school", "some college", "associate's degree", "bachelor's degree", "master's degree"])
race = st.selectbox("Race/Ethnicity", ["group A", "group B", "group C", "group D", "group E"])

# One-hot encode the categorical inputs (based on your training data!)
input_data = [
    math, reading, writing,
    1 if gender == "male" else 0,
    1 if lunch == "standard" else 0,
    1 if prep == "completed" else 0,
    1 if edu == "high school" else 0,
    1 if edu == "some college" else 0,
    1 if edu == "associate's degree" else 0,
    1 if edu == "bachelor's degree" else 0,
    1 if edu == "master's degree" else 0,
    1 if race == "group B" else 0,
    1 if race == "group C" else 0,
    1 if race == "group D" else 0,
    1 if race == "group E" else 0
]

# Predict
if st.button("Predict Performance"):
    prediction = model.predict([input_data])
    result = "🎉 Pass" if prediction[0] == 1 else "❌ Fail"
    st.success(f"Predicted Performance: {result}")
