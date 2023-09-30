#Caro2PlayersCode
# def WinCondition(x, y):
#     Win = []
#     for i in range(5):
#         Win.append([[x+i-4,y],[x+i-3,y],[x+i-2,y],[x+i-1,y],[x+i,y]])
#         Win.append([[x,y+i-4],[x,y+i-3],[x,y+i-2],[x,y+i-1],[x,y+i]])
#         Win.append([[x+i-4,y+i-4],[x+i-3,y+i-3],[x+i-2,y+i-2],[x+i-1,y+i-1],[x+i,y+i]])
#         Win.append([[x+i-4,y-i+4],[x+i-3,y-i+3],[x+i-2,y-i+2],[x+i-1,y-i+1],[x+i,y-i]])
#     return Win
# t = 0
# Winner = 0
# Player = [[], []]
# while t>=0:
#     current = t%2
#     x, y = list(map(int, input().split()))
#     Player[current].append([x,y])
#     for lst in WinCondition(x, y):
#         count = 0
#         for pair in lst:
#             if pair in Player[current]:
#                 count +=1
#             if count == 5:
#                 Winner +=1
#                 current +=1
#                 print(f'PLAYER {current} WIN')
#                 break
#     if Winner==0:
#         t+=1
#     else:
#         break

# 2023-09-29 Today I encounter something fun thanks to Anh Quan Hoang
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
def stopping(n):
    a, b = n, somefunct(n)
    while a != b:
        a, b = somefunct(a), somefunct(b)
    return(a)
'''
The function have some predictable and some *weird* fixed points
'''