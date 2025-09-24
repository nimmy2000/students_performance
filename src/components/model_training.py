from src.config import ModelTrainConfig
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle
import pandas as pd
class ModelTrainingClass:
    def __init__(self,config=ModelTrainConfig()):
        self.processed =config.processed_data_path
        self.modelpath=config.model_path
    def train(self):
        df=pd.read_csv(self.processed)
        X = df.drop(columns=["average_score"])
        y = df["average_score"]
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        model=LinearRegression()
        model.fit(X,y)
        with open (self.modelpath,"wb") as f:
            pickle.dump(model,f)


