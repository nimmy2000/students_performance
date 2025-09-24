from flask import Flask, render_template, request
from src.config import DataPreparationConfig, ModelTrainConfig
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)

en=DataPreparationConfig()
mt=ModelTrainConfig()
# Load encoder and trained model
with open( en.encoder_path,"rb") as f:
    encoder = pickle.load(f)

with open(mt.model_path, "rb") as f:
    model = pickle.load(f)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    if request.method == "POST":
        # Collect form data
        gender = request.form["gender"]
        race = request.form["race"]
        parental = request.form["parental"]
        lunch = request.form["lunch"]
        test_prep = request.form["test_prep"]

        # Convert to DataFrame for preprocessing
        input_df = pd.DataFrame([{
            "gender": gender,
            "race/ethnicity": race,
            "parental level of education": parental,
            "lunch": lunch,
            "test preparation course": test_prep
        }])

        # Encode categorical features
        encoded_input = encoder.transform(input_df)

        # Predict using trained model
        prediction = model.predict(encoded_input)[0]

        return render_template("result.html", prediction=round(prediction, 2))


if __name__ == "__main__":
    app.run(debug=True)
