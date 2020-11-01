"""
 时间复杂度为：O(nlogn)
 代价是需要额外的内存空间
"""
def mergeSort(arr):
    import math
    result = []
    if len(arr) < 2:
        return arr
    middle = math.floor(len(arr)/2)
    left, right = arr[0:middle], arr[middle:]
    # 递归方法
    result = merge(mergeSort(left), mergeSort(right))
    return result


# 合并函数
def merge(left, right):
    result = []
    while left and right:
        if left[0] <= right[0]:
            # 弹出列表中的第一个元素
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    while left:
        result.append(left.pop(0))
    while right:
        result.append(right.pop(0))
    return result


# 插入排序与归并排序的结合
# 虽然归并排序在最坏情况运行时间为 O(nlogn)，而插入排序的最坏运行时间为 O(n^2)
# 但是插入排序中的常量因子可能使得它在n较小时，在许多机器上运行更快
# 所以，在归并排序中，当子问题变得足够小时，采用插入排序来使得递归的叶变粗时有意义的
def merge_insertion_sort(arr):
    import math
    result = []
    if len(arr) < 2:
        return arr
    if len(arr) == 2:
        return insertion_sort(arr)
    middle = math.floor(len(arr)/2)
    left, right = arr[0:middle], arr[middle:]
    return merge(merge_insertion_sort(left), merge_insertion_sort(right))


def insertion_sort(arr):
    if len(arr) < 2:
        return arr
    for i in range(1, len(arr)):
        j = i - 1
        while arr[j] > arr[i] and j >= 0:
            key = arr[j]
            arr[j] = arr[i]
            arr[i] = key
            j -= 1
            i -= 1
    return arr


print(insertion_sort([5,0,1,9,3,2,7,4,6]))
print(merge_insertion_sort([0,3,2,6,5,9,8,7,4,1,15,11,13,12,14]))
