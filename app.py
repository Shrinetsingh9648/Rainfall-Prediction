import streamlit as st
import pandas as pd
import pickle

st.set_page_config(page_title="Rainfall Predictor", page_icon="🌧️", layout="centered")

# Load model
with open("rainfall_prediction_model.pkl", "rb") as file:
    model_data = pickle.load(file)

model = model_data["model"]
feature_names = model_data["feature_names"]

# Sidebar
with st.sidebar:
    st.title("🌧️ Rainfall Predictor")
    st.markdown("""
    **Built by:** Shrinet  
    **Model:** Random Forest Classifier  
    **Accuracy:** ~74%  
    ---
    Enter today's weather conditions to predict whether it will rain.
    """)

st.header("🌧️ Rainfall Prediction App")
st.caption("Built with ❤️ by Shrinet")

st.write("### Enter Weather Details")

col1, col2 = st.columns(2)

with col1:
    pressure = st.number_input("Pressure (hPa)", min_value=900.0, max_value=1100.0, value=1015.9, step=0.1)
    dewpoint = st.number_input("Dew Point (°C)", min_value=-10.0, max_value=40.0, value=19.9, step=0.1)
    humidity = st.number_input("Humidity (%)", min_value=0.0, max_value=100.0, value=95.0, step=1.0)
    cloud = st.number_input("Cloud Cover (%)", min_value=0.0, max_value=100.0, value=81.0, step=1.0)

with col2:
    sunshine = st.number_input("Sunshine (hours)", min_value=0.0, max_value=15.0, value=0.0, step=0.1)
    winddirection = st.number_input("Wind Direction (degrees)", min_value=0.0, max_value=360.0, value=40.0, step=1.0)
    windspeed = st.number_input("Wind Speed (km/h)", min_value=0.0, max_value=150.0, value=13.7, step=0.1)

st.write("")

if st.button("🔍 Predict Rainfall", use_container_width=True):
    input_data = (pressure, dewpoint, humidity, cloud, sunshine, winddirection, windspeed)
    input_df = pd.DataFrame([input_data], columns=feature_names)

    prediction = model.predict(input_df)
    probability = model.predict_proba(input_df)

    st.write("---")

    if prediction[0] == 1:
        st.success("☔ **Prediction: Rainfall Expected**")
        st.write(f"Confidence: **{probability[0][1]*100:.1f}%**")
    else:
        st.info("☀️ **Prediction: No Rainfall Expected**")
        st.write(f"Confidence: **{probability[0][0]*100:.1f}%**")