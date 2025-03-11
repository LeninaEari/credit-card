import streamlit as st
import pickle
import pandas as pd

# Load the trained model
with open("model5.pkl", "rb") as model_file:
    model5 = pickle.load(model_file)

# Streamlit UI
st.title("Credit Card Default Prediction")

st.markdown("Enter details to predict if a user will default on their credit card payment.")

# Collect user input
SEX = st.selectbox("Sex", [1, 2], format_func=lambda x: "Male" if x == 1 else "Female")
MARRIAGE = st.selectbox("Marriage", [1, 2, 3], format_func=lambda x: "Married" if x == 1 else "Single" if x == 2 else "Others")
AGE = st.number_input("Age", min_value=18, max_value=100, value=30)
BILL_AMT1 = st.number_input("Last Bill Amount", min_value=0, value=50000)
EDUCATION = st.selectbox("Education Level", [1, 2, 3, 4], format_func=lambda x: "Graduate School" if x == 1 else "University" if x == 2 else "High School" if x == 3 else "Others")
PAY_1 = st.selectbox("Previous Payment Status", [-2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8])

# Create input DataFrame
input_data = pd.DataFrame([[SEX, MARRIAGE, AGE, BILL_AMT1, EDUCATION, PAY_1]],
                          columns=['SEX', 'MARRIAGE', 'AGE', 'BILL_AMT1', 'EDUCATION', 'PAY_1'])

# Prediction Button
if st.button("Predict Default"):
    prediction = model5.predict(input_data)[0]
    result = "🔴 Likely to Default" if prediction == 1 else "🟢 Not Likely to Default"
    st.markdown(f"## Prediction: {result}")
