import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score


df = pd.read_csv("dataset.csv")

print("Dataset shape:", df.shape)

# Drop useless ID column
df = df.drop(columns=["id"])

# Drop missing values
df = df.dropna()

# ENCODE CATEGORICAL DATA


label_encoders = {}

for column in df.select_dtypes(include=["object"]).columns:

    le = LabelEncoder()

    df[column] = le.fit_transform(df[column])

    label_encoders[column] = le

# feature and target

target = "Depression"

X = df.drop(columns=[target])
y = df[target]


# -----------------------
# TRAIN TEST SPLIT
# -----------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


# -----------------------
# TRAIN MODEL
# -----------------------

model = RandomForestClassifier(
    n_estimators=300,
    max_depth=15,
    min_samples_split=5,
    random_state=42,
    n_jobs=-1
)

model.fit(X_train, y_train)


# -----------------------
# EVALUATE MODEL
# -----------------------

predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print("\nAccuracy:", accuracy)

print("\nClassification Report:")
print(classification_report(y_test, predictions))


# -----------------------
# FEATURE IMPORTANCE
# -----------------------

importance_df = pd.DataFrame({
    "feature": X.columns,
    "importance": model.feature_importances_
})

importance_df = importance_df.sort_values(
    by="importance",
    ascending=False
)

print("\nTop Features:")
print(importance_df.head(10))


# -----------------------
# SAVE MODEL
# -----------------------
# -----------------------

joblib.dump(model, "../app/model.pkl")

joblib.dump(
    label_encoders,
    "../app/encoders.pkl"
)

joblib.dump(
    list(X.columns),
    "../app/feature_columns.pkl"
)

print("\nModel + encoders saved successfully!")
