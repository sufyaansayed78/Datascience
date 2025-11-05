from src.datascience import logger
from src.datascience.pipeline.Data_Ingestion_pipeline import DataIngestionPipeLine
from src.datascience.pipeline.data_validation_pipeline import DataValidationPipeline



try : 
    data_ing_pip = DataIngestionPipeLine()
    data_ing_pip.initiate_data_ingestion_config()
    logger.info("Data INGESTION COMPLETED")

except Exception as e:
    raise e 

try : 
    logger.info("Data Validation started")
    data_validation_pipeline = DataValidationPipeline()
    data_validation_pipeline.initiate_data_validation()
    logger.info("Data Validation complete")
except Exception as e :
    raise e 
