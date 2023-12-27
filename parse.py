import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.binance.com/ru/markets/overview?p=1'
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

subtitle3_divs = soup.find_all('div', class_='subtitle3')
body2_divs = soup.find_all('div', class_='body2')

for i in range(len(subtitle3_divs)):
  subtitle3_divs[i]=subtitle3_divs[i].text.strip()
for i in range(len(body2_divs)):
  body2_divs[i]=body2_divs[i].text.strip()

data = {
    'Название': subtitle3_divs,
    'Цена': body2_divs[::4],
    'Изменение за 24 часа': body2_divs[1::4],
    'Объем': body2_divs[2::4],
    'Капитализация': body2_divs[3::4]
}

df = pd.DataFrame(data)
df.to_excel('data.xlsx', index=False)