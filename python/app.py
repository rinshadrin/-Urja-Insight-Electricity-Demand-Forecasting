import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt

# Page Config
st.set_page_config(
    page_title="Electricity Demand Forecasting",
    page_icon="⚡",
    layout="wide"
)

# Load Model
model = joblib.load("decision_tree_model.pkl")

# Title
st.title("⚡ Electricity Demand Forecasting Dashboard")
st.markdown("Machine Learning based Electricity Demand Prediction using Decision Tree Regressor")

# Sidebar
st.sidebar.header("Navigation")

page = st.sidebar.radio(
    "Select Page",
    ["Home", "Dataset", "Prediction", "Feature Importance"]
)

# ---------------- HOME ----------------
if page == "Home":

    st.header("Project Overview")

    st.write("""
    This project forecasts electricity demand using machine learning.
    The Decision Tree Regressor model is trained using:
    
    - Year
    - Month
    - Peak Met
    - Energy Requirement
    
    Target Variable:
    - Peak Demand
    """)

    col1, col2, col3 = st.columns(3)

    col1.metric("Model", "Decision Tree")
    col2.metric("Target", "Peak Demand")
    col3.metric("Task", "Forecasting")

# ---------------- DATASET ----------------
elif page == "Dataset":

    st.header("Dataset Preview")

    uploaded_file = st.file_uploader(
        "Upload Dataset",
        type=["csv"]
    )

    if uploaded_file:

        df = pd.read_csv(uploaded_file)

        st.dataframe(df)

        st.subheader("Dataset Shape")

        st.write(df.shape)

# ---------------- PREDICTION ----------------
elif page == "Prediction":

    st.header("Electricity Demand Prediction")

    year = st.number_input(
        "Year",
        2020,
        2035,
        2026
    )

    month = st.slider(
        "Month",
        1,
        12,
        1
    )

    peak_met = st.number_input(
        "Peak Met",
        value=100000
    )

    energy_requirement = st.number_input(
        "Energy Requirement",
        value=150000
    )

    input_df = pd.DataFrame({
        "Year":[year],
        "Month":[month],
        "Peak Met":[peak_met],
        "Energy Requirement":[energy_requirement]
    })

    if st.button("Predict Demand"):

        prediction = model.predict(input_df)

        st.success(
            f"Predicted Peak Demand: {prediction[0]:,.2f}"
        )

# ---------------- FEATURE IMPORTANCE ----------------
elif page == "Feature Importance":

    st.header("Feature Importance")

    feature_names = [
        "Year",
        "Month",
        "Peak Met",
        "Energy Requirement"
    ]

    importance = model.feature_importances_

    fig, ax = plt.subplots(figsize=(8,5))

    ax.barh(
        feature_names,
        importance
    )

    ax.set_title(
        "Decision Tree Feature Importance"
    )

    st.pyplot(fig)