class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionery = dict()

        for i in strs:
            i_list = [0]*26
            for j in i:
                i_list[ord(j) - ord('a')] += 1

            i_tuple = tuple(i_list)
            if i_tuple not in dictionery:
                dictionery[i_tuple] = [i]
            else:
                dictionery[i_tuple].append(i)

        output_list = list()
        for anagram in dictionery.values():
            output_list.append(list(anagram))

        return output_list 




        