import requests

# Proxy configuration
proxy = {
    'http': '   ',
    'https': '80.63.84.58:8081'
}

proxies_by_country = {
    'dk': {
        'name': 'Denmark',
        'ip': '80.63.84.58:8081',
    },
    'us': {
        'name': 'America',
        'ip': '202.5.16.44:80'
    },
    'cn': {
        'name': 'China',
        'ip': '223.247.141.77:80'
    },
    'ca': {
        'name': 'Canada',
        'ip': '159.203.61.169:3128'
    },
}

# URL to make the request to
url = 'https://www.google.com/search?q=iphone+13&hl=en&gl=DK&start=0&near=Denmark&filter=0'

# Make the request using the proxy
response = requests.get(url, proxies=proxy)

# Process the response
with open('response.html', 'w') as f:
    f.write(response.text)
