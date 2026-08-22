class Solution():
    nums = [3,2,4]
    target = 6

    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    def twoSum(self ,nums, target):

        seen = {}
        for i in range(0 , len(nums)):
            need = target - nums[i]
            if need in seen:
                return [seen[need] , i]

            seen[nums[i]] = i
        return[]
    