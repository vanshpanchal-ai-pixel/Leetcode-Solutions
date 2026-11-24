class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        threshold = len(nums) // 2

        for key, value in freq.items():
            if value > threshold:
                return key