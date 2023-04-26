from selenium import webdriver
from selenium.webdriver.common.by import By
import time

"""
incomplete, not sure if i will pursue this approach further
"""

driver = webdriver.Chrome()

# Open Scrapingbee's website
driver.get("https://www.google.com/maps/search/dentist/@41.8462044,-88.0976587,10z")

driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(100)
# Match all img tags on the page
data = driver.find_elements(By.CLASS_NAME, "hfpxzc")
#data = driver.find_elements(By.CLASS_NAME, "hfpxzc")[0].get_attribute("aria-label")

print(len(data))
