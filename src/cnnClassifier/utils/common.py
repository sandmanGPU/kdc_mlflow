import os

import joblib
from box.exceptions import BoxValueError
import yaml
from src.cnnClassifier import logger
import json
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """reads yaml file and returns

    Args:
        path_to_yaml (str): Path like input

    Raises:
        ValueError: if yaml file is empty, i.e. contains no content
        e: empty file

    Returns:
        ConfigBox: ConfigBox type
    """

    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        
        raise ValueError(f"yaml file is empty @ {path_to_yaml}")
    except Exception as e:
        raise e


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """create list of directories
    Args:
        path_to_directories (list): list containing the paths of drectories to create
        ignore_log (bool, optional): ignore if multiple dirs to be created. Default is False
    """

    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")


@ensure_annotations
def save_json(path: Path, data: dict):
    """save json data
    Args:
        path(Path): path to json file
        data(dict): data to be saved in json file

    """
    with open(path, "a") as f:
        json.dump(data, f, indent=4)

    logger.info(f"json file saved at: {path}")


@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """load json files data and return
    Args:
        path(Path): path to json file
    Returns:
        ConfigBox: data as class attribute instead of dict
    """
    with open(path) as f:
        content = json.load(f)
    logger.info(f"json file loaded successfully from: {path}")
    return ConfigBox(content)


@ensure_annotations
def save_bin(data: Any, path: Path):
    """save binary file
    Args:
        data(Any): data to be saved as binary
        path(Path): path to binary file
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"binary file save at: {path}")


@ensure_annotations
def load_bin(path: Path) -> Any:
    """load binary data

        Args:
            path (Path): path to binary file

        Returns:
            Any: object stored in the file
    """
    data = joblib(path)
    logger.info(f"binary file read from: {path}")
    return data


@ensure_annotations
def get_size(path: Path) -> str:
    """get size in KB

    Args:
        path (Path): path of the file

    Returns:
        str: size in KB
    """
    size_in_kB = round(os.path.getsize(path) / 1024)
    return f"~{size_in_kB}kB"


def decodeImage(imgstring, filename):
    imgdata = base64.b64decode(imgstring)
    with open(filename, 'wb') as f:
        f.write(imgdata)
        f.close()


def encodeImageIntoBase64(croppedImagePath):
    with(croppedImagePath, 'rb') as f:
        return base64.b64decode(f.read())
