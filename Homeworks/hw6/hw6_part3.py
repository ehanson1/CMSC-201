# File:        hw6_part3.py
# Written by:  Edward Hanson
# Date:        10/17/15
# Lab Section: 18
# UMBC email:  ehanson1@umbc.edu
# Description: Calculates total amount of words and average word length
#              of another file.


def main():
    # prompts the user to input desrired file name
    fileName = ""
    while fileName[-4:] != ".txt" and fileName[-4:] != ".dat":
        fileName = str(input("Please enter the name of the file to open: "))
        if fileName[-4:] != ".txt" and fileName[-4:] != ".dat":
            print("The file must end in .txt or .dat to be valid")

    # initializes the variables
    myFile = open(fileName, "r")
    wordCount = 0
    charCount = 0
    avgChar = 0
    wordList = []
    row = []

    # creates a 1-D list of all words in the file
    for line in myFile:
        line.strip()
        row = line.split()
        for item in row:
            wordList.append(item)

    # sums all words and characters in the file
    for item in wordList:
        wordCount += 1
        charCount += len(item)

    # finds average of characters per word in file
    avgChar = charCount / wordCount

    # prints word count and average word length
    print("The file " + fileName + " has " + str(wordCount) + " words in it.")
    print("On average, each word is " + str(avgChar) + " characters long.")

    # closes the opened file
    myFile.close()

main()
