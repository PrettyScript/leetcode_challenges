'''
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

'''

'''
Constraint Questions
1. Are the elements sorted? That doesn't matter.
2. Can the entire array only consist of zeros
'''

class Solution:
    def moveZeroes(self, nums: list) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # output = []
        # n = len(nums)
        
        # for i in range(0, n):
        #     if nums[i] != 0:
        #         output.append(nums[i])
                
        # m = len(output)
        
        # for i in range(m, n):
        #     output.append(0)
            
        # print(output)
        pointer = 0
        n = len(nums)
        for num in nums:
            if num != 0:
                nums[pointer] = num
                pointer += 1
                
        for x in range(pointer, n):
            nums[x] = 0
            
        print(nums)
            
solution = Solution()
solution.moveZeroes(nums=[0,1,0,3,12])