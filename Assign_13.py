"""1. Write a python script to store multiple items in a single variable ( Items are “Java”
,“Python”,  “SQL”,  “C” ) using list """

l1=[ "Java" , "Python", "SQL", "C"]
print(l1)
#or
print("Enter the size of the list :")
n=int(input())
l1=[]
for i in range():
    l1.append(input())
print(l1)


""" 2. Write a python script to get the data type of a list. """
l1=[ "Java" , "Python", "SQL", "C"]
print(type(l1))

"""3. Write a python script to get the last item of the list ( mylist = ["Java", "C", "Python"])"""

l1=["Java", "C", "Python"]
print(l1[-1])

""" 4. Write a python script to Change the values "SQL" and "Reactnative" with the values
"NoSQL" and "Flutter" (List is thislist = ["Java", "SQL", "C", "Reactnative",
"Javascript", "Python"] """

thislist=["Java", "SQL", "C", "Reactnative","Javascript", "Python"]
thislist[1]="NoSQL"
thislist[3]="Flutter"
print(thislist)


""" 5. Write a python script to add an item to the end of the list (item “Python”. (mylist =
["Java", "SQL", "C", "Reactnative"]  """

mylist=["Java", "SQL", "C", "Reactnative"]
mylist.append("Python")
print(mylist)

""" 6. Write a python program to append elements from another list to the current list.(firstlist = ["Java", "Python", "SQL"] secondlist = ["C", "Cpp", "NoSQL"] )"""


firstlist=["Java", "Python", "SQL"]
secondlist=["C", "Cpp", "NoSQL"]
finallist=firstlist+secondlist
print(finallist)

"""7. Write a python program to Print all items by referring to their index number (thislist =
["Java", "SQL", "C", "Reactnative", "Javascript", "Python"] """
this_list=["Java", "SQL", "C", "Reactnative", "Javascript", "Python"]
for i in range(len(this_list)):
    print("[",i,"]"," ",this_list[i])


""" 8. Write a python program to sort the list alphanumerically – thislist = ["Java", "SQL",
"C", "Reactjs", "Javascript", "Python"] """

thislist = ["Java", "SQL","C", "Reactjs", "Javascript","Python"]
print(sorted(thislist))

""" 9. Write a Python script to create a list of city names taken from the user."""

print("Enter the size of the list ")
n=int(input())
print("Enter the name of the city :")
l1=[]
for i in range(n):
    l1.append(input())
print(l1)


""" 10. Write a Python script to create a list, where each element of the list is a digit of a
given number."""

print("Enter a  no :")
x=input()
l1=[]
for i in x:
    i=int(i)
    l1.append(i)
print(l1)