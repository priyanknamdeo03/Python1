# Pattern
var = int(input("enter number "))
for i in range(1,var+1):
    print("  "*(i),end="")
    for j in range(i,var):
        print(j,end=" ")
    print()