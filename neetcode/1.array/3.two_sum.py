def twoSum( nums, target):
    prevmap={}
    for i,n in enumerate(nums):
        diff=target-n
        if diff in prevmap:
            return [prevmap[diff],i]
        prevmap[n]=i

print(twoSum(nums = [2,7,11,15], target = 9))



















# class Solution(object):
#     def twoSum(self, nums, target):
#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return i, j
