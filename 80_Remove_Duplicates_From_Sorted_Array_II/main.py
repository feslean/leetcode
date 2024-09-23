from typing import List

class Solution:
    
    def count_nums(self, k, nums):
        total_count = 1
        actual_number = nums[k]
        k = k + 1
        while k < len(nums) and nums[k] == actual_number:  # Add bounds check
            total_count += 1
            k += 1
        return total_count

    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        actual_count = 0
        global_count = 0

        while True:
            # Bounds check to prevent index errors
            if k + global_count >= len(nums):
                break
            
            actual_number = nums[k + global_count]
            actual_count = self.count_nums(k + global_count, nums)  # Correct method call
            
            global_count += actual_count

            if actual_count >= 2:
                nums[k] = actual_number
                nums[k + 1] = actual_number
                k += 2
                global_count -= 2
            else:
                nums[k] = actual_number
                k += 1
                global_count -= 1
            
            print (k)

            # Adjusted bounds check
            if k + global_count >= len(nums):
                break

        return k
