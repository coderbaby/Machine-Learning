import pandas
import requests
from bs4 import BeautifulSoup


## get html page
r = requests.get("https://www.nytimes.com/interactive/2017/06/23/opinion/trumps-lies.html")
soup = BeautifulSoup(r.text,'html.parser')
results = soup.find_all('span', attrs = {'class':'short-desc'})

records = []
for result in results:
    print("=======")
    date = result.find('strong').text[0:-1] + ', 2017'
    lie = result.contents[1][1:-2]
    explanation = result.find('a').text[1:-1]
    url = result.find('a')['href']
    records.append((date, lie, explanation, url))

print(records)
    
