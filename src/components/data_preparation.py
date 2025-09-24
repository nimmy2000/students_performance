import pandas as pd
import pickle
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from src.config import DataPreparationConfig

class DataPreparation:
    def __init__(self, config: DataPreparationConfig):
        self.config = config

    def prepare_data(self):
        # Load raw dataset
        df = pd.read_csv(self.config.raw_data_path)

        # 1️⃣ Calculate average_score
        score_cols = ["math score", "reading score", "writing score"]
        df["average_score"] = df[score_cols].mean(axis=1)

        # 2️⃣ Drop original score columns
        df.drop(columns=score_cols, inplace=True)

        # 3️⃣ Define categorical columns
        categorical_cols = ["gender", "race/ethnicity", "parental level of education", "lunch", "test preparation course"]

        # 4️⃣ OneHotEncoder for categorical columns
        categorical_transformer = OneHotEncoder(handle_unknown="ignore", sparse_output=False)

        # 5️⃣ ColumnTransformer for categorical columns, leave average_score as is
        preprocessor = ColumnTransformer(
            transformers=[
                ("cat", categorical_transformer, categorical_cols)
            ],
            remainder="passthrough"  # keeps average_score
        )

        # 6️⃣ Build pipeline
        pipeline = Pipeline(steps=[("preprocessor", preprocessor)])

        # 7️⃣ Fit and transform
        transformed_data = pipeline.fit_transform(df)

        # 8️⃣ Get fitted encoder from pipeline
        fitted_encoder = pipeline.named_steps['preprocessor'].named_transformers_['cat']

        # 9️⃣ Save the fitted encoder for later use
        with open(self.config.encoder_path, "wb") as f:
            pickle.dump(fitted_encoder, f)

        # 10️⃣ Get proper column names
        encoded_cols = fitted_encoder.get_feature_names_out(categorical_cols)
        all_cols = list(encoded_cols) + ["average_score"]

        # 11️⃣ Create processed dataframe
        processed_df = pd.DataFrame(transformed_data, columns=all_cols)

        # 12️⃣ Save processed CSV
        processed_df.to_csv(self.config.processed_data_path, index=False)

        print(f"✅ Data preparation complete. Saved at {self.config.processed_data_path}")
