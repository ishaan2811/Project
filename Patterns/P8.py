'''
    A B C D
    A B C D
    A B C D
    A B C D
'''
n=int(input("Enter any number"))
i=1
while(i<=n):
    j=1
    while(j<=n):
        print(chr(ord('A')+j-1)," ",end="")
        j=j+1
    print()
    i=i+1