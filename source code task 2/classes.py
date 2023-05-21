class InformationEntry:
    # Represents an entry in the address book
    # Stores information such as first name, last name, phone number, address, and email address

    def __init__(self, first_name, last_name, phone_number, address, email):
        # Initialize a new address book entry with the provided attributes
        # Sets the first name, last name, phone number, address, and email fields
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.address = address
        self.email = email


class OperationMethods:
    # Provides methods to interact with the address book and perform various operations

    def __init__(self, filename):
        # Initialize the address book manager with the specified filename
        # Sets up the filename attribute to store the address book data
        # Loads entries from the file into the entries list
        self.filename = filename
        self.entries = []
        self.load_entries()

    def load_entries(self):
        try:
            with open(self.filename, 'r') as file:
                for line in file:
                    entry_data = line.strip().split(' | ')
                    entry = InformationEntry(*entry_data)
                    self.entries.append(entry)
        except FileNotFoundError:
            print("**error** Address book file not found. Creating a new address book.")

    def save_entries(self):
        # Saves information such as first name, last name, phone number, address, and email address in the file

        with open(self.filename, 'w') as file:
            for entry in self.entries:
                entry_line = ' | '.join([
                    entry.first_name or '',
                    entry.last_name or '',
                    entry.email or '',
                    entry.phone_number or '',
                    entry.address or ''

                ])
                file.write(entry_line + '\n')

    def add_entry(self, entry):
        # stores information such as first name, last name, phone number, address, and email address in the entries list

        if self.is_duplicate_email(entry.email):
            print("**error** Email address already exists.")
        else:
            self.entries.append(entry)
            self.sort_entries()
            print("Entry added successfully!!!")

    def remove_entry(self, email):
        # removes specified entry attributes from the file

        for entry in self.entries:
            if entry.email == email:
                self.entries.remove(entry)
                self.sort_entries()
                print("Entry removed successfully!!!")
                return
        print("**error** Entry not found.")

    def update_entry(self, email, new_entry):
        # Provides methods to retrieve and update the entry's attributes

        for entry in self.entries:
            if entry.email == email:
                entry.first_name = new_entry.first_name
                entry.last_name = new_entry.last_name
                entry.phone_number = new_entry.phone_number
                entry.address = new_entry.address
                entry.email = new_entry.email
                print("Entry updated successfully!!!")
                return
        print("**error** Entry not found.")

    def search_entries(self, keyword):
        # Performs a case-insensitive search on a provided keyword
        # Returns a list of matching entries or an empty list if no matches are found

        search_results = []
        for entry in self.entries:
            if keyword.lower() in entry.first_name.lower()\
                    or keyword.lower() in entry.last_name.lower()\
                    or keyword.lower() in entry.email.lower()\
                    or keyword.lower() in entry.first_name.lower()\
                    or keyword.lower() in entry.phone_number.lower():
                search_results.append(entry)
        return search_results

    def print_entries(self):
        # provides a method to display the entry attributes in the screen

        if self.entries:
            for entry in self.entries:
                print("First Name:", entry.first_name)
                print("Last Name:", entry.last_name)
                print("Email:", entry.email)
                print("Phone Number:", entry.phone_number)
                print("Address:", entry.address)
                print("--------------------------")
        else:
            print("**error** Address book is empty.")

    def is_duplicate_email(self, email):
        # Ensures uniqueness of email addresses in the address book

        for entry in self.entries:
            if entry.email == email:
                return True
        return False

    def sort_entries(self):
        # Sorts the entries in the address book based on last name and then first name

        self.entries.sort(key=lambda entry: (entry.last_name or '', entry.first_name or ''))
