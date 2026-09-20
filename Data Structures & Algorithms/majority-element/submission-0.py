class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        freq_dict = dict()

        for i in nums:
            if i in freq_dict:
                freq_dict[i]+=1
            else:
                freq_dict[i]=1

        keys = list(freq_dict.keys())
        values = list(freq_dict.values())

        for i in range(len(values)):
            if values[i]>(len(nums)/2):
                return keys[i]
        