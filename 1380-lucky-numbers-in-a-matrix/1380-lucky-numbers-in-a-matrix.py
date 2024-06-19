class Solution:
    def luckyNumbers(self, matrix):
        row_min = []
        for row in matrix:
            row_min.append(min(row))
            
        col_max = []
        num_cols = len(matrix[0])
        for j in range(num_cols):
            max_val = matrix[0][j]
            for i in range(len(matrix)):
                if matrix[i][j] > max_val:
                    max_val = matrix[i][j]
            col_max.append(max_val)
            
        lucky_numbers = []
        for i in range(len(matrix)):
            for j in range(num_cols):
                if matrix[i][j] == row_min[i] and matrix[i][j] == col_max[j]:
                    lucky_numbers.append(matrix[i][j])
        
        return lucky_numbers