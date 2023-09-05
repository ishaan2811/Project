"""
      1
     121
    12321
   1234321
  123454321
 12345654321
1234567654321
"""
n=int(input())
i=1
while i<=n:
    #for spacing
    j=1
    while j<=n-i:
        print(" ",end='')
        j=j+1
    stars=1
    k=1
    #Number Increasing
    while stars<=i:
        print(k,end='')
        stars=stars+1
        k=k+1
    #Number Decreasing
    p=i-1
    while p>=1:
        print(p,end='')
        p=p-1
    print()
    i=i+1