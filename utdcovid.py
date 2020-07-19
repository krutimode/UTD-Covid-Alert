import requests
from bs4 import BeautifulSoup

URL = 'https://www.utdallas.edu/coronavirus/confirmed-cases/'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='cases')

covid_elems = results.find_all('section', class_='padding white-back mb-4')

for covid_elem in covid_elems:
	text = covid_elem.find('li', class_='padding white-back mb-4')
	print(text)