A = [15, 25, 35, 45, 55, 65, 75, 85, 95, 11, 0, 0, 0, 0, 0]
B = [1, 2, 3, 4, 5]
k = int(input("After which element?"))

if k <= 9 and k >= 0:
    for x in range(0, 10):
        A[x] = x*k
        for xd in range(0, 5):
            B[xd] = 10*(xd+1)*k
elif k < 0 or k > 9:
    k = 5
    for y in range(0, 10):
        A[y] = int(random.random()*50)
        for z in range(0, 5):
            B[z] = int(random.random()*50+50)

print(A)
print(B)

if k>=0 and k<=9:
    for zb1 in range(0, 10-k):
        A[14 - zb1] = A[9 - zb1]
    for zb2 in range(0, 5):
        A[k + zb2] = B[zb2]

print(A)
