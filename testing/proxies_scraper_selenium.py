from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import json
import re
import base64


proxies = {}
countries = []

# Get countries from countries.json
with open('countries.json', 'r', encoding='utf-8') as html_file:
    countries = json.load(html_file)
PROXY = "11.456.448.110:8080"
# Configure Selenium
options = webdriver.ChromeOptions()
options.add_argument('--proxy-server=%s' % PROXY)
# options.add_argument("--headless")  # Run Chrome in headless mode
driver = webdriver.Chrome(options=options)

for country in countries:
    try:
        url = f'http://free-proxy.cz/en/proxylist/country/{country.get("abbreviation")}/all/ping/all'
        print(url)

        # Fetch page using Selenium
        driver.get(url)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, 'tr')))
        response = driver.page_source

        # Save HTML file
        with open(f'./html/{country.get("abbreviation")}.html', 'w+', encoding='utf-8') as html_file:
            html_file.write(response)

        # Parse HTML with BeautifulSoup
        soup = BeautifulSoup(response, 'html.parser')
        for tr in soup.find_all('tr')[1:]:
            tds = tr.find_all('td')
            print(len(tds))
            if len(tds) < 2:
                continue
            ip_script = tds[0].find('script').text
            regex_pattern = r'"([^"]*)"'
            matches = re.findall(regex_pattern, ip_script)
            ip = base64.b64decode(matches[0]).decode('utf-8')
            if country.get("abbreviation") not in proxies:
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

# Quit Selenium driver
driver.quit()

# Save proxies as JSON
with open('proxies_by_c.json', 'w+', encoding='utf-8') as html_file:
    json.dump(proxies, html_file)
