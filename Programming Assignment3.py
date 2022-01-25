# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 12:43:09 2022

@author: hp
"""

#Write a Python Program to Check if a Number is Positive, Negative or Zero?

n=int(input("enter a number:"))
if (n>0):
    print("Number is Positive:",n)
elif(n<0):
    print("Number is negative:",n)
else:
    print("number is zero:")
    
#Write a Python Program to Check if a Number is Odd or Even?

n=int(input("enter a number:"))
if (n%2==0):
    print("Number is even:",n)
else:
    print("number is odd:",n)
    
    
#Write a Python Program to Check Leap Year?

y=int(input("enter a year:"))
if(y%4==0 and y%100!=0 ):
    print("leap year:",y)
elif(y%400==0):
    print("leap year:",y)
else:
    print("not leap year:",y)
    
#Write a Python Program to Check Prime Number?

def primechk(n):
    '''returns if a number is prime or not'''
    k='prime number'
    for i in range(2,n-1):
        if n%i==0:
            k='not prime number'
    return k      

y=int(input("enter a positive integer to be checked if prime"))
o=primechk(y)
print(o)

#Write a Python Program to Print all Prime Numbers in an Interval of 1-10000?

for Number in range (1, 10001):
    count = 0
    for i in range(2, (Number//2 + 1)):
        if(Number % i == 0):
            count = count + 1
            break

    if (count == 0 and Number != 1):
        print(" %d" %Number, end = '  ')