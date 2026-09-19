class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        length = len(nums)
        nums +=[-1]
        for i in range(length):
            if nums[i]!=val:
                nums[k] = nums[i]
                k+=1
            

        return k

        