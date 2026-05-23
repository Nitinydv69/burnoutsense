from fastapi import FastAPI
from pydantic import BaseModel
from predictor import BurnoutPredictor

app = FastAPI()

predictor = BurnoutPredictor("model.pkl")


class StudentInput(BaseModel):
    Gender: str
    Age: float
    City: str
    Profession: str
    Academic_Pressure: float
    Work_Pressure: float
    CGPA: float
    Study_Satisfaction: float
    Job_Satisfaction: float
    Sleep_Duration: str
    Dietary_Habits: str
    Degree: str
    Have_you_ever_had_suicidal_thoughts: str
    Work_Study_Hours: float
    Financial_Stress: float
    Family_History_of_Mental_Illness: str


@app.get("/")
def home():
    return {
        "message": "BurnoutSense API running"
    }


@app.post("/predict")
def predict(data: StudentInput):

    formatted_data = {
        "Gender": data.Gender,
        "Age": data.Age,
        "City": data.City,
        "Profession": data.Profession,
        "Academic Pressure": data.Academic_Pressure,
        "Work Pressure": data.Work_Pressure,
        "CGPA": data.CGPA,
        "Study Satisfaction": data.Study_Satisfaction,
        "Job Satisfaction": data.Job_Satisfaction,
        "Sleep Duration": data.Sleep_Duration,
        "Dietary Habits": data.Dietary_Habits,
        "Degree": data.Degree,
        "Have you ever had suicidal thoughts ?":
            data.Have_you_ever_had_suicidal_thoughts,
        "Work/Study Hours": data.Work_Study_Hours,
        "Financial Stress": data.Financial_Stress,
        "Family History of Mental Illness":
            data.Family_History_of_Mental_Illness
    }

    result = predictor.predict(
        formatted_data
    )

    return result
