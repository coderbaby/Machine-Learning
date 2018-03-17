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
    print(result)
    
