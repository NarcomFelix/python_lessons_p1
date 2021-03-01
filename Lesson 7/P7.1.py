
class Matrix:
    def __init__(self, matrix_content=[[]]):
        self.matrix_content = matrix_content

    def __str__(self):
        result = ''
        for i in range(0, len(self.matrix_content)):
            for k in range(0, len(self.matrix_content[i])):
                result = result + str(self.matrix_content[i][k]) + ' '
            result += '\n'
        return result

    def __add__(self, other):
        if len(self.matrix_content) == len(other.matrix_content) and len(
                self.matrix_content[0]) == len(other.matrix_content[0]):
            result = []
            for i_row in range(0, len(self.matrix_content)):
                temp = []
                for i_col in range(0, len(self.matrix_content[0])):
                    temp.append(self.matrix_content[i_row][i_col] +
                                other.matrix_content[i_row][i_col])

                result.append(temp)
            return Matrix(result)
        else:
            print("Матрицы разного размера")


matrix_1 = Matrix([[2, 2, 2], [3, 3, 3]])
print(matrix_1)
matrix_2 = Matrix([[4, 4, 4], [5, 5, 5]])
print(matrix_2)
result_matrix = matrix_1 + matrix_2
print(result_matrix)
        
