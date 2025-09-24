import shutil
import os
from src.config import EXTERNAL_DATA_PATH, RAW_DATA_PATH

class DataIngestion:
    """
    Component to perform data ingestion:
    Copies CSV from external source to raw_data folder.
    """
    
    def __init__(self, source_path=EXTERNAL_DATA_PATH, dest_path=RAW_DATA_PATH):
        self.source_path = source_path
        self.dest_path = dest_path

    def ingest_data(self):
        """
        Copies the file from source to destination.
        Creates destination folder if it does not exist.
        """
        # Ensure destination folder exists
        dest_folder = os.path.dirname(self.dest_path)
        os.makedirs(dest_folder, exist_ok=True)
        
        # Copy file
        shutil.copy2(self.source_path, self.dest_path)
        print(f"Data ingested successfully: {self.dest_path}")
        return self.dest_path
