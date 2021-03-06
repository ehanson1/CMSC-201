# File:        lab6.py
# Author:      Edward Hanson
# Date:        10/6/15
# Section:     18
# E-mail:      ehanson1@umbc.edu
# Description: Gives the user 3 chances to guess a predefined password.


def main():
    PASSWORD = "UMBCrulz"
    attempt = ""
    count = 0
    while attempt != PASSWORD and (count < 3):
        attempt = str(input(str(3-count)+" tries left\nEnter the password: "))
        count += 1
        if attempt == PASSWORD:
            print("Successful Login")
        else:
            print("Unsuccessful Login")
    if count == 3:
        print("Too many incorrect attempts. You are locked out of the system")
main()
