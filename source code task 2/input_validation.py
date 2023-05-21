import re


def input_first_name():
    while True:
        name = input("First Name: ")
        if bool(re.search(r'-?\d+', name)):
            print('**error** name should alphabetic letter')
            continue
        return name


def input_last_name():
    while True:
        name = input("Last Name: ")
        if bool(re.search(r'-?\d+', name)):
            print('**error** name should alphabetic letter')
            continue

        return name


def input_phone():
    while True:
        phone_number = input("Phone Number: ")
        if not bool(re.match('^[0-9]+$', phone_number)):
            print("**error** invalid input. only enter numbers")
            continue
        if len(phone_number) > 10 or len(phone_number) < 8:
            print("**error** invalid input. a phone should be of length 8 to 10 digits")
            continue

        return phone_number


def input_email():
    while True:
        email_address = input("email address: ")
        check_condition = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        if not re.match(check_condition, email_address):
            print("**error** invalid email")
            continue
        return email_address


def input_address():
    address = input("Address: ")
    return address
