#!/usr/bin/python3

print("NELNUMBERS by @nvemb3r")
print("----------------------")

current_int = 0
area_code = 0
is_valid = False
file_path = ""

while is_valid is False:

    try:
        # Ask for the file path of output for the wordlist
        file_path = input("Word list write location? : ")
        wordlist = open(file_path, "w")

        # Proceed if input is valid
        is_valid = True

    # If something goes wrong
    except IOError:

        # Display an error message
        print("Could not write file. Please try agian.")
        is_valid is False

# Reset the input validity flag
is_valid = False

while is_valid is False:

    try:
        # Ask for the target area code
        area_code = input("Area Code? : ")

        # If the input is a three digits
        if len(area_code) == 3 and int(area_code):

            # Input is valid
            is_valid = True
        else:
            # Input is invalid
            is_valid = False
            print("Please enter a valid area code")

    except ValueError:
        # Otherwise, it is invalid
        is_valid = False

        # Tell user to try again
        print("Please enter a valid area code")

# Notify the user that work is being done
print("Writing wordlist...")

# Print EVERY phone number in an area code
while (current_int < 9999999 + 1):
    # Print the area code, with the appended local number
    # print str(area_code) + str(current_int).zfill(7)
    wordlist.write(str(area_code) + str(current_int).zfill(7) + "\n")
    current_int = current_int + 1

# Close the wordlist file
wordlist.close()

# Notify the user that the job is done.
print("Done!")
print("")
