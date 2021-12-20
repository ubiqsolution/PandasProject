# COVID 19 Live Data Web Crawler
# Author: Si. Gi. Kim

# 웹크롤링시 크롬 시크릿모드 사용
# 크롤링 순서 상세하게 정리하기

import requests
from bs4 import BeautifulSoup

url = 'https://www.worldometers.info/coronavirus/'

response = requests.get(url)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    covid_data = soup.findAll('div', class_='maincounter-number')
    print('코로나19 확진자 수: ' + covid_data[0].text)
    print('코로나19 사망자 수: ' + covid_data[1].text)
    print('코로나19 완치자 수: ' + covid_data[2].text)
else : 
    print(response.status_code)
