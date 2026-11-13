class Solution:
    def isPalindrome(self, s: str) -> bool:
        palin = []
        for i in s:
            if i.isalnum():
                palin.append(i.lower())
        strs = "".join(palin)
        if strs == strs[::-1]:
            return True
        else:
            return False

                

        