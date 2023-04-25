import requests
from bs4 import BeautifulSoup

URL = "https://www.opencare.com/dentists/chicago-il/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="ResultsContainer")

print(results.prettify())
