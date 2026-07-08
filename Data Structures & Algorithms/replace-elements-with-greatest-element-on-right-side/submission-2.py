class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # Initialize the greatest value seen so far.
        # The problem requires the very last element to be replaced by -1.
        rightMax = -1

        # Traverse the array backwards (from the last index to 0).
        # range parameters: (start_index, stop_index_exclusive, step)
        for i in range(len(arr)-1, -1, -1):

            # 1. Calculate the NEW maximum before we overwrite the current element.
            # It is either the biggest number we've seen to the right, or the current number itself.
            newMax = max(rightMax, arr[i])

            # 2. Overwrite the current element with the greatest value found to its right.
            arr[i] = rightMax

            # 3. Update rightMax so it is ready for the next iteration ( the next element to the left).
            rightMax = newMax
        return arr
        