import csv

# 配列を行列風に表示する関数
def display_matrix(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            print(matrix[row][col], end=" ")
        print()

# 配列をベクトル風に表示する関数
def display_vector(vector):
    for row in range(len(vector)):
        print(vector[row], end=" ")
    print()

# csvファイルから行列を表す2次元配列を作る関数
def csv2matrix(filename):
    with open(filename) as fp:
        matrix = list(csv.reader(fp))
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                matrix[row][col] = float(matrix[row][col])
    return matrix

# csvファイルからベクトルを表す1次元配列を作る関数
def csv2vector(filename):
    with open(filename) as fp:
        vector = list(csv.reader(fp))[0]
        for row in range(len(vector)):
            vector[row] = float(vector[row])
    return vector

if __name__ == '__main__':
    A = csv2matrix('../data/matrix-1.csv')
    display_matrix(A)
    print()

    b = csv2vector('../data/vector-1.csv')
    display_vector(b)
    print()