class Solution:
    def mySqrt(self, x: int) -> int:
        if x==1:
            return 1

        # list_checks = list(range(x//2 + 1))

        left = 0
        right = x//2

        while left<=right:
            mid = (left+right)//2

            if mid*mid == x or ((mid+1)*(mid+1)>x and mid*mid < x):
                return mid
            else:
                if mid*mid<x:
                    left = mid+1
                else:
                    right = mid-1

        