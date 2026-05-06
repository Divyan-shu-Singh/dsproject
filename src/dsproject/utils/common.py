import os
import yaml
from src.dsproject import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
from box.exceptions import BoxValueError

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads a YAML file and returns its contents as a ConfigBox object.

    Args:
        path_to_yaml (Path): The path to the YAML file.
    Returns:
        ConfigBox: The contents of the YAML file as a ConfigBox object.
    """
    try:
        logger.info(f"Reading YAML file from: {path_to_yaml}")
        with open(path_to_yaml, 'r') as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"Successfully read YAML file: {path_to_yaml}")
            return ConfigBox(content)
    except BoxValueError as e:
        raise ValueError("yaml file is empty")
    except Exception as e:
        logger.error(f"Error reading YAML file: {e}")
        raise e
    
@ensure_annotations
def create_directories(path_to_directories: list, verbose: bool = True):
    """
    Creates directories if they do not exist.

    Args:
        path_to_directories (list): A list of paths to the directories to be created.
        verbose (bool): Whether to log the creation of each directory.
    """
    for path in path_to_directories:
        try:
            logger.info(f"Creating directory at: {path}")
            os.makedirs(path, exist_ok=True)
            if verbose:
                logger.info(f"Successfully created directory: {path}")
        except Exception as e:
            logger.error(f"Error creating directory: {e}")
            raise e


@ensure_annotations
def save_json(path: Path, data: dict):
    """
    Saves data to a JSON file.

    Args:
        path (Path): The path to the JSON file.
        data (Any): The data to be saved to the JSON file.
    """
    try:
        logger.info(f"Saving data to JSON file at: {path}")
        with open(path, 'w') as json_file:
            json.dump(data, json_file, indent=4)
            logger.info(f"Successfully saved data to JSON file: {path}")
    except Exception as e:
        logger.error(f"Error saving data to JSON file: {e}")
        raise e

@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """
    Loads data from a JSON file.

    Args:
        path (Path): The path to the JSON file.
    Returns:
        ConfigBox: The contents of the JSON file as a ConfigBox object.
    """
    try:
        logger.info(f"Loading data from JSON file at: {path}")
        with open(path, 'r') as json_file:
            data = json.load(json_file)
            logger.info(f"Successfully loaded data from JSON file: {path}")
            return ConfigBox(data)
    except Exception as e:
        logger.error(f"Error loading data from JSON file: {e}")
        raise e
    
@ensure_annotations
def save_bin(data: Any, path: Path):
    """
    Saves data to a binary file using joblib.

    Args:
        data (Any): The data to be saved.
        path (Path): The path to the binary file.
    """
    try:
        logger.info(f"Saving data to binary file at: {path}")
        joblib.dump(data, path)
        logger.info(f"Successfully saved data to binary file: {path}")
    except Exception as e:
        logger.error(f"Error saving data to binary file: {e}")
        raise e
    
@ensure_annotations
def load_bin(path: Path) -> Any:
    """
    Loads data from a binary file using joblib.

    Args:
        path (Path): The path to the binary file.
    Returns:
        Any: The loaded data.
    """
    try:
        logger.info(f"Loading data from binary file at: {path}")
        data = joblib.load(path)
        logger.info(f"Successfully loaded data from binary file: {path}")
        return data
    except Exception as e:
        logger.error(f"Error loading data from binary file: {e}")
        raise e
    
