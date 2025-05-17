import yaml
import dill
import os
import numpy as np
import pickle
import pandas as pd
import sys


def read_yaml_file(filepath: str) -> dict:
    with open(filepath) as fileobj:
        return yaml.safe_load(fileobj)
   
def read_data(filepath: str) -> pd.DataFrame:  
    return pd.read_csv(filepath)

def write_to_yaml(filepath: str, content: object, replace=False):

    if os.path.isdir(filepath):
        raise ValueError(f"Expected a file path, but got a directory: {filepath}")

    os.makedirs(os.path.dirname(filepath), exist_ok=True)

    if replace and os.path.exists(filepath):
        try:
            os.remove(filepath)
        except Exception as e:
            raise PermissionError(f"Could not remove existing file: {filepath} due to: {e}")

    try:
        with open(filepath, 'w') as file:
            yaml.safe_dump(content, file)
    except Exception as e:
        raise PermissionError(f"Failed to write to file: {filepath} due to: {e}")
    

def save_numpy_array_data(filepath: str, array: np.array):
    os.makedirs(os.path.dirname(filepath), exist_ok = True)
    with open(filepath, 'wb') as file:
        np.save(file, array) 


def save_object_pkl(filepath: str, obj: object):
    os.makedirs(os.path.dirname(filepath), exist_ok= True)
    with open(filepath, 'wb') as file:
        pickle.dump(obj, file)




