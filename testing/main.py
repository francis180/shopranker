import requests
url = 'https://api.jsonbin.io/v3/b/65085498619a313eb304525c/meta/privacy'
headers = {
  'X-Bin-Private': 'false',
  'X-Master-Key': '$2b$10$eqxfDt1/np8b8TxQl2rHPe38D9ielV2S6Z6Xmnlc86.zKmtfk3ZR.'
}
data = {}

req = requests.put(url, json=data, headers=headers)
print(req.text)