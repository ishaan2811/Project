"""
1
2 3
3 4 5
4 5 6 7

"""
n = int(input())
i=1
while(i<=n):
    j=1
    while(j<=i):
        print(j+i-1, end=" ")
        j=j+1
    print()
    i=i+1