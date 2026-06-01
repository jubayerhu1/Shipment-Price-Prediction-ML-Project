import logging 
import os


LOG_DIR = "LogTest"    # folder name : log

LOG_FILE_NAME ="application.log"    # file name
#  folde make 
os.makedirs(LOG_DIR, exist_ok=True)

# path difine 
# manul approach
# path = "log/application.log"

# programing approach 
log_path = os.path.join(LOG_DIR,LOG_FILE_NAME)
print(log_path) 


# Configuration
logging.basicConfig(
    filename=log_path,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level= logging.INFO
)