class Solution:
    def canJump(self, nums: List[int]) -> bool:
        zero_array = [0] * len(nums)
        zidx = 0
        total_len = len(nums)
        total_nums = 0

        if(nums[0] == 0 and total_len > 1):
            return False
        
        if(total_len == 1):
            return True
        
        for i in range(0,total_len):
            if(nums[i] == 0 and i < total_len - 1):
                zero_array[zidx] = i
                zidx += 1
            else:
                total_nums += nums[i]
        
        if(total_nums < total_len - 1):
            return False
        
        j = 1
        jumps = 0
        broke = False

        for i in range (0,zidx):
            if (zero_array[i] != 0):
                zero_idx = zero_array[i]
                while zero_idx - j >= 0:
                    if (zero_idx - j + nums[zero_idx - j] > zero_idx):
                        jumps += 1
                        j = 1
                        broke = True
                        break
                    j += 1
                if broke == False:
                    return False
                broke = False
        if jumps != zidx:
            return False

        else:
            return True
