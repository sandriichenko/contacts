import json


def load_json():
    with open("contacts.json", "rt") as f:
        return json.load(f)


def save_json(phonebook):
    with open("contacts.json", "wt") as f:
        json.dump(phonebook, f)
