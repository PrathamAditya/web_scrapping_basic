import re
import requests
import bs4


result = requests.get("https://en.wikipedia.org/wiki/Grace_Hopper")

soup = bs4.BeautifulSoup(result.text, 'lxml')

for every in soup.select('.toctext'):
    print(every.text)
