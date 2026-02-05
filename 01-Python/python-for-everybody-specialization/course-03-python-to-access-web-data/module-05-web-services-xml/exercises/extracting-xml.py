import urllib.request
import xml.etree.ElementTree as ET

url = input('Enter URL: ')
print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved', len(data), 'characters') 

tree = ET.fromstring(data)
results = tree.findall('comments/comment')

count = 0
for result in results:
    count = count + int(result.find('count').text)

print('Count:', count)