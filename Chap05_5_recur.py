# 스택으로 재귀 함수 구현하기(재귀를 제거)

"""
원래의 recur 함수:
def recur(n: int) -> int:
    while n > 0:
        recur(n - 1)    **
        print(n)
        n = n - 2

 ** 이 부분을 제거하기 위해서는 현재의 n값을 임시로 저장할 필요가 있음.
 또한 recur(n-1)의 처리를 완료하고 n값을 출력할 때 임시로 저장했던 n을 꺼내 그 값을 출력해야함.
 이러한 문제를 스택으로 해결
"""
from Chap04_4_stack import Stack

def recur(n: int) -> int:
    """재귀를 제거한 recur() 함수"""
    s = Stack(n)

    while True:
        if n > 0:
            s.push(n)           # n값을 푸시
            n = n - 1
            continue
        if not s.is_empty():    # 스택이 비어 있지 않으면
            n = s.pop()         # 저장한 값을 n에 팝
            print(n)
            n = n - 2
            continue
        break

x = int(input('정숫값을 입력하세요: '))

recur(x)