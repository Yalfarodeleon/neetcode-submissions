class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        result = count = 0 # Initialize result and count to zero

        for num in nums: # Iterate through the nums List array
            count += 1 if num else -count # This only changes count
            result = max(result, count) # get the result by getting the max of the count and result comparison
        return result