class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        numset = set(nums)
        for num in numset:
            if (num-1) not in numset:
                length = 1
                for i in range(len(numset)+1):
                    if num + length in numset:
                        length += 1
                longest = max(length, longest)
        return longest
        