"""
    1
    2 1
    3 2 1
    4 3 2 1
"""
n=int(input("Enter any number:"))
i=1
k=1
while i<=n:
    j=1
    k=i
    while j<=i:
        print(k,end=" ")
        j=j+1
        k=k-1
    print()
    i=i+1