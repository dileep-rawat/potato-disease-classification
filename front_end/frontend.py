import streamlit as st
import requests

FASTAPI_URL = "http://127.0.0.1:8000/predict"

st.title("🥔 Potato Disease Classifier")
st.write("Upload a potato leaf image to detect disease.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

    if st.button("Predict"):
        files = {"file": uploaded_file.getvalue()}
        response = requests.post(FASTAPI_URL, files={"file": uploaded_file.getvalue()})

        if response.status_code == 200:
            result = response.json()
            st.success(f"Prediction: {result['class']} ({result['confidence']})")
        else:
            st.error("Error in prediction request")
