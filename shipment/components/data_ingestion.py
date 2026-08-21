import sys
import os
from shipment.logger import logging
from pandas import DataFrame
from sklearn.model_selection import train_test_split
from typing import Tuple
from shipment.exception import shippingException
from shipment.configuration.mongo_operations import MongoDBOperation
from shipment.entity.config_entity import DataIngestionConfig
from shipment.entity.artifacts_entity import DataIngestionArtifacts
from shipment.constants import TEST_SIZE


