from src.mlproject.logging import logging
from src.mlproject.exception import CustomException
from src.mlproject.components.data_ingestion import DataIngestion
from src.mlproject.components.data_ingestion import DataIngestionConfig
import sys

if __name__=="__main__":
    logging.info("the execustion has started")
    
    try:
        data_ingestion=DataIngestion()
        data_ingestion.initiate_data_ingestion()
    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e,sys)