class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        
        rev = 0
        x1 = x
        while x1 > 0:
            rem = x1 % 10
            rev = rev * 10 + rem
            x1 = x1//10

        
        return rev == x


        