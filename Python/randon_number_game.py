from random import randint

number = randint(1, 20)
guesses = []
while True:
	guess = int(input("Guess the number > "))
	if guess in guesses:
		print("You already guessed that")
	elif guess == number:
		print(f"Correct! The number was {number}")
		guesses.append(guess)
		print(f"You took {len(guesses)} guesses. They were: {guesses}.")
		replay = input("Do you want to play again? (y/n)")
		if replay == "y":
			guesses = []
			number = randint(1, 20)
			continue
		else:
			break
	elif guess < number:
		print("Too low")
	else:
		print("Too high")
	guesses.append(guess)

print("Thanks for playing")