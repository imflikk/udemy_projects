#!/bin/python3

import requests
import pandas
from bs4 import BeautifulSoup


# Updated URL: r = requests.get("http://www.pyclass.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/", headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})

base_url = "https://www.century21.com"

# Search site above for appropriate URL, the one below will not load correctly.
r = requests.get("https://www.century21.com/real-estate/city-stateabbreviation/")
content = r.content

soup = BeautifulSoup(content, "html.parser")

results = soup.find_all('div', {'class':'results-label'})
total_listings = results[0].find('strong').text.replace('(', '').replace(')', '')

print("Total listings: " + total_listings + "\n")

properties = soup.find_all('div',{'class':'property-card'}, limit=None)
properties_list = []

for item in properties:
    d = {}
    try:
        d['Price'] = properties[properties.index(item)].find('a',{'class':'listing-price'}).text.strip()
    except:
        d['Price'] = None
    try:
        d['Beds'] = properties[properties.index(item)].find('div',{'class':'property-beds'}).text.strip()
    except:
        d['Beds'] = None
    try:
        d['Baths'] = properties[properties.index(item)].find('div',{'class':'property-baths'}).text.strip()
    except:
        d['Baths'] = None
    try:
        d['SqFeet'] = properties[properties.index(item)].find('div',{'class':'property-sqft'}).text.strip()
    except:
        d['SqFeet'] = None
    try:
        d['Address'] = properties[properties.index(item)].find('div',{'class':'property-address'}).text.strip()
    except:
        d['Address'] = None
    try:
        d['City'] = properties[properties.index(item)].find('div',{'class':'property-city'}).text.strip()
    except:
        d['City'] = None
    try:
        d['URL'] = base_url + properties[properties.index(item)].find('a',{'class':'listing-price'})['href']
    except:
        d['URL'] = None
    
    
    
    
    
    

    # print(price)
    # print(beds)
    # print(baths)
    # print(sqfeet)
    # print(address)
    # print(city)
    # print(base_url + link)
    # print()
    properties_list.append(d)

df = pandas.DataFrame(properties_list)
df.to_csv("output.csv")