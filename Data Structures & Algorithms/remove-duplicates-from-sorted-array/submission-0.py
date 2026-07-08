class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        write_ptr = 1
        for read_ptr in range(1, len(nums)):
            # Logic to check if nums[read_ptr] is a new unique element
            if nums[read_ptr] != nums[read_ptr - 1]:
                # Move the unique element forward
                nums[write_ptr] = nums[read_ptr]
                write_ptr += 1
        return write_ptr