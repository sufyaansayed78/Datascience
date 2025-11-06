from src.datascience.configs.configuration import ConfigurationManager
from src.datascience.components.data_transformation import DataTransformation
from src.datascience import logger 



class DataTransformationPipeline:
   def __init__(self):
     pass

   def initiate_data_transformation(self):
     try : 
        with open("artifacts\data_validation\status.txt",'r') as file :
           status = file.read().split(" ")[-1]
           if status == True : 
              config = ConfigurationManager()
              data_transformation_config = config.get_data_transformation_config()
              data_transformation = DataTransformation()
              data_transformation.train_test_splitting()
              logger.info('Data Transformation Complete')
           else:
              raise Exception(" Your data schema is not valid ")
     except Exception as e :
        print(e)