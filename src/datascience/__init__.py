import os 
import sys
import logging 
from datetime import datetime
log_str = "[%(asctime)s: %(levelname)s: %(module)s:%(message)s]"
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
log_dir ="logs"
log_filepath = os.path.join(log_dir,f"Log At {timestamp}.log")
os.makedirs(log_filepath,exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=log_str,

    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]

)
logger = logging.getLogger("datasciencelogger")







