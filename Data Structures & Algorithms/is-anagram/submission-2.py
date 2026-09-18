class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_dict = {}

        for char in s:
            if char in char_dict:
                char_dict[char]+=1
            else:
                char_dict[char]=1
        
        for char in t:
            if char in char_dict:
                char_dict[char] -= 1

                if char_dict[char] <0:
                    return False
            else:
                return False

        for char in char_dict:
            if char_dict[char]>0:
                return False
        return True



        