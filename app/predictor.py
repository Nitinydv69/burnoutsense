import joblib
import pandas as pd


class BurnoutPredictor:

    def __init__(self, model_path):

        self.model = joblib.load(model_path)

        self.encoders = joblib.load(
            "encoders.pkl"
        )

        self.feature_columns = joblib.load(
            "feature_columns.pkl"
        )

    def predict(self, data_dict):

        df = pd.DataFrame([data_dict])

        # Encode categorical columns
        for column, encoder in self.encoders.items():

            if column in df.columns:

                df[column] = encoder.transform(
                    df[column]
                )

        # Ensure same feature order
        df = df[self.feature_columns]

        prediction = self.model.predict(df)[0]

        probabilities = self.model.predict_proba(
            df
        )[0]

        confidence = round(
            max(probabilities) * 100,
            2
        )

        risk_label = (
            "High Risk"
            if prediction == 1
            else "Low Risk"
        )

        return {
            "mental_health_risk": risk_label,
            "confidence": confidence
        }
