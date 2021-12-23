# COVID 19 Live Data Web Crawler
# Author: Si. Gi. Kim

# 웹크롤링시 크롬 *시크릿모드 사용
# 크롤링 순서 상세하게 정리하기
# 나도코딩 웹크롤링 강좌 참고

import re
import requests
from bs4 import BeautifulSoup

def create_soup(url):
    # User Agent 설정
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}
    res = requests.get(url, headers=headers)
    res.raise_for_status() # Status_code 200 인지 확인 후 에러 발생시 에러 출력 후 종료
    soup = BeautifulSoup(res.text, "lxml")
    return soup

def worldcovid():
    print('[전세계 코로나19 Live DATA]')
    url = 'https://www.worldometers.info/coronavirus/'
    soup = create_soup(url)
    
    covid_data = soup.findAll('div', class_='maincounter-number')
    covid_date= soup.find('div', style='font-size:13px; color:#999; margin-top:5px; text-align:center').text
    
    covid_data_strip = covid_data[0].text.strip() # 텍스트화(안하면 줄바꿈 처리됨)
    covid_data_strip_1 = covid_data[1].text.strip()
    covid_data_strip_2 = covid_data[2].text.strip()
    
    print('기준날짜: ' + covid_date)
    print('코로나19 확진자 수: ' + covid_data_strip + '명')
    print('코로나19 사망자 수: ' + covid_data_strip_1 + '명')
    print('코로나19 완치자 수: ' + covid_data_strip_2 + '명')
    print('')

def localcovid():
    print('[국내 코로나19 Live DATA]')
    covid_url = 'http://ncov.mohw.go.kr/bdBoardList_Real.do' #코로나19 현황 확인 웹주소
    soup = create_soup(covid_url)
                
    covid_confirmed_day = soup.select_one('#content > div > h5:nth-child(4) > span.t_date') # 기준 날짜
    covid_confirmed_day_txt = covid_confirmed_day.get_text() # 텍스트화
    print('기준 날짜: ' + covid_confirmed_day_txt) # 기준 날짜 출력
    
    covid_confirmed_eve = soup.select_one('#content > div > div:nth-child(14) > table > tbody > tr:nth-child(1) > td:nth-child(7)') # 전일 코로나 확진자 웹크롤링
    covid_confirmed_eve_txt = covid_confirmed_eve.get_text() # 텍스트화
    print('전일 코로나 확진자 수 : ' + covid_confirmed_eve_txt + '명')  # 전일 코로나 확진자수 출력

    covid_confirmed = soup.select_one('#content > div > div.caseTable > div:nth-child(4) > ul > li:nth-child(1) > dl > dd') # 금일 코로나 확진자 웹크롤링하는거
    covid_confirmed_txt = covid_confirmed.get_text() # 텍스트화
    print('금일 코로나 확진자 수 : ' + covid_confirmed_txt + '명') # 금일 코로나 확진자수 출력

    covid_confirmed_reverge = soup.select_one('#content > div > div:nth-child(14) > table > tbody > tr:nth-child(1) > td:nth-child(9)') # 주간 일평균 코로나 확진자 웹크롤링하는거
    covid_confirmed_reverge_txt = covid_confirmed_reverge.get_text() # 텍스트화
    print('주간 일평균 코로나 확진자 수 : ' + covid_confirmed_reverge_txt + '명') # 주간 일평균 코로나 확진자수 출력
    print('')

worldcovid()
localcovid()