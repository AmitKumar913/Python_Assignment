""" 1. Write a python script to check whether a given number is positive or non-positive"""
from re import X


x=int(input("Enter a no :"))
print("Positive"if x>0 else "Negative")

""" 2. Write a python script to check whether a given number is divisible by 5 or not"""
x=int(input("Enter a no to check the divisivility of 5 "))
if x%5==0 :
    print(x," is divisible by 5")
else :
    print(x,"is not divisible by 5")

""" 3. Write a python script to check whether a given number is even or odd"""

x=int(input("Enter a number to check even or odd : "))
print("Even" if x%2==0 else "Odd")

""" 4. Write a python script to print greater between two numbers. Print number only once
even if the numbers are the same"""

x=int(input("Enter two numbers : "))
y=int(input())
if x==y:
    print(x)
elif x>y:
    print(x)
else:
    print(y)

""" 5. Write a python script to print two given words in dictionary order """

s1=input("Enter two Words :")
s2=input()
if s1<s2:
    print(s1)
    print(s2)
else:
    print(s2)
    print(s1)


""" 7. Write a python script to check whether a given number is positive, negative or zero"""

x=int(input("Enter a number :"))
if x>0 :
    print(x,"positive")
elif x<0:
    print(x,"Negative")
else :
    print(x,"Zero")
    
""" 8. Write a python script to check whether a given quadratic equation has two real &
distinct roots, real & equal roots or imaginary roots"""

print("Enter the a ,b and c to calculate the discriminant (b2 – 4ac),where ax^2+bx+c ")
a=int (input())
b=int(input())
c=int (input())
d=(b*b)-(4*a*c)
if d>0:
    print("real and distinct roots")
elif d<0:
    print("imaginary roots")
else :
    print("real and equal roots")
    
""" 9. Write a python script to check whether a given year is a leap year or not."""
print("Enter a year :")
x=int(input())
if x%4==0:
    print(x,"is a leap year")
else :
    print(x,"is not a leap year  ")

""" 10. Write a python script to print greater among three numbers. Print number only once
even if the numbers are the same """
x=int(input("Enter the three no :"))
y=int(input())
z=int(input())
if x>y and x>z:
    print(x)
elif y>x and y>z:
    print(y)
elif z>y and z>x:
    print(z)