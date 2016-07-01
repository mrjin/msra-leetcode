class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        rob = 0
        not_rob = 0
        for i in nums:
            temp = max(rob, not_rob)
            rob = not_rob + i
            not_rob = temp
        return max(rob, not_rob)