import requests
from bs4 import BeautifulSoup

URL = "https://www.opencare.com/dentists/chicago-il/"

def printResults(results_param):
    if results is None:
        print("no results found")
    else:
        for job_element in results:
            name = job_element.text
            print(name, end="\n" * 1)

page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find_all(class_="name")

printResults(results)

print("Scraping url : %s" % URL)
