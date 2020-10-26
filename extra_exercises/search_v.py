"""
考虑以下查找问题：
输入：n个数的一个序列 A=<a1,a2,...,an>和一个值 v
输出：下标 i 使得 v=A[i] 或者当 v 不在 A 中出现时，v 为特殊值 NIL.
"""
test = [5, 9, 0, 3, 2, 1, 4, 8, 7, 6, 24, 15, 84, -5]


def search_v(nums, v):
    for i in range(0, len(nums)):
        if nums[i] == v:
            return i+1
        else:
            pass
    return "NIL"


print(search_v(test, 5))
print(search_v(test, 84))
print(search_v(test, -1))
print(search_v(test, 17))
