class Solution:
    def hasDuplicate(self, num: List[int]) -> bool:
        num.sort()
        for i in range(1,len(num)):
            if num [i] == num [i-1]:
                return True
        return False
        