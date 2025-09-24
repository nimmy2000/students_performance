import os
from dataclasses import dataclass, field


DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")
EXTERNAL_DATA_PATH = os.path.join(DATA_DIR, "external_source", "exams.csv")
RAW_DATA_PATH = os.path.join(DATA_DIR, "raw_data", "data.csv")

class DataPreparationConfig:
    def __init__(self):
        # Input raw data
        self.raw_data_path = os.path.join(DATA_DIR, "raw_data", "data.csv")

        # Processed data path
        self.processed_data_path = os.path.join(DATA_DIR, "processed", "prepared_data.csv")

        # Folder to save preprocessing objects (scalers, encoders, etc.)
        self.preprocess_dir = os.path.join(DATA_DIR, "artifacts")
        os.makedirs(self.preprocess_dir, exist_ok=True)

        self.scaler_path = os.path.join(self.preprocess_dir, "scaler.pkl")
        self.encoder_path = os.path.join(self.preprocess_dir, "encoder.pkl")
@dataclass
class ModelTrainConfig:
    processed_data_path: str=field(default_factory=lambda: os.path.join(DATA_DIR, "processed", "prepared_data.csv"))
    model_dir: str = field(default_factory=lambda: os.path.join(DATA_DIR, "models"))
    model_path: str = field(default_factory=lambda: os.path.join(DATA_DIR, "models", "trained_model.pkl"))