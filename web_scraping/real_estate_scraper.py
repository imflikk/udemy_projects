#!/bin/python3

import requests
import pandas
from bs4 import BeautifulSoup


# Updated URL: r = requests.get("http://www.pyclass.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/", headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
# Century21 URL: https://www.century21.com/real-estate/roseville-ca/LCCAROSEVILLE/

r = requests.get("https://www.century21.com/real-estate/roseville-ca/LCCAROSEVILLE/")
content = r.content

soup = BeautifulSoup(content, "html.parser")

results = soup.find_all('div', {'class':'results-label'})
total_listings = results[0].find('strong').text.replace('(', '').replace(')', '')

print("Total listings in Roseville, CA: " + total_listings + "\n")

properties = soup.find_all('div',{'class':'property-card'})

for item in properties:
    city = properties[properties.index(item)].find('div',{'class':'property-city'}).text.strip()
    address = properties[properties.index(item)].find('div',{'class':'property-address'}).text.strip()
    beds = properties[properties.index(item)].find('div',{'class':'property-beds'}).text.strip()
    baths = properties[properties.index(item)].find('div',{'class':'property-baths'}).text.strip()
    sqfeet = properties[properties.index(item)].find('div',{'class':'property-sqft'}).text.strip()
    price = properties[properties.index(item)].find('a',{'class':'listing-price'}).text.strip()

    print(price)
    print(beds)
    print(baths)
    print(sqfeet)
    print(address)
    print(city)
    print()
