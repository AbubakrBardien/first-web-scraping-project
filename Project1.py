from bs4 import BeautifulSoup  # type: ignore
import requests
import csv

url = "https://quotes.toscrape.com/"

# This will send a GET request to the specified URL, and return a response object
page = requests.get(url)

soup = BeautifulSoup(page.text, "html.parser")  # HTML of webpage
# print(soup.prettify())  # Prints HTML with proper indenting

# print(soup.find("div").prettify())  # type: ignore # Retrieves the first 'div' tag and all it's contents
# print(soup.find_all("div")) # Retrieves an array or 'div' tags, and all their contents
# print(soup.find_all("div", attrs={"class": "quote"}))

# print(soup.find("div", attrs={"class": "quote"}).prettify())  # type: ignore

# print(soup.find("span").text) # Finds the 1st quote

# -----------------------------------------------------------
# Project Goal: Scrape Quotes and Authors from a webpage to a CSV file

# List of Quotes on webpage
quotes = soup.find_all("span", attrs={"class": "text"})

# List of quote Authors on webpage
authors = soup.find_all("small", attrs={"class": "author"})

csvFile = open("scraped_quotes.csv", "w")
writer = csv.writer(csvFile)
writer.writerow(["Quotes", "Authors"])

# The zip() function basically puts the 2 lists into a tuple.
# Since the lists are equal in length, this code will loop through all the
# element, otherwise the loop would stop when the shortest list is done.
for quote, author in zip(quotes, authors):
    # print(quote.text, author.text, sep="\t")
    writer.writerow([quote.text, author.text])

csvFile.close()
print("Done")
