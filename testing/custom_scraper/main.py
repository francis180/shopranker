import requests
import urllib
import pandas as pd
from requests_html import HTML
from requests_html import HTMLSession

proxy = {
    "http": "http://10.10.1.10:3128",
    "https": "http://10.10.1.10:1080",
}


def get_source(url):
    try:
        session = HTMLSession()
        response = session.get(url, proxies=proxy)
        return response

    except requests.exceptions.RequestException as e:
        print(e)


def scrape_google(query):

    query = urllib.parse.quote_plus(query)
    response = get_source("https://www.google.com/search?q=" + query)
    with open('response.html', 'w', encoding='utf-8') as f:
        f.write(str(response.html.raw_html.decode()))
    return response


scrape_google("what is my ip")
