""" 1. Write a python script to remove the last digit from a given number. (for example, if
user enters 2534 then your output should be 253) """

from re import S


x=int(input("Enter a no :"))
y=x%10
x=(x-y)//10
print(x)

""" 2. Write a python script to get the last digit from a given number. (for example, if user
enters 2089 then your output should be 9) """

x=int(input("Enter a no :"))
y=x%10
print(y)

""" 3. Write a python script to swap data of two variables """
x=int(input("Enter first no "))
y=int(input("Enter the second no "))
temp=x
x=y
y=temp
print(x,y)

""" 4. Write a python script to find x power y, where values of x and y are given by user """
x=int(input("Enter the value of x :"))
y=int(input("Enter the value of y :"))
print(pow(x,y))

""" 5. Write a python script which takes a three digit number from the user and displays
only its first digit"""

x=int(input("Enter a three digit no : "))
temp=x%10
x=(x-temp)//10
temp=x%10
x=(x-temp)//10
print(x)

""" 6. Write a python script which takes a three digit number from the user and displays
only its middle digit."""
x=int(input("Enter a three digit no : "))
temp=x%10
x=(x-temp)//10
temp=x%10
print(temp)

""" 7. Write a python script which takes a three digit number from the user and displays
only its last digit."""
x=int(input("Enter a three digit no : "))
temp=x%10
print(temp)

""" 8. Write a python script to use IN operator to display the data present in the list"""

l1="MySirG"
print("i" in l1)

""" 9. Write a python script to use NOT IN operator to display the data not present in list """

l1="MySirG"
print("i" not in l1)

"""  10. Write a python script to use IS operator to display if both variables are the same
object or not? """

x=5
y=7
z="A"
q="A"
s=5
print(x is y)
print(z is q)
print(x is s)