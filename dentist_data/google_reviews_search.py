import requests
from bs4 import BeautifulSoup

"""
not working either, can't access any divs by class
"""

URL = "https://www.google.com/search?q=Smile+Obsession+-+Chicago&tbs=prfl:e"

page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
data = soup.find_all(class_="IsZvec")

print(data)
