import csv

data = []
with open("../data/value-2.csv", "r") as fp:
    for row in csv.reader(fp):
        data.append(row)

x = []
y = []
for i in range(len(data)):
    x.append(float(data[i][0]))
    y.append(float(data[i][1]))

#スプライン解行列Aの作成のための値計算
h = [x[1] - x[0]]
v=[]
A = [(len(x) - 2) * [0]]

j = 1
while j < len(x) - 1:
    if j != len(x) - 2:
        A.append((len(x) - 2) * [0])
    h.append(x[j+1] - x[j])
    v.append(6 * ((y[j+1] - y[j]) / h[j] - (y[j] - y[j-1]) / h[j-1]))
    j += 1

#スプライン解を計算する連立方程式の係数行列Aの作成
j = 0
while j < len(x) - 2:
    if j == 0:
        A[0][0] = 2 * (h[0] + h[1])
        A[0][1] = h[1]
    elif j == (len(x) - 3):
        A[j][j-1] = h[j-2]
        A[j][j]   = 2 * (h[j-2] + h[j-1])
    else:
        A[j][j-1] = h[j]
        A[j][j]   = 2 * (h[j]+h[j+1])
        A[j][j+1] = h[j+1]
    j += 1

N = len(A)
# Aの逆行列計算（ガウス消去法を用いる）
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

A_fe, v_fe = forward_elimination_pivoting(A, v, N)
u_fe = backward_substitution(A_fe, v_fe, N)

u = [0]
for j in range(len(x)-1):
    if j==len(x)-2:
        u.append(0)
    else:
        u.append(u_fe[j])

#3次の近似関数の係数a,b,c,dを決定
a=[(u[1] - u[0]) / (6 * (x[1] - x[0]))]
b=[u[0] / 2]
c=[(y[1] - y[0]) / (x[1] - x[0]) - 1/6 * (x[1] - x[0]) * (2 * u[0] + u[1])]
d=[y[0]]
for j in range(1, len(x) - 1):
    a.append((u[j+1] - u[j]) / (6 * (x[j+1] - x[j])))
    b.append(u[j] / 2)
    c.append((y[j+1] - y[j]) / (x[j+1] - x[j]) - 1/6 * (x[j+1] - x[j]) * (2 * u[j] + u[j+1]))
    d.append(y[j])

for i in range(len(a)):
    print(i, "番目の多項式の係数（a, b, c, d）の順", a[i], b[i], c[i], d[i])