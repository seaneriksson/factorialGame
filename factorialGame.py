import sys

numberList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19 ,20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
numberListCopy = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19 ,20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
primeList = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
factorsList = []
p1Score = 0
p2Score = 0
leader = 1
searcher = 2
gameOver = False


def printNumberList():
    print(*numberList, sep = ", ")

def printScores():
    global p1Score
    global p2Score
    print ("Player 1 score is " + str(p1Score)) 
    print ("Player 2 Score is " + str(p2Score))
    print ("")
    print ("Leader is player " + str(leader))
    print ("Searcher is player " + str(searcher))
    print ("")

def gameOverCheck():
    global gameOver
    global p1Score
    global p2Score
    if len(numberList) == 0:
        print ("GAME OVER")
        print ("")
        print ("Player 1 score is " + str(p1Score)) 
        print ("Player 2 Score is " + str(p2Score))
        print ("")
        if p1Score > p2Score:
                print ("Player 1 Wins!")
        if p2Score > p1Score:
                print ("Player 2 Wins!")
        gameOver = True
        gameOverMessage = int(input("Great Job!"))

def playAgain():
    global numberList
    global numberListCopy
    playAgain = int(input("Do you want to play another round? Enter Y for Yes or N for No"))
    if playAgain == "Y":
        numberList = numberListCopy
        factorsList = []
        p1Score = 0
        p2Score = 0
        leader = 1
        searcher = 2
        gameLoop()
    if playAgain == "N":
        sys.exit()
        ##
            
 

def createFactors(inputNumber):
    global factorsList
    factorsList = []
    for x in numberList:
        if inputNumber % x == 0:
            #print (inputNumber % x)
            factorsList.append(x)
    #factorsList = factorsList[:-1]
    #print ("The factors are: " + str(factorsList))
    return factorsList

def checkFactorInput(numberInput, p1Input):
    global factorsList
    global p1Score
    global p2Score
    global leader
    global searcher
    proceed = False
    for x in factorsList:
        #print (numberInput)
        #print (x)
        if x == numberInput:
            proceed = True
            if searcher == 1:
                print ("Player 1 found a factor")
                print ("")
                p1Score = p1Score + numberInput
                printScores()
            if searcher == 2:
                print ("Player 2 found a factor")
                print ("")
                p2Score = p2Score + numberInput
                printScores()
            factorsList.remove(numberInput)
            numberList.remove(numberInput)
            #print ("The remaining factors are: " + str(factorsList))
            checkIfAllFactorsFound(factorsList, p1Input)
        else:
            proceed = False
    if proceed == False:
        print ("Sorry. The entered value is not a factor")
        print ("")
        if searcher == 1:
            leader = 1
            searcher = 2
            print ("Player 1's turn")
            print ("")
            p1Turn()
        if searcher == 2:
            leader = 2
            searcher = 1
            print ("Player 2's turn")
            print ("")
            p2Turn()
    print ("")
    printScores()
    print ("")
    return factorsList
    
def checkIfAllFactorsFound(factorsList, originalInput):
    global leader
    global searcher
    if len(factorsList) >= 1:
        print ("")
        print ("The available numbers are " + str(numberList))
        print ("")
        if searcher == 1:
            newInput = int(input("Player 1 choose another factor of " + str(originalInput) + ": "))
        if searcher == 2:
            newInput = int(input("Player 2 choose another factor of " + str(originalInput) + ": "))
        print ("")
        checkFactorInput(newInput, originalInput)
    else:
        print ("All factors have been found")
        print ("")
        if leader == 1:
            leader = 2
            searcher = 1
        else:
            leader = 1
            searcher = 2
        if len(numberList) >= 1 and leader == 1:
            print ("Player 1's turn")
            print ("")
            p1Turn()
        if len(numberList) >= 1 and leader == 2:
            print ("Player 2's turn")
            print ("")
            p2Turn()
    return factorsList
                

def p1Turn():
    global gameOver
    gameOverCheck()
    if gameOver != True:
        primeResult = False
        leader = 1
        searcher = 2
        proceed = False
        p1Input = int(input("Player 1 choose one of the following numbers: " + str(numberList) + ": "))
        print ("")
        for x in numberList:
            if x == p1Input:
                proceed = True
                break
            else:
                proceed = False
        if proceed == True:
            global p1Score
            p1Score = p1Score + p1Input
            numberList.remove(p1Input)
            for x in primeList:
                if p1Input == x:
                        print ("The chosen number is a prime number.")
                        print ("")
                        printScores()
                        primeResult = True
            if primeResult == True and len(numberList) >= 1:
                leader = 2
                searcher = 1
                if len(numberList) >= 1:
                    p2Turn()
                else:
                    gameOverCheck()
            else:
                printScores()
                print ("")
                if len(numberList) >= 1:
                    factorsFound = createFactors(p1Input)
                    if len(factorsFound) >= 1:
                        print ("")
                        print ("The available numbers are " + str(numberList))
                        print ("")
                        p2Input = int(input("Player 2 choose a factor of " + str(p1Input) + ": "))
                        print ("")
                        checkFactorInput(p2Input, p1Input)
                    else:
                        p2Turn()
                else:
                    gameOverCheck()
        if proceed == False and gameOver == False:
            p1Turn()
        return p1Input

def p2Turn():
    global gameOver
    gameOverCheck()
    if gameOver != True:
        primeResult = False
        leader = 2
        searcher = 1
        proceed = False
        p2Input = int(input("Player 2 choose one of the following numbers: " + str(numberList) + ": "))
        print ("")
        for x in numberList:
            if x == p2Input:
                proceed = True
                break
            else:
                proceed = False
        if proceed == True:
            global p2Score
            p2Score = p2Score + p2Input
            numberList.remove(p2Input)
            for x in primeList:
                if p2Input == x:
                        print ("The chosen number is a prime number.")
                        print ("")
                        printScores()
                        print ("")
                        primeResult = True
            if primeResult == True and len(numberList) >= 1:
                leader = 1
                searcher = 2
                if len(numberList) >= 1:
                    p1Turn()
                else:
                    gameOverCheck()
            else:
                printScores()
                print ("")
                if len(numberList) >= 1:
                    factorsFound = createFactors(p2Input)
                    if len(factorsFound) >= 1:
                        print ("")
                        print ("The available numbers are " + str(numberList))
                        print ("")
                        p1Input = int(input("Player 1 choose a factor of " + str(p2Input) + ": "))
                        print ("")
                        checkFactorInput(p1Input, p2Input)
                    else:
                        p1Turn()
                else:
                    gameOverCheck()
        if proceed == False and gameOver == False:
            p2Turn()
        return p2Input


                        
def gameLoop():
    p1Turn()

gameLoop()



