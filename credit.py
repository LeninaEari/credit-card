import streamlit as st
import pickle
import os
import pandas as pd

# Check if the model file exists
if os.path.exists("model5.pkl"):
    with open("model5.pkl", "rb") as model_file:
        model5 = pickle.load(model_file)
else:
    st.error("Error: Model file 'model5.pkl' not found. Please upload it.")

# Streamlit UI
st.title("Credit Card Default Prediction")

# User input
SEX = st.selectbox("Sex", [1, 2])
MARRIAGE = st.selectbox("Marriage", [1, 2, 3])
AGE = st.number_input("Age", min_value=18, max_value=100, value=30)
BILL_AMT1 = st.number_input("Last Bill Amount", min_value=0, value=50000)
EDUCATION = st.selectbox("Education Level", [1, 2, 3, 4])
PAY_1 = st.selectbox("Previous Payment Status", [-2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8])

input_data = pd.DataFrame([[SEX, MARRIAGE, AGE, BILL_AMT1, EDUCATION, PAY_1]],
                          columns=['SEX', 'MARRIAGE', 'AGE', 'BILL_AMT1', 'EDUCATION', 'PAY_1'])

if st.button("Predict Default"):
    if "model5" in globals():
        prediction = model5.predict(input_data)[0]
        result = "🔴 Likely to Default" if prediction == 1 else "🟢 Not Likely to Default"
        st.markdown(f"## Prediction: {result}")
    else:
        st.error("Model is not loaded. Please check if 'model5.pkl' exists.")
