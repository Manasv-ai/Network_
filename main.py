from Networksecurity.component.data_ingestion import DataIngestion
from Networksecurity.exception.exception import NetworkSecurityException
from Networksecurity.component.data_transformation import DataTransformation
from Networksecurity.component.data_validation import DataValidation
from Networksecurity.logging.logger import logging
from Networksecurity.entity.config_entity import DataIngestionConfig,DataValidationConfig,DataTransformationConfig
from Networksecurity.entity.config_entity import TrainingPipelineConfig
import sys



if __name__=='__main__':
    try:
        trainingpipelineconfig=TrainingPipelineConfig()
        dataingestionconfig=DataIngestionConfig(trainingpipelineconfig)
        data_ingestion=DataIngestion(dataingestionconfig)
        logging.info("Initiate the data ingestion")

        dataingestionartifact=data_ingestion.initiate_data_ingestion()
        print(dataingestionartifact)
        logging.info("Data initiation completed")
        data_validation_config=DataValidationConfig(trainingpipelineconfig)
        data_validation=DataValidation(dataingestionartifact,data_validation_config)
        logging.info("Initiate the data validation")
        data_validation_artifact=data_validation.initiate_data_validation()
        print(data_validation_artifact)

        data_transformation_config=DataTransformationConfig(trainingpipelineconfig)
        data_transformation=DataTransformation(data_validation_artifact,data_transformation_config)
        data_transformation_artifact=data_transformation.initiate_data_transformation()
        print(data_transformation_artifact)

    except Exception as e:
        raise NetworkSecurityException(e,sys)  
