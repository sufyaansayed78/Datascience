from src.datascience.constants import * 
from src.datascience.utils.common import read_yaml, create_directories, save_json
from src.datascience.entity.config_entity import (DataIngestionConfig,DataValidationConfig,ModelEvaluationConfig)
from src.datascience.configs.configuration import ConfigurationManager
import os 
from src.datascience import logger
from sklearn.linear_model import ElasticNet
import joblib
from src.datascience.entity.config_entity import ModelTrainerConfig
import pandas as pd 
from src.datascience.utils.common import create_directories
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score
import mlflow
import dagshub 
import numpy as np 
dagshub.init(repo_owner='sufyaansayed78', repo_name='Datascience', mlflow=True)

print(os.getcwd())

class ModelEvaluation:
    def __init__(self,config : ModelEvaluationConfig):
        self.config = config 

    def eval_metrices(self,actual,pred):
        rmse = np.sqrt(mean_squared_error(actual,pred))
        mae = mean_absolute_error(actual,pred)
        r2 = r2_score(actual,pred)
        return rmse,mae,r2
    
    def log_into_mlflow(self):
        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)
        test_x = test_data.drop([self.config.target_column],axis =1)
        test_y = test_data[[self.config.target_column]]

        with mlflow.start_run():
          pred = model.predict(test_x)  
          rmse,mae,r2 = self.eval_metrices(test_y,pred=pred)
          scores = {"rmse": rmse,"mae":mae,"r2":r2}
          save_json(path=Path(self.config.metric_file_name),data=scores)
          mlflow.log_params(self.config.all_params)
          mlflow.log_metric("rmse",rmse)
          mlflow.log_metric("r2",r2)
          mlflow.log_metric("mae",mae)

        



        


