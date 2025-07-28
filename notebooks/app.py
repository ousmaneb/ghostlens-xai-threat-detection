import streamlit as st
import pandas as pd
import joblib
import json
import os

# Paths
MODEL_PATH = 'models/random_forest_ddos_model.pkl'
FEATURES_PATH = 'models/feature_names.json'

# Check for required files
if not os.path.exists(MODEL_PATH) or not os.path.exists(FEATURES_PATH):
    st.error("Model or feature names file not found in 'models/'. Please make sure both files exist.")
    st.stop()

# Load model
model = joblib.load(MODEL_PATH)

# Load feature names used during training (do not modify them)
with open(FEATURES_PATH, 'r') as f:
    expected_features = json.load(f)

# App title and description
st.title("GhostLens: Threat Detection")
st.markdown("""
Upload a CSV file containing network traffic data without the `Label` column.  
The file must match the exact structure and column names used during training.
""")

# File upload
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    try:
        data = pd.read_csv(uploaded_file)
        # Strip only leading/trailing whitespace
        data.columns = [col.strip() for col in data.columns]

        # Keep only numeric columns (optional if your data is mixed)
        data = data.select_dtypes(include='number')

        # Handle infinities and missing values
        data.replace([float('inf'), -float('inf')], 0, inplace=True)
        data.dropna(inplace=True)

        # Check for missing columns
        missing_cols = [col for col in expected_features if col not in data.columns]
        if missing_cols:
            st.error(f"Your file is missing the following required columns:\n\n{missing_cols}")
            st.stop()

        # Reorder columns to match training order
        data = data[expected_features]

        # Predict
        predictions = model.predict(data)
        result_df = pd.DataFrame({'Prediction': predictions})
        result_df['Prediction'] = result_df['Prediction'].map({0: 'BENIGN', 1: 'DDoS'})

        # Show preview
        st.subheader("Preview of Uploaded Data")
        st.dataframe(data.head())

        st.subheader("Prediction Results")
        st.dataframe(result_df)

        # Download button
        csv = result_df.to_csv(index=False)
        st.download_button(
            label="Download Results as CSV",
            data=csv,
            file_name='ghostlens_predictions.csv',
            mime='text/csv'
        )

    except Exception as e:
        st.error(f"Error processing the uploaded file: {e}")
