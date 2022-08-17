from cgi import print_directory
from cgitb import reset
import requests
import bs4


base_url = "http://books.toscrape.com/catalogue/page-"

list_of_req_book = []

for i in range(1, 51):
    current_url = base_url + f"{i}" + ".html"
    result = requests.get(f"{current_url}")
    soup = bs4.BeautifulSoup(result.text, 'lxml')
    list_book = soup.select(".product_pod")
    for x in list_book:
        if len(x.select(".star-rating.Two")) != 0:
            xx = x.select('a')[1]['title']
            list_of_req_book.append(xx)

for each in list_of_req_book:
    print(each)
