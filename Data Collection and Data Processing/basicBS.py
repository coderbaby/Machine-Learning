from bs4 import BeautifulSoup
import requests

#r = requests.get('https://pythonprogramming.net/parsememcparseface/')
#soup = BeautifulSoup(r.text,'lxml')

#print(soup.find_all('p'))
## Finding all the paragraph tags 
#for ps in soup.find_all('p'):
#    print(ps.get_text())

## Finding all the text from the soup
#print(soup.get_text())

## Find all the links
'''
for url in soup.find_all('a'):
    print(url.get('href'))
'''

## Finding all the links from the nav bar
'''
nav = soup.nav
for url in nav.find_all('a'):
    print(url.get('href'))
'''
'''
body = soup.body
for paragraph in body.find_all('p'):
    print(paragraph.text)
'''
'''
for div in soup.find_all('div',class_='body'):
    print(div.text)
'''
#table = soup.table == table = soup.find('table')
#table = soup.find('table')
#table_rows = table.find_all("tr")  # creates a list of tables rows
#print(table_rows)
'''
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text for i in td]
    print(row)

Alternatively you can also use pandas 

'''

'''
import pandas as pd
df = pd.read_html('https://pythonprogramming.net/parsememcparseface/', header = 0)
print(df)
'''
r = requests.get('https://pythonprogramming.net/sitemap.xml')
soup = BeautifulSoup(r.text,'xml')

for url in soup.find_all('loc'):
    print(url.text)
