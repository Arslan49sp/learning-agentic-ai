import urllib.request
from bs4 import BeautifulSoup

url = input("Enter URL: ")
html = urllib.request.urlopen(url).read()
# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Find all 'span' tags in the parsed HTML
tags = soup('span')
total = 0
# Iterate through each 'span' tag found
for tag in tags:
    num = tag.string
    value = int(num)
    total += value
print(total)