from cgi import print_directory
from cgitb import reset
from enum import unique
import requests
import bs4


base_url = "http: // quotes.toscrape.com/page/"

list_of_quotes = []
list_of_author = set()
top_ten_tages = []
unique_author = set()


result = requests.get("http://quotes.toscrape.com/")
soup = bs4.BeautifulSoup(result.text, 'lxml')
list_book = soup.select(".quote")
for x in list_book:
    quote = x.select('.text')
    author = x.select('span')
    list_of_quotes.append(quote[0].text[2:-2:1])
    list_of_author.add(author[1].text[3:-8:1].strip('\n'))

    # list_of_author.append(author.text)
    # xx = xx.va
    # list_of_req_book.extend(xx)
top_ten = soup.find_all('div', {"class": "col-md-4 tags-box"})

# span_only = top_ten['span']
# print(top_ten.select('span'))

# t_1 = True
# page_number = 1
# while t_1:
#     result = requests.get(f"{base_url}" + f"{page_number}/")
#     soup = bs4.BeautifulSoup(result.text, 'lxml')
#     list_book = soup.select(".quote")
#     author = x.select('span')
#     unique_author.add(author[1].text[3:-8:1].strip('\n'))
#     page_number += 1
