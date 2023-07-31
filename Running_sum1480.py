#Leetcode problem 1480
#Running Sum of 1D Array
def running_sum(nums):
    for i in range(1,len(nums)):
        nums[i] = nums[i-1]+nums[i]
    return nums
def runningSum(nums):
    n = len(nums)
    result = [0] * n
    result[0] = nums[0]
    for i in range(1, n):
        result[i] = result[i-1] + nums[i]
    return result

nums = [1,2,3,4,5]
new_array = runningSum(nums)
print(new_array)