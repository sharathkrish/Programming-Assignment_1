# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 16:01:20 2022

@author: hp
"""

# Write a Python program to convert kilometers to miles?

km = int(input("Enter distance covered in km:"))
cnv = 0.621371
miles = km * cnv
print("distance covered in miles:", miles)


#Write a Python program to convert Celsius to Fahrenheit?

Cels = int(input("Enter temperature in celsius:"))
cnv= (Cels * 1.8) + 32
Fahrenheit = print("temperature in Fahrenheit:", cnv)

#Write a Python program to display calendar?

import calendar
year = int(input("enter year:"))
month = int(input("enter month:"))
print(calendar.month(year,month))

#Write a Python program to solve quadratic equation?

a= float(input("Enter the number for Quadratic EQ:"))
b= float(input("Enter the number for Quadratic EQ:"))
c= float(input("Enter the number for Quadratic EQ:"))
p= ((-b) + ((b*b - 4*a*c)**0.5))/2*a
q= ((-b) - ((b*b - 4*a*c)**0.5))/2*a
print("Solution for the quadratic equation:",p,q)


#Write a Python program to swap two variables without temp variable?

a= int(input("Enter a number:"))
b= int(input("Enter a number:"))
a,b=b,a
print(a,b)