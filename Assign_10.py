
""" 1. Write a python script to print MySirG N times on the screen"""
x="MySirG"
n=int(input("Enter the value of n :"))
for i in range(n):
    print(x)

"""2. Write a python script to print first N natural numbers """

print("Enter the n to print the first N natural numbers :")
n=int(input())
for i in range(n):
    print(i+1,end=" ")

"""3. Write a python script to print first N natural numbers in reverse order """

print("Enter the n to print the first N natural numbers in reverse order :")
n=int(input())
for i in range(n,0,-1):
    print(i,end=" ")
print()

"""4. Write a python script to print first N odd natural numbers """

print("Enter the value of n to print the first N odd natural numbers :")
n=int(input())
x=2*n
for i in range(1,x,2):
    print(i,end=" ")
print()

""" 5. Write a python script to print first N odd natural numbers in reverse order """

print("Enter the value of n to print the first N odd natural numbers in reverse order :")
n=int(input())
x=2*n
for i in range(x-1,0,-2):
    print(i,end=" ")
print()

"""6. Write a python script to print first N even natural numbers """

print("Enter the value of the n to print the first N even natural numbers : ")
n=int(input())
x=2*n
for i in range(0,x,2):
    print(i+2,end=" ")
print()

""" 7. Write a python script to print first N even natural numbers in reverse order """
print("Enter the value of the n to print the first N even natural numbers in reverse order : ")
n=int(input())
x=2*n
for i in range(x,0,-2):
    print(i,end=" ")
print()

""" 8. Write a python script to print squares of first N natural numbers """
print("Enter the value of n to print the squares of first N natural numbers :")
n=int(input())
for i in range(0,n,1):
    print((i+1)**2,end=" ")
print()

""" 9. Write a python script to print cubes of first N natural numbers """

print("Enter the value of n to print the cubes of first N natural numbers :")
n=int(input())
for i in range(0,n,1):
    print((i+1)**3,end=" ")
print()

""" 10. Write a python script to print first 10 multiples of N """
print("Enter n to print the first 10 multiples of N : ")
n=int(input())
for i in range(10):
    print(n*(i+1),end=" ")
print()