import requests
import bs4

result = requests.get(
    "https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)")

soup = bs4.BeautifulSoup(result.text, 'lxml')

x = 0
for image in soup.select('.thumbimage'):

    ext_of_image = image['src'][-3] + image['src'][-2] + image['src'][-1]

    img_link = requests.get("https:"+f"{image['src']}")
    img_path = f'my_img_{x}gg' + f'.{ext_of_image}'
    f = open(img_path, 'wb')
    f.write(img_link.content)
    f.close()

    x += 1
