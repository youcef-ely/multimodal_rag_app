import yaml 
import pickle
import base64
from IPython.display import Image, display



def load_config(config_file): 
    with open(config_file, 'r') as file: 
        config = yaml.safe_load(file) 
        return config


def display_base64_image(base64_code):
    image_data = base64.b64decode(base64_code)
    display(Image(data=image_data))


def load_from_pickle(filename):
    with open(filename, "rb") as file:
        return pickle.load(file)

def save_to_pickle(obj, filename):
    with open(filename, "wb") as file:
        pickle.dump(obj, file, pickle.HIGHEST_PROTOCOL)