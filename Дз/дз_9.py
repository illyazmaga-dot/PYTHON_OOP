import requests
from bs4 import BeautifulSoup

response = requests.get("http://books.toscrape.com/")
soup = BeautifulSoup(response.text, features="html.parser")
books = soup.find_all("h3")

for book in books:
    title = book.find("a")["title"]
    print(title)