from src.components.data_ingestion import DataIngestion

class DataIngestionPipeline:
    """
    Pipeline to run the data ingestion component.
    """
    
    def __init__(self):
        self.ingestion = DataIngestion()

    def run_pipeline(self):
        """
        Runs the data ingestion step.
        """
        ingested_file_path = self.ingestion.ingest_data()
        print(f"Pipeline completed. Data saved at: {ingested_file_path}")
        return ingested_file_path


# Run pipeline if executed directly
if __name__ == "__main__":
    pipeline = DataIngestionPipeline()
    pipeline.run_pipeline()
