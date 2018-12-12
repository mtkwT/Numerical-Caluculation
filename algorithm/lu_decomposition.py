from my_library import *

# 三重対角行列をLU分解する関数
def LU_decomposition(A, Lower_matrix, Upper_matrix, N):
    d = A[0][0]
    Upper_matrix[0][0] = d
    Lower_matrix[0][0] = 1
    
    for row in range(1,N):
        l = A[row][row-1] / d
        Lower_matrix[row][row-1] = l
        Lower_matrix[row][row] = 1
        
        d = A[row][row] - (l * A[row-1][row])
        Upper_matrix[row][row] = d
        Upper_matrix[row-1][row] = A[row-1][row]
    
    return Lower_matrix, Upper_matrix

# 前進代入する関数
def foward_substitution(Lower_matrix, b):
    z = [0 for _ in range(len(b))]
    z[0] = b[0]
    
    for row in range(1, N, 1):
        z[row] = b[row] - (Lower_matrix[row][row-1] * z[row-1])
    
    return z

# 後退代入する関数
def backward_substitution(Upper_matrix, z):
    x = [0 for _ in range(len(z))]
    x[-1] = z[-1] / Upper_matrix[-1][-1]
    
    for row in range(N-1, -1, -1):
        x[row-1] = (z[row-1] - (Upper_matrix[row-1][row] * x[row])) / Upper_matrix[row-1][row-1]
    
    return x

A = csv2matrix('../data/matrix-2.csv')
b = csv2vector('../data/vector-1.csv')
N = len(A)

Lower_matrix = [[0 for row in range(N)] for col in range(N)] 
Upper_matrix = [[0 for row in range(N)] for col in range(N)]

Lower_matrix, Upper_matrix = LU_decomposition(A, Lower_matrix, Upper_matrix, N)
print("行列 A のLU分解の出力: ")
print()
print("下三角行列: ")
display_matrix(Lower_matrix)
print()
print("上三角行列: ")
display_matrix(Upper_matrix)
print()

z = foward_substitution(Lower_matrix, b)   # 前進代入
x = backward_substitution(Upper_matrix, z) # 後退代入
print("解: ")
print()
display_vector(x)
print()