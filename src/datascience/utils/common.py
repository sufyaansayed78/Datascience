import os 
import yaml
from src.datascience import logger
import json 
import joblib 
from ensure import ensure_annotations
from box import ConfigBox
from typing import Any 
from pathlib import Path
from box.exceptions import BoxValueError

def read_yaml(yamlfilepath : str) -> ConfigBox:


    try:
        with open(yamlfilepath,'r') as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file :{yamlfilepath}loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e : 
        raise e

@ensure_annotations
def create_directories(path_to_directories : list , verbose = True ):
    for dir in path_to_directories:
        os.makedirs(dir,exist_ok=True)
        if verbose:
            logger.info(f"Created direcotry at {dir}")
@ensure_annotations
def save_json(path : Path,data : dict):
    with open(path,'w') as file :
        json.dump(data,file,indent=4)
    logger.info(f"json file saved at : {path}")

@ensure_annotations
def load_json(path : Path) -> ConfigBox:
    with open(path) as file:
        content = json.load(file)
    logger.info(f"Json file loaded successfully from : {path}")
    return ConfigBox(content)

def save_bin(path : Path,data: Any):
    joblib.dump(value = data, filename=path)
    logger.info(f"binary file saved at : {path}")

def load_bin(path : Path):
    data=joblib.load(path)
    return data


