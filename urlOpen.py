import urllib.request
import json

url = 'https://samples.openweathermap.org/data/2.5/weather?q=London,uk&appid=b6907d289e10d714a6e88b30761fae22'
res = urllib.request.urlopen(url)
content = json.loads(res.read().decode('utf8'))
print(content)
print("aaaa")
print(1)