# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

"""
pandas에는 크게 Series와 DataFrame이라는 두 종류의 자료구조가 있음
Series는 1차원 배열과 같은 자료구조
DataFrame은 2차원 배열과 같은 자료구조
date_range는 날짜형 데이터
"""

s = pd.Series([1,3,5,np.nan,6,8])
print(s)

dates = pd.date_range('20200709', periods=8) # 기본 날짜로부터 8일간을 지정한 것
print(dates)

df = pd.DataFrame(np.random.randn(8,4),         # 6행 4열의 랜덤 변수 생성
                  index=dates,                  # index를 기본 index(즉 0~5)가 아닌 직접 지정한 것으로 변경
                  columns=['A','B','C','D'])    # column 이름을 직접 지정한 것으로 변경
print(df)
print(df.head(3)) # 괄호 안에 정수 N이 있으면 첫 N행을 출력, 괄호 안에 값이 없으면 첫 5행을 출력

print(df.index)
print(df.columns)
print(df.values)
print(df.info())     # 생성한 DataFrame의 메타 정보를 출력
print(df.describe()) # 통계적 개요 출력

df = df.sort_values(by='B', ascending=True)    # B열 기준으로 오름차순 정렬
print(df)
df = df.sort_values(by='A', ascending=False)     # A열 기준으로 내림차순 정렬
print(df)

print(df['A'])  # A열 출력
print(df.A)
print(df[3:6])  # 3~5행 출력
print(df['20200711':'20200713'])                 # 실제 index를 통해 해당 행 출력

"""
loc : 특정 날짜의 데이터를 확인하고 싶을 때 사용하는 옵션
iloc : 행과 열의 번호를 이용해서 데이터에 바로 접근하고 싶을 때 사용하는 옵션
"""

print(df.loc[:,['A','B']])                       # A, B열의 모든 행 출력
print(df.loc['20200711':'20200713',['A','B']])   # A, B열의 해당 행 출력
print(df.loc['20200711',['A','B']])              # A, B열의 해당 행 출력
print(df.loc[dates[0], 'A'])                     # 해당 데이터 출력
print(df.iloc[3])               # 3행 출력
print(df.iloc[0:3])             # 0~2행 출력
print(df.iloc[3:5, 1:3])        # 3~4행 && 1~2열 출력
print(df.iloc[[1,2,4], [0,2]])  # 1,2,4행 && 0,2열 출력
print(df.iloc[1:4, :])          # 1~3행 && 전체열 출력

print(df[df.A > 0]) # A열의 데이터 중 0보다 큰 데이터에 해당하는 행들만 출력
print(df[df['A'] > 0])
print(df[df > 0])   # 데이터 전체에 조건을 걸었을 경우, 만족하지 않은 부분은 NaN으로 처리됨

"""
DataFrame의 복사 방법
그냥 = 기호를 쓰면 데이터 위치만 복사가 됨
따라서 .copy() 함수를 사용하여 깊은 복사를 수행해야 함
"""

df2 = df.copy()

df2['E'] = ['one', 'one', 'two', 'three', 'four', 'three', 'five', 'four'] # 새로운 열을 추가
print(df2)

print(df2.E.isin(['two', 'four'])) # E열에서 two 또는 four가 있는지 확인(True False로 표시됨)

print(df.apply(np.cumsum))                      # 누적합 표시
print(df.apply(lambda x: x.max() - x.min()))    # 최대값과 최소값의 차이

# ------------------------------------------------------------------------------------------

df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                    'B': ['B0', 'B1', 'B2', 'B3'],
                    'C': ['C0', 'C1', 'C2', 'C3'],
                    'D': ['D0', 'D1', 'D2', 'D3']},
                   index=[0, 1, 2, 3])

df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                    'B': ['B4', 'B5', 'B6', 'B7'],
                    'C': ['C4', 'C5', 'C6', 'C7'],
                    'D': ['D4', 'D5', 'D6', 'D7']},
                   index=[4, 5, 6, 7])

df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],
                    'B': ['B8', 'B9', 'B10', 'B11'],
                    'C': ['C8', 'C9', 'C10', 'C11'],
                    'D': ['D8', 'D9', 'D10', 'D11']},
                   index=[8, 9, 10, 11])

result = pd.concat([df1, df2, df3]) # DataFrame들을 열방향으로 단순히 합치기
print(result)

result = pd.concat([df1, df2, df3], keys=['x', 'y', 'z'])   # concat 하기 전 각각의 DataFrame마다 key값을 붙여 level 형성
print(result)