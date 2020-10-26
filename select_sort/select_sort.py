class Solution:
    def runningSum(self, nums):
        runningSum = []
        for i in range(0, len(nums)):
            temp_sum = 0
            for j in range(0, i+1):
                temp_sum = temp_sum + nums[j]
            runningSum.append(temp_sum)
        return runningSum


x = Solution()
print(x.runningSum([1, 2, 3, 4]))
