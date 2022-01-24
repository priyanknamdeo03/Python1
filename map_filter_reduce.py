num = [2,3,4,5,6,7,8]

# num = list(map(lambda x:x*x,num))

# print(num)

# def square(a):
#     return a*a

# def cube(a):
#     return a*a*a
 
# func = [square,cube]

# for i in num:
#     val = list(map(lambda x:x(i), func))   #map.........................
#     print(val)

# print(list(filter(lambda x:x>5,num)))    #filter......................

from functools import reduce

print(reduce(lambda x,y:x+y,num))    #reduce........................