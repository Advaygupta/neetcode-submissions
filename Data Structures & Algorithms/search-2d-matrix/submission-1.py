class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        columns = len(matrix[0])

        left = 0
        right = len(matrix) - 1

        while left<=right:
            mid = (left+right)//2

            current_row = matrix[mid]
            last_element = current_row[-1]

            if target==last_element:
                return True
            else:
                if target>last_element:
                    left = mid+1
                elif target<current_row[0]:
                    right = mid-1
                else:
                    first = 0
                    last = len(current_row)

                    while first<=last:
                        middle = (first+last)//2
                        if target==current_row[middle]:
                            return True
                        elif target<current_row[middle]:
                            last = middle - 1
                        else:
                            first = middle+1
                    return False
        return False



        