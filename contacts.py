from contacts_exist_model import create, read, update, delete

ACTIONS_MESSAGE = """c - create
r - read
u - update
d - delete
q - quit
"""

def create_contact():
    name = input("Name?")
    phone = input("Phone?")
    create(name, phone)

def read_contact():
    name = input("Name?")
    print(read(name))

def update_contact():
    name = input("Name?")
    phone = input("Phone?")
    update(name, phone)

def delete_contact():
    name = input("Name?")
    delete(name)

def default():
    print("Incorrect action")

ACTIONS = {
    "c": create_contact,
    "r": read_contact,
    "u": update_contact,
    "d": delete_contact,
}

while (action := input(ACTIONS_MESSAGE).lower()) != 'q':
    try:
        ACTIONS.get(action, default)()
    except KeyError as e:
        print(e)
