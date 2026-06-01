import os
from os import environ
from datetime import datetime
from dotenv import load_dotenv



load_dotenv()
# current time 
TIMESTAMP: str = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")
ARTIFACTS_DIR = os.path.join(os.getcwd(), "artifacts", TIMESTAMP)


MODEL_CONFIG_FILE = "config/model.yaml"
SCHEMA_FILE_PATH = "config/schema.yaml"

DB_URL = environ["MONGO_DB_URL"]




