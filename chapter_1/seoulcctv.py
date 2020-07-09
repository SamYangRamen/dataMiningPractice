#-*- coding: utf-8 -*-

import pandas as pd

CCTV_seoul = pd.read_csv("CCTV_in_seoul.csv", encoding="cp949", thousands=',')

print(CCTV_seoul.head()) # 데이터의 첫 5행만 보여주기
print(CCTV_seoul.columns) # 데이터의 첫 행, 즉 제목들 보여주기

CCTV_seoul.rename(columns={CCTV_seoul.columns[0] : '구별'}, inplace=True)
# 0번째 열의 제목을 변경
# inplace=True : 실제 CCTV_seoul의 변수의 내용을 갱신하라는 메시지

print(CCTV_seoul.head())

pop_seoul = pd.read_csv("population_in_seoul.csv", encoding="cp949")
print(pop_seoul.head())

pop_seoul = pd.read_excel("population_in_seoul.xlsx",
                        header = 2,                 # 세 번째(2번째) 줄부터 읽어라
                        usecols = 'B, D, G, J, N',  # B, D, G, J, N번째 열만 읽어라
                        encoding="cp949")
print(pop_seoul.head())

pop_seoul.rename(columns={pop_seoul.columns[0] : '구별',
                         pop_seoul.columns[1] : '인구수',
                         pop_seoul.columns[2] : '한국인',
                         pop_seoul.columns[3] : '외국인',
                         pop_seoul.columns[4] : '고령자'}, inplace=True)   # 각 열의 제목을 변경
print(pop_seoul.head())

print(CCTV_seoul.sort_values(by="소계", ascending=True).head(5))  # 소계를 기준으로 오름차순 정렬한 뒤 앞 5행만 출력
print(CCTV_seoul.sort_values(by="소계", ascending=False).head(5)) # 소계를 기준으로 내림차순 정렬한 뒤 앞 5행만 출력


CCTV_seoul['최근증가율'] = (CCTV_seoul['2018년'] + CCTV_seoul['2017년'] + \
                           CCTV_seoul['2016년'] + CCTV_seoul['2015년'] + \
                           CCTV_seoul['2014년'] + CCTV_seoul['2013년'] + \
                           CCTV_seoul['2012년']) / CCTV_seoul['2011년 이전'] * 100
print(CCTV_seoul.sort_values(by='최근증가율', ascending=False).head())

print(pop_seoul.head())
pop_seoul.drop([0], inplace=True)   # 0행 삭제
print(pop_seoul.head())

print(pop_seoul['구별'].unique())   # 반복된 데이터는 하나로 나타내서 한 번 이상 나타난 데이터를 확인. 즉, set으로 만들어 출력

print(pop_seoul[pop_seoul['구별'].isnull()])  # NaN이 어디에 있는지 확인

pop_seoul['외국인비율'] = pop_seoul['외국인'] / pop_seoul['인구수'] * 100
pop_seoul['고령자비율'] = pop_seoul['고령자'] / pop_seoul['인구수'] * 100
print(pop_seoul[['구별', '외국인비율', '고령자비율']].head())

