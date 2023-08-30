"""
   1   2   3   4
   5   6   7   8
   9   10  11  12
   13  14  15  16

"""

n=int(input("Enter ant number "))
i=1
k=1
while(i<=n):
    j=1
    while(j<=n):
        print(k," ",end=" ")
        j=j+1
        k=k+1
    print()
    i=i+1