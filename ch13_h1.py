import urllib
import xml.etree.ElementTree as ET

url = raw_input('Enter URL: ')

data = urllib.urlopen(url).read()
print 'Retrieved',len(data),'characters'
print data
tree = ET.fromstring(data)

sum = 0

comments = tree.findall('comments/comment')
for counts in comments:
    number = counts.find('count').text
    num = int(number)
    sum = num + sum

print sum