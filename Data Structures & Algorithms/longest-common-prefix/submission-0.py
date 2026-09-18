class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest_string = ""

        first_string = strs[0]

        for i in range(len(first_string)):
            for j in strs[1:]:
                if len(j)<=i:
                    return longest_string
                if j[i] != first_string[i]:
                    return longest_string
            longest_string+=first_string[i]

        return longest_string

        