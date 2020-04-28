'''def is_even(n):
    return n%2!=0'''
from functools import reduce 
nums=[2,6,3,5,1,8,9,10,14,17]
print(nums)
even=list(filter(lambda n : n%2!=0, nums))
db= list(map(lambda n : n+2, nums))
sum=reduce(lambda a,b: a+b,db)
print(even)
print(db)
print(sum)
