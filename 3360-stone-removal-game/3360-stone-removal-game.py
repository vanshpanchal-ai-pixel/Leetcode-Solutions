class Solution(object):
    def canAliceWin(self, n):
        """
        :type n: int
        :rtype: bool
        """
        turns = 0
        remove = 10 

        while n >= remove:
            n -= remove
            remove -= 1
            turns += 1

        return turns % 2 != 0