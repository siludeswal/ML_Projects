import streamlit as st
import joblib
import numpy as np

# ----------------------------
# Page Configuration
# ----------------------------
st.set_page_config(
    page_title="Virus Detection System",
    page_icon="🦠",
    layout="centered"
)

# ----------------------------
# Load Model
# ----------------------------
@st.cache_resource
def load_model():
    return joblib.load("best_model_mouse_viral.joblib")

model = load_model()

# ----------------------------
# Custom CSS
# ----------------------------
st.markdown("""
<style>
/* Main app background */
.stApp {
    background-image: url("https://images.unsplash.com/photo-1584036561584-b03c19da874c");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}

/* White content container */
.main {
    background-color: rgba(255, 255, 255, 0.92);
    padding: 30px;
    border-radius: 15px;
    box-shadow: 0px 0px 30px rgba(0,0,0,0.3);
}

/* Title */
.title {
    text-align: center;
    font-size: 38px;
    font-weight: bold;
    color: #ff4b4b;
}

/* Subtitle */
.subtitle {
    text-align: center;
    font-size: 18px;
    color: #333;
    margin-bottom: 30px;
}

/* Card */
.card {
    background-color: #f9f9f9;
    padding: 25px;
    border-radius: 12px;
    box-shadow: 0 8px 20px rgba(0,0,0,0.15);
}

/* Buttons */
.stButton > button {
    background-color: #ff4b4b;
    color: white;
    font-size: 18px;
    font-weight: bold;
    border-radius: 10px;
    padding: 12px;
}

/* Result text */
.success {
    color: green;
    font-size: 22px;
    font-weight: bold;
}

.danger {
    color: red;
    font-size: 22px;
    font-weight: bold;
}

/* Footer */
.footer {
    text-align: center;
    margin-top: 30px;
    color: #eee;
}
</style>
""", unsafe_allow_html=True)


# ----------------------------
# Title Section
# ----------------------------
st.markdown('<div class="title">🦠 Virus Detection System</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Predict virus presence using medicine dosage</div>', unsafe_allow_html=True)

# ----------------------------
# Input Card
# ----------------------------
st.markdown('<div class="card">', unsafe_allow_html=True)

med1 = st.number_input("💊 Medicine 1 (mL)", min_value=0.0, step=0.1)
med2 = st.number_input("💊 Medicine 2 (mL)", min_value=0.0, step=0.1)

st.markdown('</div>', unsafe_allow_html=True)

st.write("")

# ----------------------------
# Prediction
# ----------------------------
if st.button("🔍 Predict Virus", use_container_width=True):
    input_data = np.array([[med1, med2]])
    prediction = model.predict(input_data)[0]

    st.write("")

    if prediction == 1:
        st.markdown('<div class="danger">⚠️ Virus Detected</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="success">✅ No Virus Detected</div>', unsafe_allow_html=True)

# ----------------------------
# Footer
# ----------------------------
st.markdown("""
<div class="footer">
    <hr>
    <p>🚀 Deployed by Sahil Deswal</p>
</div>
""", unsafe_allow_html=True)
