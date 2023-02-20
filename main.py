import requests
from bs4 import BeautifulSoup
import pandas as pd
prodData = []

for i in range(1,10):
    url = f'https://www.jumia.com.ng/mens-watches/?page={i}#catalog-listing'
    res = requests.get(url).text
    soup = BeautifulSoup(res, 'lxml')
    # print(soup.prettify())
    watch_div = soup.find_all('a', class_="core")
    watchName = soup.find_all('div', class_="info")
    for info in watchName:
        title = info.find("h3").text
        price = info.find('div', class_= 'prc').text
        
        prodData.append([title, price])
df = pd.DataFrame(prodData, columns=['title', 'price'])
df.to_csv('prodData.csv')
print("success")
