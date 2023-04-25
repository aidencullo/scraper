import requests

URL = "https://www.opencare.com/dentists/chicago-il/"
page = requests.get(URL)

print(page.text)
