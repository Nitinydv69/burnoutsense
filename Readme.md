# 🧠 BurnoutSense

<div align="center">

### AI-Powered Student Burnout & Depression Risk Prediction System

Machine Learning + FastAPI + Streamlit + Google Cloud Platform

![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-API-green)
![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-red)
![Google Cloud](https://img.shields.io/badge/Google%20Cloud-Deployed-blue)
![ML](https://img.shields.io/badge/Machine%20Learning-ScikitLearn-orange)

</div>

---

## 📌 Overview

**BurnoutSense** is an AI-powered student mental health risk prediction system designed to estimate **burnout and depression risk** using academic, lifestyle, and mental-health-related indicators.

The system uses a **Machine Learning model** deployed through a **FastAPI backend** and served through an interactive **Streamlit frontend**, hosted on **Google Cloud Platform (GCP)**.

Users provide student-related information such as:

- Academic Pressure
- Sleep Duration
- CGPA
- Financial Stress
- Study Satisfaction
- Work/Study Hours
- Suicidal Thoughts
- Family Mental Health History

The system then predicts:

✅ **Mental Health Risk (Low / High)**  
✅ **Prediction Confidence (%)**

---

## 🚀 Live Deployment

### Frontend (Streamlit UI)

```text
http://35.242.134.99:8502
Backend API (FastAPI)
https://burnoutsense-196034272039.europe-west1.run.app
Swagger Documentation
https://burnoutsense-196034272039.europe-west1.run.app/docs
🏗️ System Architecture
                    ┌──────────────────────┐
                    │       User           │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Streamlit Frontend   │
                    │ (Compute Engine VM)  │
                    └──────────┬───────────┘
                               │ API Request
                               ▼
                    ┌──────────────────────┐
                    │ FastAPI Backend      │
                    │ (Google Cloud Run)   │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ ML Model (.pkl)      │
                    │ Scikit-Learn         │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Prediction Response  │
                    └──────────────────────┘
Frontend

Technology: Streamlit

Responsibilities:

User Interface
Input collection
API communication
Prediction visualization

Hosted on:

Google Compute Engine VM

Backend API

Technology: FastAPI

Responsibilities:

Handle API requests
Validate input data
Load trained ML model
Generate predictions
Return JSON response

Hosted on:

Google Cloud Run

Machine Learning Model

Technology: Scikit-Learn

The trained model is stored using .pkl serialization for efficient inference without retraining.

Files used:

model.pkl
encoders.pkl
feature_columns.pkl
📊 Dataset

Dataset used:

Student Depression Dataset (Kaggle)

The dataset includes student-related mental health and academic indicators.

Main features used in prediction:

Feature	Description
Academic Pressure	Academic stress level
Work Pressure	Work-related stress
CGPA	Academic performance
Sleep Duration	Sleep quality indicator
Dietary Habits	Healthy / Moderate / Unhealthy
Study Satisfaction	Satisfaction with studies
Job Satisfaction	Satisfaction with job/work
Financial Stress	Financial pressure
Suicidal Thoughts	Mental health risk indicator
Family History	Family history of mental illness
☁️ Google Cloud Deployment

The system is deployed using two Google Cloud services.

1. Compute Engine (Frontend Hosting)

Used to host the Streamlit application.

Configuration

Property	Value
VM Name	burnoutsense-vm
Machine Type	e2-micro
vCPU	2
Memory	1 GB
Region	europe-west2-a
OS	Debian 12

Purpose:

Persistent frontend hosting
Public web access
Streamlit deployment
2. Cloud Run (Backend API)

Used to deploy the FastAPI backend container.

Configuration

Property	Value
Service Name	burnoutsense
Region	europe-west1
Min Instances	0
Max Instances	1
Public Access	Enabled

Purpose:

Serverless deployment
Cost optimization
Automatic scaling

Benefits:

✅ Serverless architecture
✅ Near-zero idle cost
✅ Auto scaling
✅ Production-like deployment

💰 Estimated Monthly Cost
Service	Purpose	Estimated Monthly Cost
Compute Engine VM	Streamlit Frontend	€5–8/month
Cloud Run	FastAPI API	€0–2/month
Storage & Networking	Supporting resources	< €1/month
Estimated Total Cost
≈ €6–10/month

The infrastructure was intentionally optimized for low operational cost using:

Cloud Run serverless scaling
Minimum instances = 0
Lightweight VM configuration
⚙️ Installation & Setup
Clone Repository
git clone https://github.com/Nitinydv69/burnoutsense.git

cd burnoutsense
Install Dependencies

Using Poetry:

poetry install
Run FastAPI Backend
poetry run uvicorn app.main:app --reload

Runs locally at:

http://127.0.0.1:8000

Swagger docs:

http://127.0.0.1:8000/docs
Run Streamlit Frontend
poetry run streamlit run streamlit_app.py \
--server.address 0.0.0.0 \
--server.port 8502
🔬 Example Predictions
🟢 Low Risk Example

Prediction: Low Risk
Confidence: ~98%

Profile:

Academic Pressure: 0
Work Pressure: 0
CGPA: 9.2
Study Satisfaction: 10
Sleep Duration: More than 8 hours
Financial Stress: 0
Suicidal Thoughts: No
Family History: No
🔴 High Risk Example

Prediction: High Risk
Confidence: ~93%

Profile:

Academic Pressure: 9
Work Pressure: 6
CGPA: 4.8
Study Satisfaction: 1
Sleep Duration: Less than 5 hours
Financial Stress: 9
Suicidal Thoughts: Yes
Family History: Yes
🧪 API Example
Request
{
  "Gender": "Male",
  "Age": 22,
  "City": "Mumbai",
  "Profession": "Student",
  "Academic_Pressure": 9,
  "Work_Pressure": 6,
  "CGPA": 4.8,
  "Study_Satisfaction": 1,
  "Job_Satisfaction": 1,
  "Sleep_Duration": "Less than 5 hours",
  "Dietary_Habits": "Unhealthy",
  "Degree": "BCA",
  "Have_you_ever_had_suicidal_thoughts": "Yes",
  "Work_Study_Hours": 14,
  "Financial_Stress": 9,
  "Family_History_of_Mental_Illness": "Yes"
}
Response
{
  "mental_health_risk": "High Risk",
  "confidence": 93.55
}
🛠️ Challenges Solved

During deployment several engineering issues were encountered and resolved:

Docker Build Issues

Fixed containerization problems in the Dockerfile.

Cloud Run Port Issue

Configured application to correctly use Cloud Run expected ports.

Model Loading Errors

Resolved model path issues:

app/model.pkl
app/encoders.pkl
app/feature_columns.pkl
Import Errors

Corrected Python module imports:

from app.predictor import BurnoutPredictor
API Validation Errors (422)

Unified request payload format between Streamlit and FastAPI.

Streamlit ↔ FastAPI Integration

Ensured end-to-end communication between frontend and backend.

🔮 Future Improvements

Potential future upgrades include:

Improved model accuracy
Student wellness recommendations
University analytics dashboard
Real-time monitoring
Better UI/UX
Multi-class risk prediction
📌 Academic Disclaimer

This project was developed for educational and academic purposes only.

It is not a medical diagnosis tool and should not be used as a substitute for professional psychological or medical evaluation.

👨‍💻 Author

Nitin Yadav
University of Milan
Master’s of Data Science for Economics and Health

Project: BurnoutSense
