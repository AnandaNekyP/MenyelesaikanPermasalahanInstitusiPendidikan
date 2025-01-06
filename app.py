import streamlit as st
import joblib
import numpy as np
import pandas as pd
import random

# Load the trained model, scaler, and min-max values
minmax = pd.read_csv('data/min_max_values.csv')
model = joblib.load('model/dropout_model.pkl')
scaler = joblib.load('model/power_transformer.pkl')

# Function to make predictions
def predict_status(inputs):
    # Convert inputs to numpy array and reshape
    input_array = np.array(inputs).reshape(1, -1)
    input_array = scaler.transform(input_array)
    prediction = model.predict(input_array)
    return prediction

# Function to randomize input values within the range
def randomize_inputs():
    randomized_inputs = {}
    for row in minmax['Column']:
        min_val = minmax.loc[minmax['Column'] == row, 'Min Value'].values[0]
        max_val = minmax.loc[minmax['Column'] == row, 'Max Value'].values[0]
        
        # Randomize the value within the range, keeping the same type
        if isinstance(min_val, float) and isinstance(max_val, float):
            randomized_inputs[row] = round(random.uniform(min_val, max_val), 2)
        else:
            randomized_inputs[row] = random.randint(min_val, max_val)
    return randomized_inputs

# Create the Streamlit app
st.set_page_config(page_title="Student Dropout Prediction", layout="wide")
st.title("🎓 Student Dropout Prediction")

# Display a description of the app
st.markdown("""
This app predicts whether a student is likely to drop out based on their personal and academic information.
Fill in the details for each field below and press **Predict** to see the result.
You can also click **Randomize Inputs** to automatically fill in random values for the inputs.
""")

# Initialize session state for storing inputs if not already present
if 'inputs' not in st.session_state:
    st.session_state.inputs = {}

# Create the input sections in columns
col1, col2 = st.columns([2, 1])

# Column 1: Input Fields
with col1:
    st.subheader("Enter Student Information")

    # Create input fields for each column from the dataset
    for row in minmax['Column']:
        min_val = minmax.loc[minmax['Column'] == row, 'Min Value'].values[0]
        max_val = minmax.loc[minmax['Column'] == row, 'Max Value'].values[0]
        
        # Calculate step size based on min-max difference if the values are float
        if isinstance(min_val, float) and isinstance(max_val, float):
            step = round((max_val - min_val) / 100, 2)  # Adjust step to fit the range
        else:
            step = 1
        
        # If the input already exists in session_state, use it; otherwise, create a new slider
        st.session_state.inputs[row] = st.slider(
            row,
            min_val,
            max_val,
            value=st.session_state.inputs.get(row, min_val),  # Use previous value if exists
            step=step,  # Adjusted step size
            help=f"Adjust the slider for {row} (Min: {min_val}, Max: {max_val})"
        )


# Column 2: Prediction Button and Result
with col2:
    # Show the input data in a nice format for user review
    st.write("### Your Input Data:")
    st.write(st.session_state.inputs)

    st.subheader("Prediction Results")

    # Make prediction when the user clicks the button
    if st.button('Predict'):
        # Call prediction function
        prediction = predict_status(list(st.session_state.inputs.values()))

        # Display the prediction result with styling
        st.write("### 📊 Prediction Result:")
        result = "Dropout" if prediction[0] == 1 else "Not Dropout"
        st.markdown(f"**The prediction is:** {result}")

    # Add the "Randomize Inputs" button
    if st.button("Randomize Inputs"):
        randomized_inputs = randomize_inputs()
        st.session_state.inputs = randomized_inputs  # Update session_state with randomized inputs
        st.write("### Randomized Input Data:")
        st.write(randomized_inputs)


