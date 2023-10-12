import requests
from bs4 import BeautifulSoup
import json
url = 'https://www.ncbi.nlm.nih.gov/books/NBK7249/'


response = requests.get(url)
trs = BeautifulSoup(response.text, 'html.parser').find_all('tr')

countries = []

for tr in trs:
    tds = tr.find_all('td')
    if (len(tds) < 2):
        continue
    countries.append({
        'name': tds[0].text,
        'abbreviation': tds[1].text
    })
    countries.append({
        'name': tds[2].text,
        'abbreviation': tds[3].text
    })

with open('countries.json', 'w+', encoding='utf-8') as html_file:
    json.dump(countries, html_file)
