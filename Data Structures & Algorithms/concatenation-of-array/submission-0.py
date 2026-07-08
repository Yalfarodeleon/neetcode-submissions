class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [] # Create an array
        for i in range(2): # Asks for array of length 2n, if wanted 3 or x could change in the future
            for n in nums: 
                ans.append(n) # Appends the copied values to the end of the new answ array
        return ans