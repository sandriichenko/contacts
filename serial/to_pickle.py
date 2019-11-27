import pickle


def load_pickle():
    with open("contacts.pickle", "rb") as f:
        return pickle.load(f)


def save_pickle(phonebook):
    with open("contacts.pickle", "wb") as f:
        pickle.dump(phonebook, f)
