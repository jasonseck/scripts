import requests
url = 'http://data.mtgox.com/api/2/BTCUSD/money/ticker'
r = requests.get(url, headers={'Accept': 'application/json'})
print r.json()['data']['avg']['display_short']
