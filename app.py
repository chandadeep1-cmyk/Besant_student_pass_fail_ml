
# STEP 3: STUDENT PASS/FAIL WEB APPLICATION

import pickle
import streamlit as st

# Set up the web page
st.title("🎓 Student Pass/Fail Predictor")
st.write("Enter the number of hours studied.")

# Load the saved ML model
with open("Besant_student_model.pkl", "rb") as file:
    model = pickle.load(file)

# Take input from the user
hours = st.number_input(
    "Study hours",
    min_value=0.0,
    max_value=24.0,
    value=4.0,
    step=0.5
)

# Predict when the button is clicked
if st.button("Predict Result"):

    prediction = model.predict([[hours]])[0]
    probability = model.predict_proba([[hours]])[0]

    if prediction == 1:
        st.success("Prediction: Pass")
    else:
        st.error("Prediction: Fail")

    print_probability = round(max(probability) * 100, 2)

    st.write(
        f"Model confidence in its predicted class: "
        f"{print_probability}%"
    )

st.caption(
    "Educational demonstration only. "
    "This model is not suitable for real student assessment."
)
