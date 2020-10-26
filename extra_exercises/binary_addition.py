"""
考虑吧两个 n 位二进制整数加起来的问题，这两个整数分别存储在两个二元数组 A 和 B 中.
这两个整数的和应该按二进制形式存储在一个 (n+1) 元数组中.请给出该算法的代码描述.
"""
test_1 = [0, 1, 1, 1, 1, 1, 1, 1, 1, 0]
test_2 = [1, 0, 1, 0, 0, 0, 1, 1, 1, 0]


# 注意：算法1默认左边为低位，右边为高位
def binary_addition_1(A, B):
    carry = 0
    sums = [0] * (len(A) + 1)
    for j in range(0, len(A)):
        if A[j] + B[j] + carry == 0:
            carry = 0
            sums[j] = 0
        elif A[j] + B[j] + carry == 1:
            carry = 0
            sums[j] = 1
        elif A[j] + B[j] + carry == 2:
            carry = 1
            sums[j] = 0
        else:
            carry = 1
            sums[j] = 1

    if carry == 1:
        sums[len(A)] = 1
    else:
        sums[len(A)] = 0
    return sums


# 注意：算法2默认右边为低位，左边为高位
def binary_addition_2(A, B):
    carry = 0
    sums = [0] * (len(A) + 1)
    for j in range(len(A)-1, -1, -1):
        if A[j] + B[j] + carry == 0:
            carry = 0
            sums[j+1] = 0
        elif A[j] + B[j] + carry == 1:
            carry = 0
            sums[j+1] = 1
        elif A[j] + B[j] + carry == 2:
            carry = 1
            sums[j+1] = 0
        else:
            carry = 1
            sums[j+1] = 1

    if carry == 1:
        sums[0] = 1
    else:
        sums[0] = 0
    return sums


print(test_1)
print(test_2)
print(binary_addition_1(test_1, test_2))
print(binary_addition_2(test_1, test_2))
