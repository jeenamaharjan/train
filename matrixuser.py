p = int(input("enter the number of row matrix:"))
q = int(input("enter the number of column matrix:"))
n = int(input("enter the column number of matrix/row number of matix:"))

print("enter the number of matrix1 :")
matrix1 = [[int(input()) for i in range(n)] for i in range(p)]
print("matrix1:")
for i in range(p):
    for j in range(n):
        print(format(matrix1[i][j],"<5"),end="")
    print()
print("enter the elements for matrix2:")
matrix2 = [[int(input()) for i in range(q)] for i in range(n)]
print("matrix2:")
for i in range(n):
    for j in range(q):
        print(format(matrix2[i][j],"<5"),end="")
    print()

result = [[0 for i in range(q)]for j in range(p)]
for i in range(p):
    for j in range(q):
        for k in range(n):
            result[i][j] = result[i][j] + matrix1[i][k] + matrix2[k][j]
print("result is :")
for i in range(p):
    for j in range(q):
        print(format(result[i][j],"<5"),end="")
    print()