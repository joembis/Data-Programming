
import requests
import termcolor
import colorama
import pyfiglet
import random
colorama.init()

valid_colors = ("red", "green", "yellow", "blue", "magenta", "cyan", "white")
on_colors = ("on_red", "on_green",
			"on_blue", "on_magenta", "on_cyan", "on_white")
url = "https://icanhazdadjoke.com/search"

# makes and prints the Dad Joke 3000 title
dj3000 = pyfiglet.figlet_format("Dad Joke 3000", "standard")
colour_dj3000 = termcolor.colored(
	dj3000,
	random.choice(valid_colors),
	random.choice(on_colors),
	)

print(colour_dj3000)

while True:
	search_term = input("What would you like to hear a joke about? > ")

	# retrieve the json data from the url with the dad jokes, as a string
	response = requests.get(
		url, 
		headers= {"accept": "application/json"},
		params= {"term": search_term})


	#turn the string data into a python dictionary
	data = response.json()  

	# try and print a random joke. if no jokes returned, throw an error 
	# message and ask to try again
	results = data["results"]
	jokes = [joke["joke"] for joke in results]
	try:
		print(random.choice(jokes))
		another = input("Would you like to hear another? (y/n) > ")
		if another == "n":
			break
	except:
		print(f"Sorry, there are no jokes about {search_term}.")
		try_again = input("Would you like to try again? (y/n) > ")
		if try_again == "n":
			break