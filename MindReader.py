###########################################
#
# Author: MAKDev
#
# Description: The user enters heads or tails and the computer
#              will try to guess what the user chose.
#              This program uses a hash table
#              to try and guess what the user will input.
#              It does this by getting the previous four inputs.
#              It then compares those previous inputs to the hash table
#              If one value in the hash is higher than the other
#              the computer will chose that value.
#              If the computer gets it wrong, the user gets a point.
#              If the computer gets it right, it gets a point.
#              The game ends when the user or the computer gets 25 points
#              
#
############################################

# Imports random to choose randomly when there isn't enough data
# Or if there is an equal value in the data
import random

# This will keep track of what choices the player makes based on previous choices
# The first number in the list represents heads
# The second number in the list represents tails
# There are sixteen different possibilities 
# It resembles the binary values of 0-15 with h = 0 and t = 1
playerChoiceHash = {"HHHH": [0,0], "HHHT": [0,0], "HHTH": [0,0], "HHTT": [0,0], 
        "HTHH": [0,0], "HTHT": [0,0], "HTTH": [0,0], "HTTT": [0,0], "THHH": [0,0], 
        "THHT": [0,0], "THTH": [0,0], "THTT": [0,0], "TTHH": [0,0], "TTHT": [0,0], 
        "TTTH": [0,0], "TTTT": [0,0],}
        

# Game Variables
playerPoints = 0
compPoints = 0
numOfGames = 0
allPreviousChoices = []

# INSTRUCTIONS
print()
print("----------------------------------------------------------------")
print("In this program you will play a game against the computer.")
print("You will guess either heads or tails.")
print("(Make sure to press enter after you guess)")
print("The computer will then try and guess what it thinks you chose.")
print("If the computer guesses correctly, it gets a point.")
print("If it guesses incorrectly, you get a point!")
print("The computer does not know what you chose until the end.")
print("The game ends when either the computer or you get 25 points!")
print("Good luck!")
print("----------------------------------------------------------------")
print()

#------------------------------------------------------------
# The game function is where the game will be ran
# The game runs one round at a time
# It takes no arguments and doesn't return anything
# Instead it uses already declared variables and uses those
#------------------------------------------------------------

def game():
    # I had to tell the program the variables are global
    # Otherwise it spit out an error
    global numOfGames
    global playerPoints
    global compPoints


    #--------------------
    # Main Game interface
    #--------------------
    
    print("Your Turn")
    playerChoice = input('Please enter "H" for heads and "T" for tails:')
    playerChoice = playerChoice.strip().upper()
    if playerChoice != str("H") and playerChoice != str("T"):
        print("Invalid Input. Please try again")
        return
        
    #----------------------------------------------
    # This if else statement is where the computer
    # decides to choose heads or tails
    #----------------------------------------------
    
    # If it has done less than four games it doesn't have enough data
    # So it chooses randomly
    if numOfGames < 4:
        # Updates number of games
        # Only updates the number of games up to five
        numOfGames += 1
        # Since there isn't enough data yet, it guesses randomly
        computerChoice = random.randint(0,1)
        if computerChoice == 0:
            computerChoice = "H"
        else:
            computerChoice = "T"
        # Adds the choice to a list of all previous choices
        allPreviousChoices.append(playerChoice)
    # If there are more than five games played
    # It enters this else statement
    # It checks to see if it has data 
    # and makes a guess based on the data
    else:
        # The first thing it does is get the previous four choices
        # Then turns that into a string
        previousChoices = allPreviousChoices[-4:]
        previousChoiceString = ""
        for i in range(4):
            temp = previousChoices[i]
            previousChoiceString += temp
        # Finds which one of the sixteen possibilities the previous Choices were
        # It then gets the list that the string is associated with
        headOrTails = playerChoiceHash[previousChoiceString]  
        # If heads is chose more than tails it guesses heads
        if headOrTails[0] > headOrTails[1]:
            computerChoice = "H"
        # If tails is chose more than heads it guesses tails
        elif headOrTails[0] < headOrTails[1]:
            computerChoice = "T"
        # If they are chosen equally it will guess
        else:
            computerChoice = random.randint(0,1)
            if computerChoice == 0:
                computerChoice = "H"
            else:
                computerChoice = "T"
        
        # Adds the choice to a list of all previous choices
        # If we did this before the checks, the computer would get it
        # right every time because we basically told it what the user
        # just input
        allPreviousChoices.append(playerChoice)
        if allPreviousChoices[-1] == "H":
            headOrTails[0] += 1
            playerChoiceHash.update({previousChoiceString: headOrTails})
        else:
            headOrTails[1] += 1
            playerChoiceHash.update({previousChoiceString: headOrTails})
    
    #----------------------
    # Main Game Interface
    #----------------------
    print(f'The computer chose {computerChoice} and the player chose {playerChoice}.')
    if computerChoice == playerChoice:
        print("One point for the computer!")
        compPoints += 1
    else:
        print("One Point for the player!")
        playerPoints += 1
    print(f'Computer: {compPoints} , Player: {playerPoints}')
    print()
    
        

while True:
    # First checks to see if player or computer has already won
    if playerPoints == 25:
        print("You Win!")
        print("You have beat the computer")
        break
    elif compPoints == 25:
        print("The Computer has beat you!")
        print("Give it another go!")
        break
    else:
        # If neither have won, it runs the game function
        game()