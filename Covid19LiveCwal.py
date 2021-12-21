# COVID 19 Live Data Web Crawler
# Author: Si. Gi. Kim

# 웹크롤링시 크롬 *시크릿모드 사용
# 크롤링 순서 상세하게 정리하기

import requests
from bs4 import BeautifulSoup

def worldcovid():
    url = 'https://www.worldometers.info/coronavirus/'

    # User Agent 설정
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}

    response = requests.get(url, headers = headers)

    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        covid_data = soup.findAll('div', class_='maincounter-number')
        
        print('-전세계 코로나19 DATA-')
        print('코로나19 확진자 수: ' + covid_data[0].text + '명')
        print('코로나19 사망자 수: ' + covid_data[1].text + '명')
        print('코로나19 완치자 수: ' + covid_data[2].text + '명')
        print('')
        
    else : 
        print('Error Code: ' + response.status_code)

def localcovid():
    # 코로나19 현황 시작
    covid_url = 'http://ncov.mohw.go.kr/bdBoardList_Real.do' #코로나19 현황 확인 웹주소

    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'}
    covid_url_request = requests.get(covid_url, headers=headers) #코로나19 현황 웹주소 requests화
    
    if covid_url_request.status_code == 200: # 응답코드가 200일때
        covid_html = covid_url_request.text # 해당 사이트 html text화
        covid_soup = BeautifulSoup(covid_html, 'html.parser')
        
                
        print('-국내 코로나19 DATA-')
        covid_confirmed_day = covid_soup.select_one('#content > div > h5:nth-child(4) > span.t_date') # 기준 날짜
        covid_confirmed_day_txt = covid_confirmed_day.get_text() # 텍스트화
        print('기준 날짜: ' + covid_confirmed_day_txt) # 기준 날짜 출력
        
        covid_confirmed_eve = covid_soup.select_one('#content > div > div:nth-child(14) > table > tbody > tr:nth-child(1) > td:nth-child(7)') # 전일 코로나 확진자 웹크롤링
        covid_confirmed_eve_txt = covid_confirmed_eve.get_text() # 텍스트화
        print('전일 코로나 확진자 수 : ' + covid_confirmed_eve_txt + '명')  # 전일 코로나 확진자수 출력
    
        covid_confirmed = covid_soup.select_one('#content > div > div.caseTable > div:nth-child(4) > ul > li:nth-child(1) > dl > dd') # 금일 코로나 확진자 웹크롤링하는거
        covid_confirmed_txt = covid_confirmed.get_text() # 텍스트화
        print('금일 코로나 확진자 수 : ' + covid_confirmed_txt + '명') # 금일 코로나 확진자수 출력
    
        covid_confirmed_reverge = covid_soup.select_one('#content > div > div:nth-child(14) > table > tbody > tr:nth-child(1) > td:nth-child(9)') # 주간 일평균 코로나 확진자 웹크롤링하는거
        covid_confirmed_reverge_txt = covid_confirmed_reverge.get_text() # 텍스트화
        print('주간 일평균 코로나 확진자 수 : ' + covid_confirmed_reverge_txt + '명') # 주간 일평균 코로나 확진자수 출력
        print('')
    
    else :
        print(covid_url_request.status_code)

worldcovid()
localcovid()