class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        # Return base cases
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1,1]]
        
        # Initialize variables
        output_final = [[1], [1,1]]
        output_last = [1,1]
        
        # Iterate through all row values
        for i in range(2, numRows):
            # Initialize array for ith row
            output_row_i = [1] + [0]*(i-1) + [1]
            # Iterate through all elements in ith row except first and last element (always 1 and 1)
            for j in range(1, i):
                # Update jth element in ith row
                output_row_i[j] = output_last[j - 1] + output_last[j]
            output_last = output_row_i
            output_final.append(output_last)
            
        return output_final
