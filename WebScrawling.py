import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup

url="http://py4e-data.dr-chuck.net/known_by_Nazzera.html"
names=['1']
count=int(input())
position=int(input())
html=urllib.request.urlopen(url).read()
soup=BeautifulSoup(html,'html.parser')

tags=soup('a')

for i in range(count):
    url=tags[position-1].get('href',None)
    name=tags[position-1].contents[0]
    names.append(name)
    html=urllib.request.urlopen(url).read()
    soup=BeautifulSoup(html,'html.parser')
    tags=soup('a')
print(names[-1])
    