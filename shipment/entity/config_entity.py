import os
#class MainUtils:
from shipment.utils.main_utils import MainUtils
from shipment.constants import *
from dataclasses import dataclass


@dataclass
class DataIngestionCongfig:

    def __init__(self):
        self.UTILS = MainUtils()
        self.SCHEMA_CONFIG = self.UTILS.read_yaml_file(filename=SCHEMA_FILE_PATH)
        pass