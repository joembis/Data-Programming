import requests
from bs4 import BeautifulSoup
import csv

base_url = "https://www.rithmschool.com"
# response = requests.get(base_url)

# soup = BeautifulSoup(response.text, "html.parser")
next_url = base_url + "/blog" # set to the first page of the blog

with open("scraping_blog_data.csv", "w+", newline= "") as csv_file:
	csv_writer = csv.writer(csv_file)
	csv_writer.writerow(["title", "url", "date"]) # write the title row before the loop
	while True:
		response = requests.get(next_url) # make a new request with the modified url
		soup = BeautifulSoup(response.text, "html.parser")
		articles = soup.find_all("article")
		for article in articles:
			atag = article.find("a") # store the data in the <a> tag
			title = atag.get_text() # .get_text() gets just the text
			url = atag["href"] # extract the data tagged with "href"
			#the date is not in the <a> tag, it's in the <time> tag
			date = article.find("time")["datetime"]
			# print(title, url, date)
			csv_writer.writerow([title, url, date])
		try: # check and see if there is a next button, and if there is, extract the <a> tag containing the url modifier
			navs = soup.find(class_ = "next")
			a_tag = navs.find("a")
		except: # if there is no next button, break the loop
			print("Finished Scraping")
			break
		else: #if there is a modifer, append it to the base_tag and re-run the loop
			next_url = base_url + a_tag["href"]
			# print(next_url)
