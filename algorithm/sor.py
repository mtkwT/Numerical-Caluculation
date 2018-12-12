from my_library import *

def sor_algorithm(A, b, N, x):
    while(1):
        summation = 0
        error = 0
        for i in range(N):
            new_x = 0
            for j in range(N):
                if j != i:
                    new_x += A[i][j] * x[j]
            new_x = omega * (b[i] - new_x) / A[i][i] + (1 - omega) * x[i]
            summation += abs(new_x)
            error += abs(new_x - x[i]) 
            x[i] = new_x
        if (error < epsilon * summation):
            break
    return x

A = csv2matrix('../data/matrix-2.csv')
b = csv2vector('../data/vector-1.csv')
N = len(A)

epsilon = 1e-6 # 収束判定条件のε=10^-6
omega = 1.0
x = [0 for _ in range(N)] # 初期値

x = sor_algorithm(A, b, N, x)
print("sor法による連立方程式の解: ")
print()
display_vector(x)