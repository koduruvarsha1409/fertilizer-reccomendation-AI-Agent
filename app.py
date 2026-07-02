import streamlit as st
import pandas as pd
import joblib

# -----------------------------
# Page Title
# -----------------------------
st.set_page_config(page_title="Fertilizer Recommendation", page_icon="🌱")

st.title("🌱 Fertilizer Recommendation Agent")
st.write("Enter the soil details to get the recommended fertilizer.")

# -----------------------------
# Load Model and Label Encoders
# -----------------------------
try:
    model = joblib.load("fertilizer_xgboost.pkl")
    label_encoders = joblib.load("label_encoders.pkl")
except Exception as e:
    st.error("Error loading model or label encoders.")
    st.exception(e)
    st.stop()

# -----------------------------
# User Inputs
# -----------------------------
temperature = st.number_input(
    "Temperature (°C)",
    min_value=0.0,
    max_value=100.0,
    value=25.0
)

humidity = st.number_input(
    "Humidity (%)",
    min_value=0.0,
    max_value=100.0,
    value=60.0
)

moisture = st.number_input(
    "Moisture",
    min_value=0.0,
    max_value=100.0,
    value=40.0
)

soil = st.selectbox(
    "Soil Type",
    label_encoders["Soil Type"].classes_
)

crop = st.selectbox(
    "Crop Type",
    label_encoders["Crop Type"].classes_
)

nitrogen = st.number_input(
    "Nitrogen",
    min_value=0,
    max_value=200,
    value=30
)

potassium = st.number_input(
    "Potassium",
    min_value=0,
    max_value=200,
    value=20
)

phosphorous = st.number_input(
    "Phosphorous",
    min_value=0,
    max_value=200,
    value=15
)

# -----------------------------
# Predict Button
# -----------------------------
if st.button("🌾 Recommend Fertilizer"):

    try:

        # Encode categorical values
        soil_encoded = label_encoders["Soil Type"].transform([soil])[0]
        crop_encoded = label_encoders["Crop Type"].transform([crop])[0]

        # Create dataframe
        feature_names = model.get_booster().feature_names

input_data = pd.DataFrame(
    [[
        temperature,
        humidity,
        moisture,
        soil_encoded,
        crop_encoded,
        nitrogen,
        potassium,
        phosphorous
    ]],
    columns=feature_names
)
        # -----------------------------
        # Debug Information
        # -----------------------------
        st.subheader("Input Data")
        

        st.write("Column Names:")
        

        # -----------------------------
        # Prediction
        # -----------------------------
        prediction = model.predict(input_data)

        st.write("Prediction Value:")
        st.write(prediction)

        # -----------------------------
        # Decode Prediction
        # -----------------------------
        fertilizer = label_encoders["Fertilizer Name"].inverse_transform(prediction)

        st.success(f"✅ Recommended Fertilizer: {fertilizer[0]}")

    except Exception as e:

        st.error("Prediction Failed")
        st.exception(e)
