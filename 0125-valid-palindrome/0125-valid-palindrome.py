class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()

        is_palindrome = True

        left = 0
        right = len(s) - 1

        while left < right:
    
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1

            if s[left] == s[right]:
                 left += 1
                 right -= 1 
            else :
                is_palindrome = False
                break

        return is_palindrome