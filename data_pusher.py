import os
import json
import certifi
import pandas as pd
import numpy as np
import pymongo

from dotenv import load_dotenv
import pymongo.mongo_client
load_dotenv()

MONGO_DB_URL = os.getenv('MONGO_DB_URL')
print(MONGO_DB_URL)

ca = certifi.where()

class NetworkDataExtract():
    def __init__(self):
        pass

    def csv_to_json(self, filepath):
        data_df = pd.read_csv(filepath)
        data_df.reset_index(drop = True, inplace = True)
        records_json = list(json.loads(data_df.T.to_json()).values())
        return records_json
    
    def insert_to_mongodb(self, records, database, collection):
        self.database = database
        self.collection = collection
        self.records = records

        self.mongo_client = pymongo.MongoClient(MONGO_DB_URL)

        self.database = self.mongo_client[self.database]
        self.collection = self.database[self.collection]

        self.collection.insert_many(self.records)


        return(len(self.records))
    
if __name__ == '__main__':
    FILE_PATH = r"E:\environments\SocialSecurityNetwork_project\src\network_data\phisingData.csv"
    DATABASE = "MAHIDB"
    Collection = "NetworkData"

    extract_obj = NetworkDataExtract()
    records = extract_obj.csv_to_json(FILE_PATH)
    no_of_records = extract_obj.insert_to_mongodb(records, DATABASE, Collection)
    print(no_of_records)

    
    
        
         




