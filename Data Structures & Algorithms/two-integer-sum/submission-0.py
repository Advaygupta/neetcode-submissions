class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            temp_list = nums[i+1:]
            num = target - nums[i]

            if max(temp_list)<(num) or min(temp_list)>num:
                pass
            else:
                for j in range(i+1, len(nums)):
                    if nums[j]==num:
                        return [i,j]
                    
        