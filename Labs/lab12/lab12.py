# File:        lab12.py
# Written By:  Edward Hanson
# Date:        12/1/15
# Section:     18
# E-mail:      ehanson1@umbc.edu
# Description: 


def main():
    myFile = open("eng2sp.txt", "r")
    dictionary = createDict(myFile)
    findWord(dictionary, "")
    myFile.close()

def createDict(myFile):
    dictionary = {}
    for line in myFile:
        key, variable = line.split()
        dictionary[key] = variable
    return dictionary

def findWord(dictionary, request):
    request = str(input("Please enter the English word you would like to translate.\n(Enter the word 'EXIT' to quit the program): "))
    if request == "EXIT":
        return request
    else:
        if request in dictionary:
            print("\tIn Spanish, the word \"" + str(request) + "\" is \"" + str(dictionary[request]) + "\"")
        else:
            print("\tSorry, I do not know the word \"" + str(request) + "\"")
        findWord(dictionary, request)

main()
