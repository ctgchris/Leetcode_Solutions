class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        insert=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[insert], nums[i]= nums[i], nums[insert]
                insert+=1
        return nums