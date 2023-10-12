import requests
from bs4 import BeautifulSoup
import json
import re
import base64


proxies = {}
countries = []
# get countries from countries.json
with open('countries.json', 'r', encoding='utf-8') as html_file:
    countries = json.load(html_file)


for country in countries:
    try:
        print(
            f'http://free-proxy.cz/en/proxylist/country/{country.get("abbreviation")}/all/ping/all')
        response = requests.get(
            f'http://free-proxy.cz/en/proxylist/country/{country.get("abbreviation")}/all/ping/all')
        with open(f'./html/{country.get("abbreviation")}.html', 'w+', encoding='utf-8') as html_file:
            html_file.write(response.text)
        soup = BeautifulSoup(response.text, 'html.parser')
        for tr in soup.find_all('tr')[1:]:
            tds = tr.find_all('td')
            print(len(tds))
            if (len(tds) < 2):
                continue
            ip_script = tds[0].find('script').text
            regex_pattern = r'"([^"]*)"'
            matches = re.findall(regex_pattern, ip_script)
            ip = base64.b64decode(matches[0]).decode('utf-8')
            if (proxies.get(country.get("abbreviation")) == None):
                proxies[country.get("abbreviation")] = []

            proxies[country.get("abbreviation")].append({
                'ip': ip,
                'port': tds[1].text,
                'protocol': tds[2].text,
                'country': tds[3].text,
                'region': tds[4].text,
                'city': tds[5].text,
                'anonymity': tds[6].text,
                'speed': tds[7].text,
                'uptime': tds[8].text,
                'response': tds[9].text,
                'last_checked': tds[10].text
            })
    except Exception as e:
        print(e)
        continue

with open('proxies_by_c.json', 'w+', encoding='utf-8') as html_file:
    json.dump(proxies, html_file)
