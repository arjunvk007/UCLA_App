import streamlit as st
import joblib
import pandas as pd
import os

st.set_page_config(page_title="🎓 UCLA Admission Predictor", layout="centered")
st.title("🎓 Neural Network Admission Predictor")

# Load trained model
model_path = 'models/admission_nn_model.pkl'
if not os.path.exists(model_path):
    st.error("❌ Model not found. Please train the model using `train.py`.")
    st.stop()

model = joblib.load(model_path)

# Read admission input data from CSV
csv_path = 'Admission(in).csv'
if not os.path.exists(csv_path):
    st.error("❌ Input file 'Admission(in).csv' not found in the directory.")
    st.stop()

st.subheader("📄 Reading admission data from `Admission(in).csv`")
try:
    input_df = pd.read_csv(csv_path)

    # One-hot encode University_Rating and Research
    input_df["University_Rating_2"] = (input_df["University_Rating"] == 2).astype(int)
    input_df["University_Rating_3"] = (input_df["University_Rating"] == 3).astype(int)
    input_df["University_Rating_4"] = (input_df["University_Rating"] == 4).astype(int)
    input_df["University_Rating_5"] = (input_df["University_Rating"] == 5).astype(int)
    input_df["Research_1"] = (input_df["Research"].map(lambda x: str(x).lower() in ['yes', '1', 'true'])).astype(int)

    # Drop original columns not used in model
    input_df = input_df.drop(columns=["University_Rating", "Research"], errors='ignore')

    # Align columns to match model input
    input_df = input_df.reindex(columns=model.feature_names_in_, fill_value=0)

    st.write("📋 Processed input data:")
    st.dataframe(input_df)

    if st.button("🔮 Predict Admission"):
        predictions = model.predict(input_df)
        input_df["Prediction"] = ["🎉 High Chance" if pred == 1 else "❌ Low Chance" for pred in predictions]

        st.subheader("📢 Prediction Results:")
        st.dataframe(input_df[["Prediction"]])

except Exception as e:
    st.error(f"⚠️ Error reading or processing file: {e}")

    
 
