class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_string = ''
        for i in range(len(s)):
            if s[i].isalnum():
                new_string += s[i].lower()
        reversed_string = new_string[::-1]
        
        if new_string == reversed_string:
            return True
        return False
        