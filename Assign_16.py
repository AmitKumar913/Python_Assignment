""" 1. Write a python script to store multiple items in a single variable ( Items are “Java”
,“Python”,  “SQL”,  “C” ) using tuple"""


t1="java","python","SQL","C"
print(t1)

"""2. Write a python program to store only one item using tuple."""
t1=tuple( [int(e) for e in input("Enter ony one element \n").split(',') ] )
print(t1)
print(type(t1))

"""3. Write a python program to reverse the tuple. """

t1=tuple( [int(e) for e in input("Enter the elements separated by comma \n").split(',') ] )
print(t1)
print(t1[::-1])

"""4. Write a python program to Swap two tuples in Python. """
t1="a","b","c"
t2=4,8,2
t3=()
t3=t2
t2=t1
t1=t3
print(t1)
print(t2)

"""5. Write a python program to check if all items in the tuple are the same. """

t1=tuple( [int(e) for e in input("Enter the elements separated by comma for 1st tuple \n").split(',') ])
t2=tuple( [int(e) for e in input("Enter the elements separated by comma for 2nt tuple \n").split(',') ])
print("if all items in the tuple are the same then 'True' otherwise 'False'")
print(True if t1==t2 else False)

""" 6. Write a python program to divide the tuple into four variables.
tuple1=(100, 200, 300, 400)"""

tuple1=(100, 200, 300, 400)
for i in tuple1:
    t1=tuple( [int(e) for e in str(i).split(',') ])
    print(t1)

"""7. Write a python program to copy elements 4 and 5 from the following tuple  into a new
tuple. tuple1=(1,2,3,4,5,6)  """

tuple1=(1,2,3,4,5,6)
t1=()
t1=tuple1[4:6:]
print(tuple1)
print(t1)

""" 8. Write a python program to Sort a tuple of tuples by the second item.
tuple1 = (('a', 21),('b', 37),('c', 11), ('d',29))"""

tuple1 = (('a', 21),('b', 37),('c', 11), ('d',29))
print(tuple1)
l1=list(tuple1)
l2=[]
n=len(l1)
while n:
    i=0
    x=l1[i]
    while i!=(n):
        if x[1]>l1[i][1]:
            x=l1[i]
            ind=l1.index(l1[i])
        i+=1
    l2.append(x)
    l1.remove(x)
    n=len(l1)
print("Sorted tuple of tuples by the second item : ")
print(tuple(l2))


"""9. Write a python program to print the value 20 from given nested tuple
tuple1 = ("Python", [10, 20, 30], (2, 4, 16)) """

tuple1 = ("Python", [10, 20, 30], (2, 4, 16))
print(tuple1[1][1])



""" 10. Write a python program to change the first item (22) of a list within the following tuple
to 222.
tuple1 = (11, [22, 33], 44, 55)"""
tuple1 = (11, [22, 33], 44, 55)
tuple1[1][0]=222
print(tuple1)
