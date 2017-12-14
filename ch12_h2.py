import urllib
from BeautifulSoup import *

url = raw_input('Enter URL: ')
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)
span_comments = soup('span')

sum = 0

for numbers in span_comments:
    number = int(numbers.contents[0])
    sum = sum + number

print sum