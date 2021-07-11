# n = int(input("enter no. of rows"))
#
# for i in range(n):
#     print((chr(65+i)+" ")*(i+1))

n = int(input("enter no. of rows"))
k=0
for i in range(n):
    for j in range(i+1):
        print(chr(65+k)+" ",end="")
        k+=1
    print()

# for i in range(n,0,-1):
#     print("*"*(i),end="  ")
#     print()


# for i in range(n,0,-1):
#     for j in range(  i):
#         print(chr(65+j)+" ",end="")
#     print()