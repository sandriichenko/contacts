import configparser

from serial.to_json import load_json, save_json
from serial.to_pickle import load_pickle, save_pickle

config = configparser.ConfigParser()
config.read("phonebook.ini")

if config["Serializer"]["format"] == 'json':
    load, save = load_json, save_json
elif config["Serializer"]["format"] == 'pickle':
    load, save = load_pickle, save_pickle
else:
    raise ImportError("Incorrect format")
