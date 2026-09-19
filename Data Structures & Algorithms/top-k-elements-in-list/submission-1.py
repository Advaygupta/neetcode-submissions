class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = dict()

        for i in nums:
            if i in freq_dict:
                freq_dict[i]+=1
            else:
                freq_dict[i]=1

        values = list(freq_dict.values())
        keys = list(freq_dict.keys())
        output_list = list()

        for i in range(k):
            max_val = max(values)
            index = values.index(max_val)
            output_list.append(keys[index])

            del values[index]
            del keys[index]

        return output_list
        