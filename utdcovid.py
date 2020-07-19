import requests
import os
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

first = listings_text[0]

#twilio things
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
fromnum = os.environ['TWILIO_NUMBER']
tonum = os.environ['TO_NUMBER']
client = Client(account_sid, auth_token)

message = client.messages.create(body =first, from_ = fromnum,to = tonum)

# To Do
# Run Everyday
# Check to see new updates
# AWS Lambda
