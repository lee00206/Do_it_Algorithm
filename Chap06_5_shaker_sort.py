# 셰이커 정렬 알고리즘 구현하기
# 홀수 패스에서는 가장 작은 원소를 맨 앞으로 이동
# 짝수 패스에서는 가장 큰 원소를 맨 뒤로 이동

from typing import MutableSequence

def shaker_sort(a: MutableSequence) -> None:
    """셰이커 정렬"""
    left = 0
    right = len(a) - 1
    last = right
    while left < right:
        for j in range(right, left, -1):
            if a[j - 1] > a[j]:
                a[j - 1], a[j] = a[j], a[j - 1]
                last = j
        left = last

        for j in range(left, right):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                last = j
        right = last
