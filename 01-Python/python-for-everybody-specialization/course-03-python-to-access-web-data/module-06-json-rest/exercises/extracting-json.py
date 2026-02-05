import json
import urllib.request

url = input('Enter location: ')
print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved', len(data), 'characters') 

js = json.loads(data)

sum = 0
for item in js['comments']:
    sum = sum + int(item['count'])

print(sum)