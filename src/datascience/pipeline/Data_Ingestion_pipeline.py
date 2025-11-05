from src.datascience.configs.configuration import ConfigurationManager
from src.datascience.components.data_ingestion import DataIngestion
from src.datascience import logger

class DataIngestionPipeLine:
        def __init__(self):
             pass

        def initiate_data_ingestion_config(self):
            config = ConfigurationManager()
            data_ingestion_config = config.get_data_ingestion_config()
            data_ingestion = DataIngestion(config=data_ingestion_config)
            data_ingestion.download_file()
            data_ingestion.extract_zip_file()


if __name__=="__main__":
      try:
            logger.info(f">>>>>>> DATA INGESTION STARTED")
            obj = DataIngestionPipeLine()
            obj.initiate_data_ingestion_config()
            logger.info(f"DATA INGETION COMPLETED")
      except Exception as e :
            raise e 
            
            