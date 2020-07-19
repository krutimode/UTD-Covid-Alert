import requests
from bs4 import BeautifulSoup

URL = 'https://www.utdallas.edu/coronavirus/confirmed-cases/'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

#find the div in the html
results = soup.find(id='cases')
covid_elems = results.find_all('section', class_='padding white-back mb-4')

#list comprehension
for covid_elem in covid_elems:
	text = covid_elem.find('li', class_='padding white-back mb-4')
	print(text)

# To Do
# Use Twilio for texts
# Run Everyday
# Check to see new updates
# AWS Lambda
