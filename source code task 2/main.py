# imports necessary classes and methods from other files
from input_validation import *
from classes import InformationEntry, OperationMethods


def main():
    address_book = OperationMethods("book.txt")

    # infinite loop that continues until user exits
    while True:

        # Display menu and get user input for chosen action
        print("\nAddress Book Manager")
        print("---------------------")
        print("1. Add")
        print("2. Print")
        print("3. Update")
        print("4. Remove")
        print("5. Search")
        print("6. Save")
        print("7. Exit")

        choice = input("Enter your operation (1-7): ")

        # Perform the corresponding action based on the user's choice
        if choice == '1':
            first_name = input_first_name()
            last_name = input_last_name()
            email = input_email()
            phone_number = input_phone()
            address = input_address()

            new_entry = InformationEntry(first_name, last_name, phone_number, address, email)
            address_book.add_entry(new_entry)

        elif choice == '2':
            address_book.print_entries()

        elif choice == '3':
            print("Enter the email address of the entry to be updated.")
            email = input_email()
            print("Now enter all the new information.\n")
            new_first_name = input_first_name()
            new_last_name = input_last_name()
            new_phone_number = input_phone()
            new_address = input_address()
            new_email = input_email()

            new_entry = InformationEntry(new_first_name, new_last_name, new_phone_number, new_address, new_email)
            address_book.update_entry(email, new_entry)

        elif choice == '4':
            print("Enter the email address of the entry to be removed.")
            email = input_address()
            address_book.remove_entry(email)

        elif choice == '5':
            keyword = input("Enter a keyword(first name/ last name/ email/ phone number/ address) to search: ")
            results = address_book.search_entries(keyword)
            if results:
                print("Search Results:")
                for entry in results:
                    print(f"First Name: {entry.first_name}")
                    print(f"Last Name: {entry.last_name}")
                    print(f"Phone Number: {entry.phone_number}")
                    print(f"Address: {entry.address}")
                    print(f"Email: {entry.email}")
                    print("--------------------------")
            else:
                print("**error**No matching entries found.")

        elif choice == '6':
            address_book.save_entries()
            print("Address book saved successfully.")

        elif choice == '7':
            print('have a nice day!!!')
            break

        else:
            print("**error**Invalid choice. Please enter a number from 1 to 7.")


# Entry point of the program
# Calls the main function to start the address book manager
if __name__ == '__main__':
    main()
