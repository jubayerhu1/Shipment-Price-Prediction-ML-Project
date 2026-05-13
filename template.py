# This script automatically creates the complete project folder structure
# and empty files for the "shipment" machine learning project.

# Importing required modules
import os
from pathlib import Path

# Defining the main project/package name
project_name = "shipment"

# List of all files and directories to create
list_of_files = [

    # Main package initialization
    f"{project_name}/__init__.py",

    # Components module
    f"{project_name}/components/__init__.py",
    f"{project_name}/components/data_ingestion.py",  
    f"{project_name}/components/data_validation.py",
    f"{project_name}/components/data_transformation.py",
    f"{project_name}/components/model_trainer.py",
    f"{project_name}/components/model_evaluation.py",
    f"{project_name}/components/model_pusher.py",

    # Configuration module
    f"{project_name}/configuration/__init__.py",

    # Constants module
    f"{project_name}/constants/__init__.py",

    # Entity module
    f"{project_name}/entity/__init__.py",
    f"{project_name}/entity/config_entity.py",
    f"{project_name}/entity/artifact_entity.py",

    # Exception handling module
    f"{project_name}/exception/__init__.py",

    # Logger module
    f"{project_name}/logger/__init__.py",

    # Pipeline module
    f"{project_name}/pipline/__init__.py",
    f"{project_name}/pipline/training_pipeline.py",
    f"{project_name}/pipline/prediction_pipeline.py",

    # Utility functions module
    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/main_utils.py",

    # Root-level project files
    "app.py",
    "requirements.txt",
    "Dockerfile",
    ".dockerignore",
    "demo.py",
    "setup.py",

    # Configuration files
    "config/model.yaml",
    "config/schema.yaml",

    # Test files | if need you can add any folder 
   # "test/test.py"
]

# Loop through every file path in the list
for filepath in list_of_files:

    # Convert string path into Path object
    filepath = Path(filepath)

    # Split directory path and filename
    filedir, filename = os.path.split(filepath)

    # Create directory if it does not already exist
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)

    # Create empty file if file doesn't exist
    # or if file exists but is empty
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):

        # Open file in write mode to create it
        with open(filepath, "w") as f:
            pass

    else:
        # Print message if file already exists
        print(f"file is already present at: {filepath}")