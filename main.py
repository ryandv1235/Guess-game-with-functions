import random

userInput = None

def Game():
	inGame = True
	while inGame:
		print("Guess the number between 0-5")
		userInput = input()
		if userInput.isdigit():
			userInput = int(userInput)
			print("Your number is: " + str(userInput))
			numberToGuess = random.randint(1, 4)
			print("The random number: " + str(numberToGuess))
			if userInput == numberToGuess:
				print("You won!")
				inGame = False
			else:
				print("You lost! Try again.")

Game()
