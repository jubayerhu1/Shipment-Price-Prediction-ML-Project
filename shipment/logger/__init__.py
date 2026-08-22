import logging
import os
from datetime   import datetime


## Create a unique log file name using the current date and time
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Build the full path where the log directory will be created inside the current working directory
log_path = os.path.join(os.getcwd(), 'log', LOG_FILE)

# Create the log directory (and any missing parent folders) if it doesn't already exist
os.makedirs(log_path, exist_ok= True)

# Create the log directory (and any missing parent folders) if it doesn't already exist
LOG_FILE_PATH = os.path.join(log_path, LOG_FILE)

logging.basicConfig(
    filename= LOG_FILE_PATH,
    format= "[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    level= logging.INFO

)

