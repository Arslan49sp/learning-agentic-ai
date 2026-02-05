import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup


# User Inputs
url = input('Enter URL: ')
count = int(input('Enter count: '))
position = int(input('Enter position: '))

print('Retrieving:', url)

# Repeat the process 'count' times
for i in range(count):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    
    # Retrieve all anchor tags
    tags = soup('a')
    
    # Find the tag at the specific position 
    target_tag = tags[position - 1]
    url = target_tag.get('href', None)
    
    print('Retrieving:', url)

# The result is the text within the last tag found
print('Last Name:', target_tag.contents[0])