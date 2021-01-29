# seq_search() 함수를 사용하여 실수 검색하기
from typing import Any, Sequence

def seq_search(a: Sequence, key: Any) -> int:
    """시퀀스 a에서 key와 값이 같은 원소를 선형 검색(while문)"""
    i = 0

    while True:
        if i == len(a):
            return -1   # 검색에 실패하여 -1을 반환
        if a[i] == key:
            return i    # 검색에 성공하여 현재 검사한 배열의 인덱스를 반환
        i += 1

print('실수를 검색합니다.')
print('주의: "End"를 입력하면 종료합니다.')

number = 0
x = []

while True:
    s = input(f'x[{number}]: ')
    if s == 'End':
        break
    x.append(float(s))
    number += 1

ky = float(input('검색할 값을 입력하세요: '))

idx = seq_search(x, ky)
if idx == -1:
    print('검색값을 갖는 원소가 존재하지 않습니다.')
else:
    print(f'검색값은 x[{idx}]에 있습니다.')
