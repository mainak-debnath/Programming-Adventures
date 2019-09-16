r1,c1=input("Enter the number of rows and columns of 1st matrix:").split()
r1,c1=int(r1),int(c1)
x=[[int(input("Enter a number:")) for i in range(c1)]for j in range(r1)]

r2,c2=input("Enter the number of rows of 2nd matrix:").split()
r2,c2=int(r2),int(c2)
y=[[int(input("Enter a number:")) for i in range(c2)]for j in range(r2)]

print("Matrix 1:")
for i in range(r1):
    for j in range(c1):
        print(x[i][j]," ",end=" ")
    print()
print("Matrix 2:")
for i in range(r2):
    for j in range(c2):
        print(y[i][j]," ",end=" ")
    print()
z=[[0 for i in range(c2)]for j in range(r1)]
if(c1!=r2):
    print("Matrix multiplication is not possible")
else:
    print("Product of Matrix 1 and Matrix 2:")
    for i in range(r1):
        for j in range(c2):
            for k in range(r2):
                z[i][j]+=x[i][k]*y[k][j]

for r in z:
    print(r)
