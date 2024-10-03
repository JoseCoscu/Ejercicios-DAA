from itertools import permutations


arr1=['p','p','p','','p','','','c','','p',''] #output: 2
#          pi                          pj
arr2=['p','p','','p','','','c','','','p'] #output: 3
#     pi                      
arr3=['','p','','p','','','c','','','p','','p','','p'] #output: 5



def crim_max(arr):
    c=-1
    pi=-1
    pj=len(arr)+1
    for i in range(len(arr)):
        if arr[i]=='c':
            c=i
            break
    for i in range(len(arr)):
        if arr[i]=='p' and i<c and (c-i)%2==0:
            pi=i
        if arr[i]=='p' and pj==len(arr)+1 and i>c and (i-c)%2==0:
            pj=i
    count=0
    for i in range(len(arr)):
        if arr[i]=='p' and i>pi and i<pj:
            count+=1
    return count



# print(crim_max(arr1))
# print(crim_max(arr2))
# print(crim_max(arr3))

