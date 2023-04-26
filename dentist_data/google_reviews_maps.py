import requests
from bs4 import BeautifulSoup

"""
incomplete, not sure if i will pursue this approach further
"""

URL = "https://www.google.com/maps/search/dentist/@41.8548265,-88.0135516,10z"

page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
#names_raw = soup.find_all(class_="hfpxzc")

print(soup)
