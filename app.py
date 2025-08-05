import streamlit as st
import numpy as np
import pickle

# Load the trained model
model = pickle.load(open('stroke_model (2).pkl', 'rb'))  # adjust the file path if needed

# App title
st.title("🧠 Stroke Prediction App")

st.write("This app predicts whether a person is at risk of a stroke based on medical and demographic information.")

# User inputs
age = st.number_input("Age", min_value=0, max_value=120, value=30)
hypertension = st.selectbox("Hypertension", ["No", "Yes"])
heart_disease = st.selectbox("Heart Disease", ["No", "Yes"])
avg_glucose_level = st.number_input("Average Glucose Level", min_value=0.0, value=90.0)
bmi = st.number_input("BMI", min_value=0.0, value=25.0)

gender = st.radio("Gender", ["Male", "Female", "Other"])
ever_married = st.radio("Ever Married", ["Yes", "No"])
work_type = st.selectbox("Work Type", ["Private", "Self-employed", "Govt_job", "Children", "Never_worked"])
residence_type = st.radio("Residence Type", ["Urban", "Rural"])
smoking_status = st.selectbox("Smoking Status", ["formerly smoked", "never smoked", "smokes", "Unknown"])

# Encoding categorical variables (one-hot encoding with drop_first=True logic)
gender_male = 1 if gender == "Male" else 0
gender_other = 1 if gender == "Other" else 0

ever_married_yes = 1 if ever_married == "Yes" else 0

work_type_never_worked = 1 if work_type == "Never_worked" else 0
work_type_private = 1 if work_type == "Private" else 0
work_type_self_employed = 1 if work_type == "Self-employed" else 0
work_type_children = 1 if work_type == "Children" else 0

residence_type_urban = 1 if residence_type == "Urban" else 0

smoking_status_never_smoked = 1 if smoking_status == "never smoked" else 0
smoking_status_smokes = 1 if smoking_status == "smokes" else 0

# Final feature vector (same order as model was trained on)
features = np.array([[age, 
                      1 if hypertension == "Yes" else 0,
                      1 if heart_disease == "Yes" else 0,
                      avg_glucose_level,
                      bmi,
                      gender_male,
                      gender_other,
                      ever_married_yes,
                      work_type_never_worked,
                      work_type_private,
                      work_type_self_employed,
                      work_type_children,
                      residence_type_urban,
                      smoking_status_never_smoked,
                      smoking_status_smokes]])

# Predict button
if st.button("Predict Stroke Risk"):
    prediction = model.predict(features)
    if prediction[0] == 1:
        st.error("⚠️ The person is likely at **risk of stroke**.")
    else:
        st.success("✅ The person is **not likely** at risk of stroke.")
