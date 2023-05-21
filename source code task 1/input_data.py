import re


def input_datum():
    run_again = True
    while run_again:
        # Prompt user for player name
        name = input('Enter the player name: ')

        # Check if name contains any digits
        if bool(re.search(r'-?\d+', name)):
            print('**error** name should be alphabetic letters')
            run_again = True
            continue

        # Prompt user for score
        score = input('Enter the score(0-100): ')

        # Check if score is a valid integer within the range of 0-100
        if (not bool(re.match('^[0-9]+$', score))) or int(score) < 0 or int(score) > 100:
            print('**error** invalid input')
            run_again = True
            continue

        # Open the "golf.txt" file in append mode and write the player's name and score
        f = open("golf.txt", "a")
        f.write("| " + str(name) + " " * (19 - len(name)) + "| " + str(score) + " " * (10 - len(score)) + "|\n")
        f.close()

        # Prompt user if they want to add another player
        option = input('Do you want to add another player? Y/N: ')
        if option == 'Y' or option == 'y' or option == 'Yes':
            run_again = True
        else:
            run_again = False
