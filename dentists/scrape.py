import requests
from bs4 import BeautifulSoup

URL = "https://www.opencare.com/dentists/chicago-il/"

companies = []
ratings = []


def unparen(val):
    return val.replace('(','').replace(')','')  

def processRatings(data):
    global ratings
    processResults(data, ratings)
    ratings = map(unparen, ratings)

def processCompanies(data):
    processResults(data, companies)

def processResults(results_param, values):
    if results_param is None:
        print("no results found")
    else:
        for job_element in results_param:
            value = job_element.text
            values.append(value)

def scrape():
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    companies_raw = soup.find_all(class_="name")
    ratings_raw = soup.find_all(class_="ml-5 text-muted")
    processRatings(ratings_raw)
    processCompanies(companies_raw)

def printResults():
    print(list(ratings))
    print(list(companies))

scrape()
printResults()

print("Scraping url : %s" % URL)
