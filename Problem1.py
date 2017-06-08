"""
File: Problem1.py
Ian Davidson
June 7th, 2017

Description:

Write a function that takes the path to a text file, and returns a dictionary mapping every
unique word to its frequency. e.g. {‘the’ : 5, ‘you’: 12}. Run it on the attached file
“lebowski­intro.txt” to test your work. Hint: the Python collections module has
something useful for you here.

"""


# include this=> /usr/local/Cellar/python3/3.5.1/Frameworks/Python.framework/Versions/3.5/lib/python3.5/collections/
import collections


def expectedInput(c):
    #this function will return true if the character c, is aphabetic or an apostrophe, false otherwise
    if c.isalpha() or c == "'":
        return True
    return False


def createRepresentation(fileName):
    # opens file for reading
    infile = open(fileName, "r")

    c = infile.read(1) #reads in one character

    currentStr = ""

    container = collections.Counter()#container used is a Counter
    endWord = False

    while(c != ''):#iterative walk through the input file, one character at a time

        if expectedInput(c):
            # only expected characters will be in the container
            currentStr += c.lower()
        else:
            endWord = True


        if endWord:
            if currentStr != '':
                container[currentStr] += 1;

                currentStr = ""
            endWord = False

        c = infile.read(1)


    infile.close()

    return container


def main():

    filePath = input("enter path to file: ")


    container = createRepresentation(filePath)

    print(container)

main()