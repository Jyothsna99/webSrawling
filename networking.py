import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = input('Enter location: ')


print('Retrieving', url)
uh = urllib.request.urlopen(url)

data = uh.read()
print('Retrieved', len(data), 'characters')
print(data.decode())
tree = ET.fromstring(data)

results = tree.findall('comments/comment/count')
tot=0
for count in results:
    tot+=int(count.text)
print(tot)
    

   