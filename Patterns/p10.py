'''
     A
     B C
     C D E
     D E F G
'''
n=int(input("Enter any number"))
i=1
while(i<=n):
    j=1
    while(j<=i):
        print(chr(ord("A")+j+i-2)," ",end="")
        j=j+1
    print()
    i=i+1