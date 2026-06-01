import sys
from json import loads
from typing import Collection
from pandas import DataFrame
from pymongo.database import Database
import pandas as pd
from pymongo import MongoClient
from shipment.constants import DB_URL
from shipment.exception import shippingException
from shipment.logger import logging


class MongoDBOperation:

    def __init__(self):
        self.DB_URL = DB_URL
        self.client = MongoClient(self.DB_URL)

    def get_database(self, db_name) -> Database:
        '''
        Methon name : get_database
        Description : This method gets database from MongoDB from the db_name
        Output : A database is created in MongoDB with name as db_name 
        '''

        logging.info("Entered get_data_from_Mongodb method of Data_Ingesti on class")

        try:
            # Getting the DB
            db = self.client[db_name]

            logging.info(f"Created {db_name} database in MongoDB")
            logging.info("Exited get_database method MongoDB_opertation class")

            return db
            
          
        except Exception as e:
            raise shippingException(e, sys) from e


    def get_collection_as_dataframe(self, db_name, collection_name) -> DataFrame:

        '''
        Method name : get_collection_as_dataframe
        Description : This method is used for converting the selected collection to dataframe
        output : A collection is returned from the selected db_name and collection_name

        '''
        logging.info(
            "Entered get collection_as_dataframe method of MongoDB_operation class"
        )
        

        try:
            # Getting the database
            database = self.get_database(db_name)

            # Getting the collection name 
            collection = database.get_collection(name = collection_name)

            # Reading the dataframe and dropping the _id colum
            df = pd.DataFrame(list(collection.find()))
            if "_id" in df.columns.to_list():
                df = df.drop(columns=["_id"])
            
            logging.info("Covnerted collection to dataframe")
            logging.info(
            "Exited get_collection_as_dataframe method of mongoDB_Operation class")
            return df
        
        except Exception as e:
            raise shippingException(e, sys) from e
    


    
        