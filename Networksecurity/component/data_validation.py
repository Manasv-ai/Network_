from Networksecurity.entity.artifact_entity import DataIngestionArtifact, DataValidationArtifact
from Networksecurity.entity.config_entity import DataValidationConfig
from Networksecurity.exception.exception import NetworkSecurityException
from Networksecurity.constant.training_pipeline import SCHEMA_FILE_PATH
from Networksecurity.utils.main_utils.utils import read_yaml_file, write_yaml_file
from Networksecurity.logging.logger import logging
from scipy.stats import ks_2samp
import pandas as pd
import sys, os


class DataValidation:
    def __init__(self, data_ingestion_artifact: DataIngestionArtifact,
                 data_validation_config: DataValidationConfig):
        try:
            self.data_ingestion_artifact = data_ingestion_artifact
            self.data_validation_config = data_validation_config
            self._schema_config = read_yaml_file(SCHEMA_FILE_PATH)
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    @staticmethod
    def read_data(file_path) -> pd.DataFrame:
        try:
            return pd.read_csv(file_path)
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def validate_no_of_columns(self, dataframe: pd.DataFrame) -> bool:
        try:
            no_of_columns = len(self._schema_config["columns"])
            logging.info(f"Required no of columns: {no_of_columns}")
            logging.info(f"Dataframe has columns: {len(dataframe.columns)}")

            return len(dataframe.columns) == no_of_columns
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def detect_dataset_drift(self, base_df, current_df, threshold=0.05) -> bool:
        try:
            status = True
            report = {}
            for column in base_df.columns:
                d1 = base_df[column]
                d2 = current_df[column]
                is_sample_dist = ks_2samp(d1, d2)
                if threshold <= is_sample_dist.pvalue:
                    is_found = False
                else:
                    is_found = True
                    status = False

                report.update({
                    column: {
                        "p_value": float(is_sample_dist.pvalue),
                        "drift_status": is_found
                    }
                })

            drift_report_file_path = self.data_validation_config.drift_report_file_path
            dir_path = os.path.dirname(drift_report_file_path)
            os.makedirs(dir_path, exist_ok=True)
            write_yaml_file(file_path=drift_report_file_path, content=report)

            return status
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def initiate_data_validation(self) -> DataValidationArtifact:
        try:
            train_file_path = self.data_ingestion_artifact.trained_file_path
            test_file_path = self.data_ingestion_artifact.test_file_path

            train_dataframe = self.read_data(train_file_path)
            test_dataframe = self.read_data(test_file_path)

            # Validate columns
            if not self.validate_no_of_columns(train_dataframe):
                raise NetworkSecurityException("Train data missing columns", sys)

            if not self.validate_no_of_columns(test_dataframe):
                raise NetworkSecurityException("Test data missing columns", sys)

            # Detect drift
            status = self.detect_dataset_drift(train_dataframe, test_dataframe)

            os.makedirs(os.path.dirname(self.data_validation_config.valid_train_file_path), exist_ok=True)
            train_dataframe.to_csv(self.data_validation_config.valid_train_file_path, index=False)
            test_dataframe.to_csv(self.data_validation_config.valid_test_file_path, index=False)

            data_validation_artifact = DataValidationArtifact(
                validation_status=status,
                valid_train_file_path=self.data_validation_config.valid_train_file_path,
                valid_test_file_path=self.data_validation_config.valid_test_file_path,
                invalid_train_file_path=None,
                invalid_test_file_path=None,
                drift_report_file_path=self.data_validation_config.drift_report_file_path,
            )
            return data_validation_artifact

        except Exception as e:
            raise NetworkSecurityException(e, sys)
