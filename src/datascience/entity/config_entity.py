from dataclasses import dataclass
import os 
from pathlib import Path

@dataclass
class DataIngestionConfig:
    root_dir : Path 
    source_URL : str 
    local_data_file : Path
    unzip_dir : Path
    