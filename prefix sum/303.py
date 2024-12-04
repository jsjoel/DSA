class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        c=0
        for i in range(left,right+1):
            c+=self.nums[i]
        return c
        

# Leetcode method
# class NumArray(object):

#     def __init__(self, nums):
#         """
#         :type nums: List[int]
#         """
#         self.presum = nums
#         for i in range(len(nums)-1):
#             self.presum[i+1] += self.presum[i]
        

#     def sumRange(self, left, right):
#         """
#         :type left: int
#         :type right: int
#         :rtype: int
#         """
#         if left == 0 : return self.presum[right]
#         return self.presum[right] - self.presum[left-1]





















# # Your NumArray object will be instantiated and called as such:
# nums = [-2,0,3,-5,2,-1]
# left,right = 0,2
# left,right = 2,5
# # left,right = 0,5
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
# print(param_1)