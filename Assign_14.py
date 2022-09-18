""" 1. Write a Python script to create a list of first N natural numbers. """
print("Enter the size of list to make a list of N natural numbers :")
n=int(input())
l1=[]
for i in range(n):
    l1.append(i+1)
print(l1)

""" 2. Write a Python script to create a list of first N odd natural numbers. """
print("Enter the size of list to make a list of first N odd natural numbers :")
n=int(input())
l1=[]
for i in range(1,2*n,2):
    l1.append(i)
print(l1)

"""3. Write a Python script to create a list of first N even natural numbers. """
print("Enter the size of list to make a list of first N even natural numbers :")
n=int(input())
l1=[]
for i in range(1,2*n,2):
    l1.append(i+1)
print(l1)

""" 
4. Write a Python script to find the greatest number in a given list of numbers."""
print("Enter the size of the list ")
n=int(input())
l1=[]
for i in range(n):
    l1.append(int(input()))
print(l1)
print(max(l1))


"""5. Write a Python script to find the smallest number in a given list of numbers. """
print("Enter the size of the list ")
n=int(input())
l1=[]
for i in range(n):
    l1.append(int(input()))
print(l1)
print(min(l1))


"""6. Write a Python script to calculate the sum of elements in a given list of numbers. """
print("Enter the size of the list ")
n=int(input())
l1=[]
for i in range(n):
    l1.append(int(input()))
print(l1)
print(sum(l1))

"""7. Write a Python script to remove all non int values from a list. """

print("Enter the size of the list ")
n=int(input())
l1=[]
for i in range(n):
    x=eval(input())
    l1.append(x)
print(l1)
l2=[]
for i in l1:
    if type(i)==int:
        l2.append(i)
print(l2)


""" 8. Write a Python script to print distinct elements along with their frequencies of
occurrence in the list. """

print("Enter the size of the list")
n=int(input())
l1=[]
l1.append(input() for i in range(n))

"""9. Write a Python script to print indices of all occurrences of a given element in a given
list. """
print("Enter the size of the list ")
n=int(input())
l1=[]
for i in range(n):
    l1.append(int(input()))
print(l1)
x=int(input("Enter a given element in that list to know the occurrences if that : "))
print("The occurrences of ",x,"is ->",l1.count(x))
for i in range(n):
    if x==l1[i]:
        print("The indices of all occurrences ->",i)
    

"""10. Write a python script to sort a list."""

print("Enter the size of the list ")
n=int(input())
l1=[]
for i in range(n):
    l1.append(int(input()))
l1.sort()
print(l1)

