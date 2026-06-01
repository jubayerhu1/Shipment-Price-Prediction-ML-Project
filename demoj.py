from shipment.constants import DB_URL

print(DB_URL)
print("Connection successfull !")

"""
for data checking : 
from shipment.configuration.mongo_operations import MongoDBOperation





obj = MongoDBOperation()
df = obj.get_collection_as_dataframe(db_name="ShipmentDB", collection_name = "shipment_collection")
print(df.head())
print(df.shape)"""