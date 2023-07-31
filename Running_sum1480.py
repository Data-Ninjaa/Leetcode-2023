#Leetcode problem 1480
#Running Sum of 1D Array
#method runnig_sum
def running_sum(nums):
    # loop to iterate from 2nd index of the nums list
    for i in range(1,len(nums)):
        #updating the nums list
        nums[i] = nums[i-1]+nums[i]
    #return the updated list
    return nums
nums = [1,2,3,4,5]
new_array = running_sum(nums)
print(new_array)
