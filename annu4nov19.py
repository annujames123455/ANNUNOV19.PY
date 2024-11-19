'''
author name:Annu James
date:19/11/24
'''
limit=int(input("enter the limit:"))
for i in range(limit+1):
    for j in range(i):
        print("*",end=" ")
    print()
print('decreasing triangle')
for i in range(limit,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()
    print("hill pattern")
for i in  range(1,limit+1):
          for j in  range(limit-i):
                print(" ",end=" ")
          for k in range(2*i-1):
                print("*",end=" ")
          print()
print("reverse hill pattern")
for i in range(limit,0,-1):
         for j in range(limit-i):
             print(" ",end=" ")
         for k in range(2*i-1):
             print("*",end=" ")
         print()
