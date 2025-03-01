from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataIngestionConfig:
    root_dir: Path          # root_dir: Directory where all data-related files are stored.
    source_URL: Path        # source_URL: URL to download the data from.
    local_data_file: Path   # local_data_file: Path where the downloaded file will be stored.
    unzip_dir: Path         # unzip_dir: Directory where the extracted files will be placed.
@dataclass
class DataValidationConfig:
    root_dir:Path
    STATUS_FILE:str
    unzip_data_dir:Path
    all_schema:dict

@dataclass
class DataTransformationConfig:
    root_dir: Path
    data_path: Path