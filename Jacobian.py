#Joints R for revolute and P for prismatic
J = ["R","P","R","R","R","R"]

# A6 matrix
A6 = [[0.292, -0.956, 0, 0],
      [0.956, 0.292, 0, 0],
      [0, 0, 1, 0.1],
      [0, 0, 0, 1]]

# A5 matrix
A5 =[[-0.276, 0, 0.961, 0],
    [0.961, 0, 0.276, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 1]]

# A4 matrix
A4 =[[0.927, 0, 0.375, 0.046],
    [0.375, 0, -0.927, 0.019],
    [0, 1, 0, 0],
    [0, 0, 0, 1]]

# A3 matrix
A3 =[[0.707, 0.707, 0, 0.318],
    [0.707, -0.707, 0, 0.318],
    [0, 0, -1, 0.25],
    [0, 0, 0, 1]]

# A2 matrix
A2 =[[0, 1, 0, 0],
    [1, 0, 0, 0.65],
    [0, 0, -1, 0.78],
    [0, 0, 0, 1]]

# A1 matrix
A1 =[[0.682, -0.731, 0, 0.375],
    [0.731, 0.682, 0, 0.402],
    [0, 0, 1, 0.350],
    [0, 0, 0, 1]]

A123456, A23456, A3456, A456, A56 = [[0, 0, 0, 0], [0, 0, 0, 0],[0, 0, 0, 0],[0, 0, 0, 0]],\
                                    [[0, 0, 0, 0], [0, 0, 0, 0],[0, 0, 0, 0],[0, 0, 0, 0]],\
                                    [[0, 0, 0, 0], [0, 0, 0, 0],[0, 0, 0, 0],[0, 0, 0, 0]],\
                                    [[0, 0, 0, 0], [0, 0, 0, 0],[0, 0, 0, 0],[0, 0, 0, 0]],\
                                    [[0, 0, 0, 0], [0, 0, 0, 0],[0, 0, 0, 0],[0, 0, 0, 0]]


for i in range(len(A5)):
   for j in range(len(A6[0])):
       for k in range(len(A6)):
           A56[i][j] += A5[i][k] * A6[k][j]
           A56[i][j] = round(A56[i][j], 3)

for i in range(len(A4)):
   for j in range(len(A56[0])):
       for k in range(len(A56)):
           A456[i][j] += A4[i][k] * A56[k][j]
           A456[i][j] = round(A456[i][j], 3)

for i in range(len(A3)):
   for j in range(len(A456[0])):
       for k in range(len(A456)):
           A3456[i][j] += A3[i][k] * A456[k][j]
           A3456[i][j] = round(A3456[i][j], 3)

for i in range(len(A2)):
   for j in range(len(A3456[0])):
       for k in range(len(A3456)):
           A23456[i][j] += A2[i][k] * A3456[k][j]
           A23456[i][j] = round(A23456[i][j], 3)

for i in range(len(A1)):
   for j in range(len(A23456[0])):
       for k in range(len(A23456)):
           A123456[i][j] += A1[i][k] * A23456[k][j]
           A123456[i][j] = round(A123456[i][j], 3)

M = [A123456, A23456, A3456, A456, A56, A6]

#Calculating jacobian matrix
Jacob = [[0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0]]

for y in range(6):
    matrix = M[y]
    if J[y] == "R":
        Jacob[0][y] = (-matrix[0][0])*(matrix[1][3])+(matrix[1][0])*(matrix[0][3])
        Jacob[1][y] = (-matrix[0][1])*(matrix[1][3])+(matrix[1][1])*(matrix[0][3])
        Jacob[2][y] = (-matrix[0][2])*(matrix[1][3])+(matrix[1][2])*(matrix[0][3])
        Jacob[3][y] = matrix[2][0]
        Jacob[4][y] = matrix[2][1]
        Jacob[5][y] = matrix[2][2]
    elif J[y] == "P":
        Jacob[0][y] = matrix[2][0]
        Jacob[1][y] = matrix[2][1]
        Jacob[2][y] = matrix[2][2]
        Jacob[3][y] = 0
        Jacob[4][y] = 0
        Jacob[5][y] = 0

for i in range(len(Jacob)):
   for j in range(len(Jacob[0])):
        for k in range(len(Jacob)):
            Jacob[i][j] = round(Jacob[i][j], 3)

print("")
print("A6 matrix")
for r in A6:
   print(r)
print("")
print("A56 matrix")
for r in A56:
   print(r)
print("")
print("A456 matrix")
for r in A456:
   print(r)
print("")
print("A3456 matrix")
for r in A3456:
   print(r)
print("")
print("A23456 matrix")
for r in A23456:
   print(r)
print("")
print("A123456 matrix")
for r in A123456:
   print(r)
print("")
print("Jacobian matrix")
for r in Jacob:
   print(r)
