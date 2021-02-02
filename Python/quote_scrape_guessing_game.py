from bs4 import BeautifulSoup
import requests
import random

base_url = "https://quotes.toscrape.com"
master_list = []
next_url = ""

# scraping the web to make a master list. each item in the list is a list with [quote, author, href]
while True:
	#scraping for the data
	response = requests.get(base_url+next_url)
	soup = BeautifulSoup(response.text, "html.parser")
	quotes = soup.find_all(class_="quote")

	# saving into the master_list
	for item in quotes:
		quote = item.find(class_="text").text
		author = item.find(class_="author").text
		href = item.find("a")["href"]
		master_list.append([quote, author, href])
	# check if there is a next button on the page. if so, follow it and run the loop again
	try:
		next_url = soup.find(class_="next").a["href"]
	except:
		print("no more pages")
		break
	else:
		print(next_url)

# would be a good idea here to save all the scraped data to a file so it doesn't rescrape the same data each time the program is run. Then on subsequent executions, check if there is a file with the data and read it instead of rescraping.

remaining_guesses = 4
while True:
	# choose a random quote and retrieve data for the clues
	random_quote = random.choice(master_list)
	# make a request for the authors info page to get data for the clues
	response = requests.get(base_url + random_quote[2]).text
	soup = BeautifulSoup(response, "html.parser")
	# data for the clues:
	birth_date = soup.find(class_="author-born-date").text
	birth_loc = soup.find(class_="author-born-location").text
	author_names = random_quote[1].split()
	first_initial = author_names[0][0]
	last_initial = author_names[-1][0]
	# put the clue data into a list of clues
	clues = [
	 	f"The author was born on {birth_date}",
	 	f"The author was born {birth_loc}",
	 	f"The author's initials are {first_initial} {last_initial}"]

	print("Here's a quote: \n")
	print(random_quote[0], "\n")
	"""# lines used to check code was working #
	print(random_quote[1], "\n") # cheat-check line
	print(random_quote[2], "\n") # cheat-check line
	print(birth_date) # cheat-check line
	print(birth_loc) # cheat-check line
	print(first_initial, last_initial) # cheat-check line
	print(clues) # cheat-check line
	"""

	# main game loop
	while remaining_guesses > 0:
		guess = input(f"Who said this? {remaining_guesses} guesses remaining > ")
		if guess.upper() == random_quote[1].upper():
			print("Correct!")
			break
		elif remaining_guesses > 1:
			print("Incorrect. Here's a clue:")
			print(clues[-(remaining_guesses-1)])
			remaining_guesses -= 1
		else:
			print(f"Bad luck! The answer was {random_quote[1]}")
			remaining_guesses -= 1

	again = input("Would you like to play again (y/n)")
	if again == "y" :
		remaining_guesses = 4
		continue
	elif again == "n": break

