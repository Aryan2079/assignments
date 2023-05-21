import input_data
import read_data

repeat_main = True
while repeat_main:
    print('===========================================')
    print('**Welcome to SpringWood Golf Club** ')
    print('Please choose an option from the followings.')
    print('1) Add player name and score')
    print('2) Display all the player information and scores')
    print('3) Quit.')
    print('===========================================')

    choice = input('Enter your choice: ')

    # Perform actions based on user's choice
    match choice:
        case '1':
            input_data.input_datum()  # Call the function to input player data
        case '2':
            read_data.read_datum()  # Call the function to read and display player data
        case '3':
            print('**GoodBye.. See you again!** ')
            repeat_main = False  # Set the flag to end the loop and exit the program
        case _:
            print('**error** invalid option')
            repeat_main = True  # Prompt the user to choose a valid option again
