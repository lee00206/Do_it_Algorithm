# 뮤터블 시퀀스 원소를 역순으로 정렬

from typing import Any, MutableSequence

def reverse_array(a: MutableSequence) -> None:
    # 뮤터블 시퀀스 a의 원소를 역순으로 정렬
    n = len(a)
    for i in range(n // 2):
        a[i], a[n - i - 1] = a[n - i - 1], a[i]

if __name__ == '__main__':
    print('배열 원소를 역순으로 정렬합니다.')
    nx = int(input('원소 수를 입력하세요: '))
    x = [None] * nx # 원소 수가 nx인 리스트를 생성

    for i in range(nx):
        x[i] = int(input(f'x[{i}]값을 입력하세요: '))

    reverse_array(x) # x를 역순으로 정렬

    print('배열 원소를 역순으로 정렬했습니다.')
    for i in range(nx):
        print(f'x[{i}] = {x[i]}')

"""
더 간단한 방법으로 reverse 함수를 쓰는 것도 있음
x.reverse()   리스트 x의 원소를 역순으로 정렬
y = list(reversed(x))   리스트 x의 원소를 역순으로 정렬하여 y에 대입
"""