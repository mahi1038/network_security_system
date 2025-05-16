import pandas as pd
import numpy as np
import os
from datetime import datetime
import pymongo

# cofiguration of the ingestion 
from src.entity.config_entity import DataIngestionConfig
from src.entity.artifact_entity import DataIngestionArtifactConfig
import os
from sklearn.model_selection import train_test_split

from dotenv import load_dotenv
load_dotenv()

MONGO_DB_URL = os.getenv("MONGO_DB_URL")

class DataIngestion:
    def __init__(self, data_ingestion_config: DataIngestionConfig):
        self.data_ingestion_config = data_ingestion_config

    def export_collection_as_dataframe(self):
        database_name = self.data_ingestion_config.database_name
        collection_name = self.data_ingestion_config.collection_name

        self.mongo_client = pymongo.MongoClient(MONGO_DB_URL)
        collection = self.mongo_client[database_name][collection_name]
        df = pd.DataFrame(list(collection.find()))
        if "_id" in df.columns.to_list():
            df = df.drop(columns = ["_id"], axis = 1)

        df.replace({"na": np.nan}, inplace = True)
        return df
    
    def export_data_to_feature_store(self, dataframe):
        feature_store_file_path = self.data_ingestion_config.feature_store_file_path

        dir_path = os.path.dirname(feature_store_file_path)
        os.makedirs(dir_path, exist_ok = True)
        dataframe.to_csv(feature_store_file_path, index = False, header = True)
        return dataframe
    
    def train_test_split_data(self, Dataframe):
        train_set, test_set = train_test_split(Dataframe, test_size = self.data_ingestion_config.train_test_ratio)


        dir_path = os.path.dirname(self.data_ingestion_config.train_path)
        os.makedirs(dir_path, exist_ok = True)

        train_set.to_csv(self.data_ingestion_config.train_path, index = True, header = False)
        test_set.to_csv(self.data_ingestion_config.test_path, index = True, header = False)




    def initiate_data_ingestion(self):
        dataframe = self.export_collection_as_dataframe()
        dataframe = self.export_data_to_feature_store(dataframe)

        self.train_test_split_data(dataframe)

        data_ingestion_artifact_cofig = DataIngestionArtifactConfig(self.data_ingestion_config.train_path, self.data_ingestion_config.test_path)

        return data_ingestion_artifact_cofig


       
