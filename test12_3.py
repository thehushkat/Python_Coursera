import urllib
from BeautifulSoup import *

url = raw_input('Enter URL: ')

# Tells you what to do seven times (iteration)
for i in range(7):
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)

# These are items we'll use later
    links = soup('a')
    position = []

# This part takes the link position, prints it, and finds the same link position for the iteration
    for link in links:
        name = link.get('href', None)
        position.append(name)
    print position[17]
    url = position[17]