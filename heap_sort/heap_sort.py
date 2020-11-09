from typing import List
import math

test = [5, 9, 0, 3, 2, 1, 4, 8, 7, 6, 24, 15, 84, -5]


def max_heapify(A: List, i):
    left = i << 1
    right = i << 1 + 1
    large = i
    if left < heap_size and A[left] > A[large]:
        large = left
    if right < heap_size and A[right] > A[large]:
        large = right
    if large != i:
        max_heapify(A, large)


def build_max_heap(A: List):
    global heap_size
    heap_size = len(A)
    for i in range(math.floor(len(A)/2), 1, -1):
        max_heapify(A, i)


def heap_sort(A: List):
    build_max_heap(A)
    for i in range(len(A), 2, -1):
        temp = A[i]
        A[i] = A[1]
        A[1] = temp
        A.heap_size = A.heap_size - 1
        max_heapify(A, 1)


print(heap_sort(test))
