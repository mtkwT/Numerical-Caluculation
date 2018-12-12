from my_library import *

# 部分ピボット選択付きの前進消去をする関数
def forward_elimination_pivoting(A, b, N):
    for piv in range(N):
        # 各列で値が最大となる行を見つける
        max_val_row = piv
        max_val = 0.0
        for row in range(piv, N, 1):
            if (abs(A[row][piv]) > max_val):
                # 値が最大の行
                max_val_row = row
                max_val = abs(A[row][piv])
        # 値が最大の行と入れ替え
        if (max_val_row != piv):
            tmp = 0.0
            for col in range(N):
                tmp = A[max_val_row][col]
                A[max_val_row][col] = A[piv][col]
                A[piv][col] = tmp
            tmp = b[max_val_row]
            b[max_val_row] = b[piv]
            b[piv] = tmp
        # 前進消去の計算
        for row in range(piv+1, N, 1):
            alpha = A[row][piv] / (A[piv][piv])
            for col in range(piv, N, 1):
                A[row][col] -= A[piv][col] * alpha
            b[row] -= b[piv] * alpha
    return A, b

# 後退代入をする関数
def backward_substitution(A, b, N):
    for row in range(N-1, -1, -1):
        for col in range(N-1, row, -1):
            b[row] -= A[row][col] * b[col]
        b[row] /= A[row][row]
    return b

A = csv2matrix('../data/matrix-1.csv')
b = csv2vector('../data/vector-1.csv')
N = len(A) # Aの次数

A_fe, b_fe = forward_elimination_pivoting(A, b, N)
print("行列 A のガウスの消去法の出力: ")
print()
display_matrix(A_fe)
print()

print("解: ")
print()
x = backward_substitution(A, b, N)
display_vector(x)
print()