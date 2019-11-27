from config import load, save

try:
    phonebook = load()
except FileNotFoundError:
    phonebook = {}


def _contact_exists(message, g):
    def decorator(f):
        def wrapper(name, *args):
            if g(name not in phonebook):
                raise KeyError(message)
            return f(name, *args)
        return wrapper
    return decorator


contact_exists = _contact_exists("Contact doesn't exist", lambda x: x)
contact_not_exists = _contact_exists("Contact already exists", lambda x: not x)

@contact_not_exists
def create(name, phone):
    phonebook[name] = phone
    save(phonebook)

@contact_exists
def read(name):
    return phonebook[name]

@contact_exists
def update(name, phone):
    phonebook[name] = phone
    save(phonebook)

@contact_exists
def delete(name):
    del phonebook[name]
    save(phonebook)
