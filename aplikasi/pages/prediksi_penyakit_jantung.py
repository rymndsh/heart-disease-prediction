import streamlit as st
import numpy as np
import pickle
import os

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="Heart Disease Prediction", layout="centered")

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; background-color: #fcfcfc; }
    .stApp { background-image: url("https://www.transparenttextures.com/patterns/cubes.png"); background-attachment: fixed; }
    .main-container { background: rgba(255, 255, 255, 0.9); padding: 30px; border-radius: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.03); border: 1px solid #f0f0f0; }
    .title-text { text-align: center; color: #E94E77; font-weight: 600; margin-bottom: 5px; }
    .subtitle-text { text-align: center; color: #7f8c8d; font-size: 14px; margin-bottom: 30px; }
    hr { border: 0; height: 1px; background: linear-gradient(to right, transparent, #E94E77, transparent); margin: 20px 0; }
    .stButton>button { width: 100%; border-radius: 12px; height: 50px; background-color: #E94E77; color: white; border: none; font-weight: 600; transition: all 0.3s ease; }
    .stButton>button:hover { background-color: #D43F67; transform: translateY(-2px); box-shadow: 0 5px 15px rgba(233, 78, 119, 0.3); }
    </style>
""", unsafe_allow_html=True)

# --- LOAD MODEL (ROBUST PATH METHOD) ---
# Mencari lokasi file secara dinamis agar tidak error di Cloud
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(current_dir)
model_path = os.path.join(root_dir, 'penyakit_jantung_xgb.sav')

try:
    model = pickle.load(open(model_path, 'rb'))
    model_loaded = True
except Exception as e:
    model_loaded = False
    st.error(f"🚨 Failed to load model! Could not find 'penyakit_jantung_xgb.sav'.")
    st.info(f"System was looking in: {model_path}")

# --- HEADER ---
st.markdown('<h1 class="title-text">🫀 Heart Disease Prediction</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle-text">Analyze patient health data with machine learning precision</p>', unsafe_allow_html=True)
st.markdown('<hr>', unsafe_allow_html=True)

# --- FORM LAYOUT ---
with st.container():
    st.subheader("📋 Clinical Information")
    col1, col2 = st.columns(2)
    
    with col1:
        age = st.number_input("Age", min_value=1, max_value=120, value=25)
        sex = st.selectbox("Sex", [("Male", 1), ("Female", 0)], format_func=lambda x: x[0])[1]
        cp = st.selectbox("Chest Pain Type (cp)", [("Type 0", 0), ("Type 1", 1), ("Type 2", 2), ("Type 3", 3)], format_func=lambda x: x[0])[1]
        trestbps = st.number_input("Resting Blood Pressure (trestbps)", min_value=80, max_value=200, value=120)
        chol = st.number_input("Cholesterol (chol)", min_value=100, max_value=600, value=200)
        fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", [("No", 0), ("Yes", 1)], format_func=lambda x: x[0])[1]

    with col2:
        restecg = st.selectbox("Resting ECG Results", [("Normal", 0), ("Abnormal", 1), ("Hypertrophy", 2)], format_func=lambda x: x[0])[1]
        thalach = st.number_input("Max Heart Rate (thalach)", min_value=60, max_value=220, value=150)
        exang = st.selectbox("Exercise Induced Angina", [("No", 0), ("Yes", 1)], format_func=lambda x: x[0])[1]
        oldpeak = st.number_input("ST Depression (oldpeak)", min_value=0.0, step=0.1, value=0.0)
        slope = st.selectbox("Slope of ST Segment", [("Upsloping", 1), ("Flat", 2), ("Downsloping", 3)], format_func=lambda x: x[0])[1]
        ca = st.slider("Number of Major Vessels (ca)", 0, 4, 0)
        thal = st.selectbox("Thalassemia", [("Normal", 3), ("Fixed Defect", 6), ("Reversable Defect", 7)], format_func=lambda x: x[0])[1]

st.markdown("<br>", unsafe_allow_html=True)

# --- PREDICTION LOGIC ---
if st.button("🔍 Run Analysis"):
    if not model_loaded:
        st.error("Cannot run analysis because the model file is missing.")
    else:
        input_data = np.array([[age, sex, cp, trestbps, chol, fbs, restecg,
                                 thalach, exang, oldpeak, slope, ca, thal]], dtype=np.float64)

        prediction = model.predict(input_data)
        probability = model.predict_proba(input_data)[0]

        st.markdown("---")
        
        if prediction[0] == 1:
            st.error(f"### Patient Indicates Heart Disease", icon="🚨")
            st.metric("Risk Level", f"{probability[1]*100:.1f}%")
            st.warning("Please consult a cardiologist immediately for further examination.")
        else:
            st.success(f"### Patient's Heart Looks Healthy", icon="💖")
            st.metric("Risk Level", f"{probability[1]*100:.1f}%")
            st.info("Heart condition is within normal limits. Maintain a healthy diet and regular exercise.")

        with st.expander("📄 Data Summary"):
            st.json({
                "Profile": f"{age} yrs, {'M' if sex==1 else 'F'}",
                "Blood Pressure": trestbps,
                "Cholesterol": chol,
                "Prediction": "Positive" if prediction[0] == 1 else "Negative"
            })
