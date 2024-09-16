import os
import sys
from pandas import DataFrame
from sklearn.model_selection import train_test_split

from us_visa.entity.config_entity import DataIngestionConfig
from us_visa.entity.artifact_entity import DataIngestionArtifact
from us_visa.exception import USvisaException
from us_visa.logger import logging
from us_visa.data_access.usvisa_data import USVisaData


class DataIngestion:
    def __init__(self, data_ingetion_config:DataIngestionConfig=DataIngestionConfig()):

        try:
            self.data_ingestion_config = data_ingetion_config
        except Exception as e:
            raise USvisaException(e, sys)

    def export_data_into_feature_store(self)->DataFrame:

        try:
            logging.info(f"Exporting data from MongoDB into feature store")
            usvisa_data = USVisaData()
            dataframe = usvisa_data.export_collection_as_dataframe(
                collection_name=self.data_ingestion_config.collection_name
            )
            logging.info(f"shape of dataframe: {dataframe.shape}")

            feature_store_file_path = self.data_ingestion_config.feature_store_file_path
            dir_path = os.path.dirname(feature_store_file_path)
            os.makedirs(dir_path, exist_ok=True)
            logging.info(f"Saving Exported Data into feature store file path: {feature_store_file_path}")
            dataframe.to_csv(feature_store_file_path, index=False, header=True)
            return dataframe
        
        except Exception as e:
            raise USvisaException(e, sys)

    def split_data_as_train_test(self, dataframe: DataFrame) -> None:
        logging.info("Entered split_data_as_train_test method of Data_Ingestion class")
        try:
            # Check if the dataframe is empty
            if dataframe.empty:
                raise ValueError("The dataframe is empty. Please check the data source.")

            train_set, test_set = train_test_split(dataframe, test_size=self.data_ingestion_config.train_test_split_ratio)
            logging.info("Performed train test split on the dataframe")
            logging.info("Exited split_data_as_train_test method of Data_Ingestion class")
            dir_path = os.path.dirname(self.data_ingestion_config.training_file_path)
            os.makedirs(dir_path, exist_ok=True)
            
            logging.info("Exporting train and test data file path.")
            train_set.to_csv(self.data_ingestion_config.training_file_path, index=False, header=True)
            test_set.to_csv(self.data_ingestion_config.testing_file_path, index=False, header=True)
            logging.info("Exported train and test data files path")
        except Exception as e:
            raise USvisaException(e, sys) from e
        
    def initiate_data_ingestion(self) -> DataIngestionArtifact:
        logging.info("Entered initiate_data_ingestion method of Data_Ingestion class")

        try:
            dataframe = self.export_data_into_feature_store()
            logging.info("Got the data from from MongoDB")
            self.split_data_as_train_test(dataframe)
            logging.info("Performed the train and test split operation on the dataset.")
            logging.info("Exited initiate_data_ingestion method of Data_Ingestion class")
            
            data_ingestion_artifact = DataIngestionArtifact(
                trained_file_path=self.data_ingestion_config.training_file_path,
                test_file_path=self.data_ingestion_config.testing_file_path)
            logging.info(f"Data Ingestion artifact: {data_ingestion_artifact}")
            return data_ingestion_artifact
        except Exception as e:
            raise USvisaException(e, sys) from e

            

        
