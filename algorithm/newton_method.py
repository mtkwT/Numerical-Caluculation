import csv

with open("../data/polynomial-1.csv", "r") as fp:
    reader = csv.reader(fp)
    poly_coef = [d for d in reader][0]

for i in range(len(poly_coef)):
    poly_coef[i] = float(poly_coef[i])

print("多項式 f1 の係数: ", poly_coef)

poly_coef = poly_coef[::-1] # 後で計算しやすいように昇べき順にしておく

# 最適化する目的関数（多項式）
def optimize_func(x):
    func = 0
    for i in range(len(poly_coef)):
        func += poly_coef[i] * x**i        
    return func

# 最適化する目的関数の導関数
def optimize_func_prime(x):
    func = 0
    for i in range(len(poly_coef)):
        if i != 0:
            func += poly_coef[i] * i * x**(i-1)
    return func

# ニュートン法
def newton_method(initial_value, error):
    x_past = initial_value
    x_current = 0
    while(1):
        x_current = x_past - (optimize_func(x_past) / optimize_func_prime(x_past))
        if optimize_func(x_current) < error:
            break
        x_past = x_current
    return x_current

with open("../data/value-1.csv", "r") as fp:
    reader = csv.reader(fp)
    init = [d for d in reader][0][0]

init = float(init)

x = newton_method(init, 1e-8)

print("解: ", x)