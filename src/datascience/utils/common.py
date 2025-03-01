import os
import yaml
from src.datascience import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
from box.exceptions import BoxValueError

@ensure_annotations
def read_yaml(path_to_yaml: Path)-> ConfigBox:
    """
    reads yaml file and returns

    Args:
    path_to_yaml(str): path like input

    Raises:
    value error: if yaml file is empty
    e: empty file

    Returns:
    ConfigBOX: configBox  type
    
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content=yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded succefully")
            return ConfigBox(content)
        
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """
    create list of directories

    Args:
        path to directories:list of path of directories
        ignore_log(bool,optional): ignore if multiple directories is to be created
    
    """
    for path in path_to_directories:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f"created directory at {path}")


@ensure_annotations
def save_json(path: Path, data: dict):
    """
    Args:
        path(Path):path to json file
        data(dict): data to be saved in json file
    
    """
    with open(path,"w") as f:
        json.dump(data, f, indent=4)

        logger.info(f"json file saved: {path}")


@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    with open(path) as f:
        content= json.load(f)

    logger.info(f"json file saved at {path}")
    return ConfigBox(content)


@ensure_annotations
def save_bin(data: Any, path: Path):
    """
    data(ANy): data to be saved as binary
    path(path): path to binary file


    """
    joblib.dump(value=data,filename=path)
    logger.info(f"binary file saved at: {path}")



@ensure_annotations
def load_bin(path: Path)-> Any:
    """
    load binary data
    path(path): path to binary file

    Returns:
            returns any object stored in the file


    """
    data=joblib.load(path)
    logger.info(f"binary file loaded from: {path}")
    return data