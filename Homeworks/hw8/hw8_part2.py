# File:        hw8_part2.py
# Written by:  Edward Hanson
# Date:        11/20/15
# Lab Section: 18
# UMBC email:  ehanson1@umbc.edu
# Description: draws a right triangle with the tip facing down using an inputed
#              character and height


def main():
    height = int(input("Please enter a height for the triangle: "))
    while height < 1:
        print("Incorrect input! Value of height must be greater than 0.")
        height = int(input("Please enter a height for the triangle: "))
    char = str(input("Please enter a character for your triangle: "))
    print()
    tri(height, char)

# tri() is a recursive function that creates a right triangle with a tip facing down
# Input: the height of the triangle and character used to make the triangle
# Ouput: a right triangle with its tip facing down
def tri(height, char):
    print(char * height)
    if height == 1:
        return 1
    else:
        return tri(height - 1, char)

main()
