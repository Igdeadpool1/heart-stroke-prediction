
import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open("stroke_model.pkl", "rb"))

# App title
st.title("Stroke Prediction App")

# Input form
gender = st.selectbox("Gender", ["Male", "Female", "Other"])
age = st.slider("Age", 1, 100)
hypertension = st.selectbox("Hypertension", ["No", "Yes"])
heart_disease = st.selectbox("Heart Disease", ["No", "Yes"])
ever_married = st.selectbox("Ever Married", ["No", "Yes"])
work_type = st.selectbox("Work Type", ["Private", "Self-employed", "Govt_job", "children", "Never_worked"])
residence_type = st.selectbox("Residence Type", ["Urban", "Rural"])
avg_glucose_level = st.slider("Avg Glucose Level", 50.0, 300.0)
bmi = st.slider("BMI", 10.0, 60.0)
smoking_status = st.selectbox("Smoking Status", ["formerly smoked", "never smoked", "smokes", "Unknown"])

# Preprocess inputs
gender = 1 if gender == "Male" else 0
hypertension = 1 if hypertension == "Yes" else 0
heart_disease = 1 if heart_disease == "Yes" else 0
ever_married = 1 if ever_married == "Yes" else 0
residence_type = 1 if residence_type == "Urban" else 0

work_type_dict = {"Private": 0, "Self-employed": 1, "Govt_job": 2, "children": 3, "Never_worked": 4}
smoking_dict = {"formerly smoked": 0, "never smoked": 1, "smokes": 2, "Unknown": 3}

work_type = work_type_dict[work_type]
smoking_status = smoking_dict[smoking_status]

# Predict
if st.button("Predict Stroke Risk"):
    features = np.array([[gender, age, hypertension, heart_disease, ever_married, work_type,
                          residence_type, avg_glucose_level, bmi, smoking_status]])
    prediction = model.predict(features)
    if prediction[0] == 1:
        st.error("⚠️ High Risk of Stroke")
    else:
        st.success("✅ Low Risk of Stroke")
