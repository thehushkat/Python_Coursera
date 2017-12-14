import urllib
import json

url = raw_input('Enter URL: ')

data = urllib.urlopen(url).read()
info = json.loads(data)

total_counts = 0
for i in info['comments']:
    numbers = i['count']
    total_counts = total_counts + numbers

print total_counts