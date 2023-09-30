import random

# 3
def increasingOrder(n):
    lst = [i for i in str(n)]
    lst.sort()
    return lst
def decreasingOrder(n):
    lst = increasingOrder(n)
    lst.reverse()
    return lst
def somefunct(n):
    incre = int(''.join(increasingOrder(n)))
    decre = int(''.join(decreasingOrder(n)))
    return decre - incre
# for i in range(100000000):
#     test = somefunct(i) - i
#     if test == 0:
#         print(i)

def stopping(n):
    a, b = n, somefunct(n)
    while a != b:
        a, b = somefunct(a), somefunct(b)
        print(a)
    return(a)

def stopping1(n):
    a = n
    lst = []
    while a not in lst:
        lst.append(a)
        a = somefunct(a)
    lst.append(a)
    return lst
def somefunctLoop(n):
    lst = stopping1(n)
    l = len(lst)
    for i in range(l):
        if lst[i] == lst[-1]:
            newlist = lst[i:-1]
            break
    return(newlist)
dct = {}
for i in range(20000):
    if len(somefunctLoop(i))==2:
        dct[i] = somefunctLoop(i)
print(dct.values())




l = 5
sol = '6'
for i in range(l):
    sol += '3'
sol += '17'
for i in range(l):
    sol += '6'
sol += '4'
