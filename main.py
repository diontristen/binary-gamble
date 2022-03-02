# even length
# number of input should be same as the given integer
# 1 0 1 0 1 0

### Functions
def getInput():
    try:
        initialInput = input("Enter even number: ")
        parseInput = int(initialInput)
        validate = checkIfEven(parseInput)
        if validate == True:
            getList(parseInput)
        else:
            getInput()
    except:
        print("Invalid input")


def checkIfEven(gInput):
    try:

        if (gInput % 2 == 0):
            return True
        return False
    except ValueError:
        print("Please enter an integer")
        return False
    except:
        print("Error")

def getList(parseInput):
    try:
        givenList = input("Enter Binary: ")
        givenList = givenList.split()
        validate = checkLength(givenList, parseInput)    # string to list and validate
        if validate == True:
            valid = checkIfBinary(givenList)
            if valid == True:
                checkWinner(givenList, parseInput)
            else:
                print("not valid")
        else:
            print("Number is not equal to the length of the list")
    except:
        print("ERROR")


def checkLength(gList, parseInput):
    try:
        if len(gList) == parseInput:
            return True
        return False
    except:
        print("ERROR")

def checkIfBinary(gList):
    try:
        validList = ['1', '0']
        valid = all(el in validList for el in gList)
        return valid
    except:
        print("ERROR")

def checkWinner(gList, parseNumber):
    try:
        middle = int(parseNumber / 2)
        firstHalf = gList[:middle]
        secondHalf = gList[middle:]

        firstWinner = firstHalf.count('1')
        secondWinner = secondHalf.count('1')

        if firstWinner > secondWinner:
            print("Left Side Wins")
        elif firstWinner < secondWinner:
            print("Right Side Wins")
        else:
            print("It's a Tie")
    except:
        print("ERROR")


 #### Call Functions
getInput()


