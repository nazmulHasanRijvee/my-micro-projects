import json  # imports json to use json file.

import os  # imports os to track the file.

from typing import TextIO  # file should be an object that supports .read() and .write()

# used for better clarity.

# Designing the program a bit. String is printed after 15 spaces.
print(f"{'Phone Book':>{15}}")

print(20 * "=")

# Assigning the file name to a variable to use it.
FILE_NAME = "contacts.json"

""" Checks if the file exists, if it doesn't return empty dictionary. If it does than read
 the file and loads it as a useful object like dictionary. Added error handling if
 files contain invalid json contents. """


def load_contact():
    if not os.path.exists(FILE_NAME):
        print(f"❌ File '{FILE_NAME}' not found.")
        return {}

    try:
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        print(f"⚠️ File '{FILE_NAME}' contains invalid JSON.")
        return {}


""" Creates the file if it doesn't exist or overwrites it. Converts the dictionary into
 json format and writes to the file with 4 spaces for each level of indentation to
 make it look clean. TextIO is a comment type hint. """


def save(contacts_data):

    with open(FILE_NAME, "w") as f:  # type: TextIO
        json.dump(contacts_data, f, indent=4)


# Loads the dictionary with data from the file.
contacts = load_contact()


# To show the menu of operations.
def menu():

    print("\nEnter the operation you want to perform:-")

    print(42 * "_")

    print("1. Add a contact.")

    print("2. View contacts.")

    print("3. Search contacts")

    print("4. Update a contact.")

    print("5. Delete a contact")

    print("6. Exit the program.")


# Adding the values in the nested dictionary and saving it in the json file.
def add():

    # contacts = load_contact()

    name = input("\n🙂Enter the contacts name :- ").title()

    phone = input("\n☎️Enter the phone number :- ")

    email = input("\n📧Enter the email :- ").lower()

    contacts[name] = {"phone": phone, "email": email}

    save(contacts)

    print("\nContact has been added successfully. ✅")


# To view the dictionary and also checks if the contact exist or not.
def view():

    # contacts = load_contact()

    if not contacts:
        print("\nThere is no contact available. ❌")

    else:
        for name, info in contacts.items():
            print("\nName: ", name)

            print("Phone :", info["phone"])

            print("Email :", info["email"])

            print(28 * "-")


# Search the contact by its name to find it.
def search():

    name = input("\n🙂Enter tha name of the contact :- ").title()

    if name in contacts:
        info = contacts[name]

        print(f"\n🔍Found the contact for {name}")

        print(f"\n☎️Phone : {info['phone']}")

        print(f"\n📧Email : {info['email']}")
    else:
        print("\nThe contact can't be found. ❌")


# Updates the contact if it exits.
def update():

    name = input("\n🙂Enter the name of the contact to update :- ").title()

    if name in contacts:
        updating = input("\n🪪Enter the field(phone, email) to update :- ").lower()

        updating_info = input("\n🗃️Enter the info to update :- ").lower()

        update2(name, updating, updating_info)

    else:
        print("\nThe contact can't be found. ❌")


""" Supports update method to find out which info to update and if that info field exists or not
 and saves the file in json. """


def update2(name, updating, updating_info):

    if updating in ("phone", "email"):
        contacts[name].update({updating: updating_info})

        save(contacts)

        print("\nThe contact has been updated successfully. ✅")

    else:
        print("\nThe field doesn't exist. ❌ ")


# Deletes the contact if it exists and saves the file in json.
def delete():
    name = input("\n🙂Enter the name of the contact to delete :- ")

    if name in contacts:
        del contacts[name]

        save(contacts)

    else:
        print("\nThe contact can't be found. ❌")


# Main code where all these methods are used.
while True:
    menu()

    # Error handling if wrong data type is given as input for example strings instead of int.
    try:
        operation = int(input("\n😀Enter the operation you want to perform :- "))

    except ValueError:
        print(f"\nOops invalid input please enter a number between 1-6. \n{20 * '🙄'}")
        continue

    if operation == 1:
        add()

    elif operation == 2:
        view()

    elif operation == 3:
        search()

    elif operation == 4:
        update()

    elif operation == 5:
        delete()

    elif operation == 6:
        print("\nThank you for using this program. ❤️")
        break

    else:
        print(f"\nOops invalid input please enter a number between 1-6. \n{20 * '🙄'}")
        continue
