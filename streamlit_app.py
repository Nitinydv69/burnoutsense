import streamlit as st
import requests

API_URL = "https://burnoutsense-196034272039.europe-west1.run.app/predict"

st.set_page_config(
    page_title="BurnoutSense",
    page_icon="🧠",
    layout="centered"
)

st.title("🧠 BurnoutSense")
st.subheader("Student Mental Health Risk Predictor")

st.markdown(
    """
    Enter student lifestyle, academic, and mental health
    related details to estimate burnout/depression risk.
    """
)

with st.form("prediction_form"):

    gender = st.selectbox(
        "Gender",
        ["Male", "Female"]
    )

    age = st.slider(
        "Age",
        15,
        40,
        23
    )

    city = st.selectbox(
        "City",
        [
            "Mumbai",
            "Delhi",
            "Bangalore",
            "Chennai",
            "Pune"
        ]
    )

    profession = st.selectbox(
        "Profession",
        ["Student"]
    )

    academic_pressure = st.slider(
        "Academic Pressure",
        0,
        10,
        5
    )

    work_pressure = st.slider(
        "Work Pressure",
        0,
        10,
        2
    )

    cgpa = st.slider(
        "CGPA",
        0.0,
        10.0,
        6.4
    )

    study_satisfaction = st.slider(
        "Study Satisfaction",
        0,
        10,
        5
    )

    job_satisfaction = st.slider(
        "Job Satisfaction",
        0,
        10,
        4
    )

    sleep_duration = st.selectbox(
        "Sleep Duration",
        [
            "Less than 5 hours",
            "5-6 hours",
            "7-8 hours",
            "More than 8 hours"
        ]
    )

    dietary_habits = st.selectbox(
        "Dietary Habits",
        [
            "Healthy",
            "Moderate",
            "Unhealthy"
        ]
    )

    degree = st.selectbox(
        "Degree",
        [
            "BCA",
            "B.Tech",
            "BSc",
            "MCA"
        ]
    )

    suicidal_thoughts = st.selectbox(
        "Have you ever had suicidal thoughts?",
        ["No", "Yes"]
    )

    work_study_hours = st.slider(
        "Work / Study Hours",
        0,
        16,
        6
    )

    financial_stress = st.slider(
        "Financial Stress",
        0,
        10,
        5
    )

    family_history = st.selectbox(
        "Family History of Mental Illness",
        ["No", "Yes"]
    )

    submitted = st.form_submit_button(
        "Predict Risk"
    )

if submitted:

    payload = {
        "Gender": gender,
        "Age": age,
        "City": city,
        "Profession": profession,
        "Academic_Pressure": academic_pressure,
        "Work_Pressure": work_pressure,
        "CGPA": cgpa,
        "Study_Satisfaction": study_satisfaction,
        "Job_Satisfaction": job_satisfaction,
        "Sleep_Duration": sleep_duration,
        "Dietary_Habits": dietary_habits,
        "Degree": degree,
        "Have_you_ever_had_suicidal_thoughts": suicidal_thoughts,
        "Work_Study_Hours": work_study_hours,
        "Financial_Stress": financial_stress,
        "Family_History_of_Mental_Illness": family_history
    }

    with st.spinner("Analyzing mental health risk..."):

        try:

            response = requests.post(
                API_URL,
                json=payload,
                timeout=30
            )

            if response.status_code == 200:

                result = response.json()

                risk = result.get(
                    "mental_health_risk",
                    "Unknown"
                )

                confidence = result.get(
                    "confidence",
                    0
                )

                st.divider()

                if risk == "High Risk":
                    st.error(
                        f"⚠️ Burnout Risk: {risk}"
                    )
                else:
                    st.success(
                        f"✅ Burnout Risk: {risk}"
                    )

                st.metric(
                    label="Prediction Confidence",
                    value=f"{confidence}%"
                )

            else:

                st.error(
                    "Prediction failed. Please try again."
                )

        except Exception as e:

            st.error(
                f"Error: {str(e)}"
            )
