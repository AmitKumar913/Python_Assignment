""" 1. Write a python script to print MySirG N times on the screen"""

print("Enter the no. of time you want to print :")
n=int(input())
while n>0:
    print("MySirG")
    n-=1
print()

""" 2. Write a python script to print first N natural numbers"""
print("Enter the value of n you want to print the natural numbers")
n=int(input())
i=0
while i<n:
    print(i+1,end=" ")
    i+=1
print()

""" 3. Write a python script to print first N natural numbers in reverse order """

print("Enter the value of n you want to print the natural numbers in reverse order")
n=int(input())
while n>0:
    print(n,end=" ")
    n-=1
print()
""" 4. Write a python script to print first N odd natural numbers"""
print("Enter the value of n to want the first n odd natural numbers :")
n=int(input())
i=0
count=0
while count!=n:
    if i%2!=0:
        print(i,end=" ")
        count+=1
    i+=1
print()
"""5. Write a python script to print first N odd natural numbers in reverse order """

print("Enter the value of n to want the first n odd natural numbers in reverse order :")
n=int(input())
i=2*n
while i>0:
    if i%2!=0:
        print(i,end=" ") 
    i-=1
print()  
"""6. Write a python script to print first N even natural numbers """

print("Enter the value of n to want the first n odd natural numbers :")
n=int(input())
i=1
count=0
while count!=n:
    if i%2==0:
        print(i,end=" ")
        count+=1
    i+=1
print()

"""7. Write a python script to print first N even natural numbers in reverse order """

n=int(input())
i=2*n
while i>0:
    if i%2==0:
        print(i,end=" ") 
    i-=1
print() 

""" 8. Write a python script to print squares of first N natural numbers"""
print("Enter the value of the n to print squares of the first N natural numbers :")
n=int(input())
i=1
while i<=n:
    print(i**2,end=" ")
    i+=1

"""9. Write a python script to print cubes of first N natural numbers"""
print("Enter the value of the n to print cubes of the first N natural numbers :")
n=int(input())
i=1
while i<=n:
    print(i**3,end=" ")
    i+=1

""" 10. Write a python script to print first 10 multiples of N"""

print("Enter the value of the n to print  first 10 multiples of N :")
n=int(input())
i=1
while i<=n:
    print(i*5,end=" ")
    i+=1
