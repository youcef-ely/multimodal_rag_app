import yaml 
import base64
from IPython.display import Image, display



def load_config(config_file): 
    with open(config_file, 'r') as file: 
        config = yaml.safe_load(file) 
        return config


def display_base64_image(base64_code):
    image_data = base64.b64decode(base64_code)
    display(Image(data=image_data))