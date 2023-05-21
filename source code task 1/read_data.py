def read_datum():
    # Print table headers
    print("| player name" + " " * 8 + "| score" + " " * 5 + "|")
    print("|====================|===========|")

    # Open the "golf.txt" file in read mode
    f = open("golf.txt", "r")

    # Read and print the contents of the file
    print(f.read())

    # Close the file
    f.close()
