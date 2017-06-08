"""
File: Problem2.py
Ian Davidson
June 7th, 2017

Description:

Write a function that flattens a potentially nested list. That is, it takes a list where some of
the elements might be lists, and returns one list with no list elements. E.g.
[[1,2],3,[[4,5],6],7] ­> [1,2,3,4,5,6,7] Hint: this is a lot like a tree­walking problem.

"""


def flattenListLocal(oldList, newList ):
    """
This algorithm recursively breaks down list named: oldlist using a depth-first traversal,
Then adding each element found to a list named: newList
    """

    #basecase to escape function when done
    if len(oldList) == 0:
        return


    #distinguish between list or int
    if type(oldList[0]) == list:
    #check to see if the first elem in old list is actually a deep list

        flattenListLocal(oldList[0], newList) #this is the case which deals with deep lists
    else:
        newList.append(oldList[0])

    #no matter the direction of that if statement, by this point everything from oldList[0] should be inside newList
    oldList.pop(0)


    #recusive call with a smaller oldList
    return flattenListLocal(oldList, newList)


def flattenList(startingList):
    """
this function calls the a helper function then returns the flat-version of the parameter: startingList.

Because lists are passed by reference we can just the return the fully formed, flat list: newList
    """

    newList  = []
    flattenListLocal(startingList, newList)

    return newList

def main():
    list = [[1,2],3,[[4,5],6],7]
    flatList = flattenList(list)
    print(flatList)

main()