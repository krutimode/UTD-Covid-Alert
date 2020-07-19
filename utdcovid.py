import requests
from bs4 import BeautifulSoup
from twilio.rest import Client

URL = 'https://www.utdallas.edu/coronavirus/confirmed-cases/'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

#find the directory in the html
covid_elems = soup.find_all('div', class_='padding white-back mb-4')
listings = covid_elems[1].find_all('li')

#list comprehension
listings_text = [listing.get_text() for listing in listings]
print(listings_text)

# To Do
# Use Twilio for texts
# Run Everyday
# Check to see new updates
# AWS Lambda
