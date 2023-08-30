'''
    A
    A B
    A B C
    A B C D
'''
n=int(input("ENTER ANY NUMBER"))
i=1
while(i<=n):
    j=1
    while(j<=i):
        print(chr(ord('A')+j-1),end=" ")
        j=j+1
    print()
    i=i+1

