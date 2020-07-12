import random

userInput = None

def getAndValidateNumber():
	notValid = True
	while notValid:
		print("You have to guess a number between 0-5")
		userInput = input()
		if userInput.isdigit():
			userInput = int(userInput)
			if userInput > 0 and userInput < 5:
				print("You picked the number " + str(userInput))
				notValid = False
				randomNumber()


numberToGuess = None

def randomNumber():
	numberToGuess = random.randint(1, 4)
	print("The Random number: " + str(numberToGuess))
	checkWin(numberToGuess)
	
	
def checkWin(numberToGuess):
	if userInput == numberToGuess:
		print("You won !")
	else:
		print("You lose !")

getAndValidateNumber()