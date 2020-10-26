test = [5, 9, 0, 3, 2, 1, 4, 8, 7, 6, 24, 15, 84, -5]


def insertion_sort(nums):
    a = nums
    for j in range(1, len(a)):
        # a[j] 代表当前需要插入有序序列的数，a[0...i]为前i+1个已经排序号的有序序列
        key = a[j]
        i = j - 1
        # 将a[j]与前j个有序数依次比较大小，并找到合适的位置插入
        while i >= 0 and a[i] > key:
            a[i+1] = a[i]
            i = i - 1
            a[i+1] = key
        else:
            pass

    return a


print(insertion_sort(test))
