from src.config import DataPreparationConfig
from src.components.data_preparation import DataPreparation


def run_data_preparation_pipeline():
    # Load config
    config = DataPreparationConfig()

    # Run preparation
    prep = DataPreparation(config)
    prep.prepare_data()


if __name__ == "__main__":
    run_data_preparation_pipeline()
