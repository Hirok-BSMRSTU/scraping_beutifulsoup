from bs4 import BeautifulSoup 
import requests
from csv import writer

"""url = "https://www.pararius.com/apartments/amsterdam/page-2"
page = requests.get(url)


soup = BeautifulSoup(page.content, 'html.parser')

lists = soup.find_all('section', class_="listing-search-item")"""

with open('housing.csv', 'w', encoding = 'utf8', newline = '') as f:
    thewriter = writer(f)
    header = [ 'Title', 'Location', 'Price', 'Area']
    thewriter.writerow(header)
    url1 = "https://www.pararius.com/apartments/amsterdam/page-"
    url_sec = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20']
    for i in url_sec:
        url = url1 + i
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        lists = soup.find_all('section', class_="listing-search-item")

        for list in lists:
            title = list.find('a', class_="listing-search-item__link--title").text.replace('\n','')
            location = list.find('div', class_="listing-search-item__location").text.replace('\n','')
            price = list.find('div', class_="listing-search-item__price").text.replace('\n','')
            area = list.find('li', class_="illustrated-features__item--surface-area").text.replace('\n','')
            info = [title, location, price, area]
            thewriter.writerow(info)
