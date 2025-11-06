from src.datascience import logger
from sklearn.model_selection import train_test_split
from src.datascience.entity.config_entity import DataTransformationConfig
import os 
import pandas as pd



class DataTransformation:
    def __init__(self,config : DataTransformationConfig):
        self.config = config
    
    def train_test_splitting(self):
        data_path = pd.read_csv(self.config.data_path)
        train,test = train_test_split(data_path)
        train.to_csv(os.path.join(self.config.root_dir,"train.csv"),index = False)
        test.to_csv(os.path.join(self.config.root_dir,"test.csv"),index = False)
        logger.info("Splitted data into train and test")
        