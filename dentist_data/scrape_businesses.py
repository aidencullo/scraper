import requests
from bs4 import BeautifulSoup
import os

"""
Script for scraping company names and star ratings from https://www.opencare.com/dentists/chicago-il/
"""

URL = "https://www.opencare.com/dentists/chicago-il/"

companies = []
ratings = []

# text manipulation

def unparen(val):
    return val.replace('(','').replace(')','')  

def uncomma(val):
    return val.split(',')[0]

# extracing info we want from html elements

def process_ratings(data):
    global ratings
    process_results(data, ratings)
    ratings = list(map(unparen, ratings))

def process_companies(data):
    global companies
    process_results(data, companies)
    companies = list(map(uncomma, companies))

def process_results(results_param, values):
    if results_param is None:
        print("no results found")
    else:
        for job_element in results_param:
            value = job_element.text
            values.append(value)

# main scraper
            
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

# file manipulation
    
def write_to_file():
    f = open("dentists.csv", "a")
    f.write("Companies, Ratings\n")
    for company, rating in zip(companies, ratings):
        formatted_txt = "%s,%s\n" % (company, rating)
        f.write(formatted_txt)
    f.close()

def read_file():
    f = open("dentists.csv", "r")
    print(f.read())

def delete_file():
    os.remove("dentists.csv")

# main
    
delete_file()
scrape()
write_to_file()
read_file()

print("Scraping url : %s" % URL)
