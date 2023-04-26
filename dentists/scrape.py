import requests
from bs4 import BeautifulSoup

URL = "https://www.opencare.com/dentists/chicago-il/"

companies = []
ratings = []

def unparen(val):
    return val.replace('(','').replace(')','')  

def uncomma(val):
    return val.split(',')[0]

def process_ratings(data):
    global ratings
    processResults(data, ratings)
    ratings = list(map(unparen, ratings))

def process_companies(data):
    global companies
    processResults(data, companies)
    companies = list(map(uncomma, companies))

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
    process_ratings(ratings_raw)
    process_companies(companies_raw)

def print_results():
    print(list(ratings))
    print(list(companies))

def write_to_file():
    f = open("dentists.csv", "a")
    
    for company, rating in zip(companies, ratings):
        formatted_txt = "%s,%s\n" % (company, rating)
        f.write(formatted_txt)

    f.close()

def read_file():
    f = open("dentists.csv", "r")
    print(f.read())

scrape()
write_to_file()
read_file()

print("Scraping url : %s" % URL)
