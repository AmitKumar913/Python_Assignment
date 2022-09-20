""" 1. Write a python program to store all the programming languages known to you using
Set."""
s1=set()
n=int(input("Enter the value of n to stroe the N programming languages known to you : "))
print("Enter the languages names one by one : ")
while n:
    x=input()
    s1.add(x)
    n-=1
print(s1)

""" 2. Write a python program to store your own information {name, age, gender, so on..}"""
s1=set()
print("Enter your own information : ")
s1.add(input("Enter your name : "))
s1.add(int(input("Age :")))
s1.add(input("Enter your gender : "))
print(s1)
    
"""3. Write a python script to get the data type of a Set. """
s1={ 10,'aA',67.7,(2+1j),'this',True}
print(s1)
print(type(s1))
for i in s1:
    print(i,type(i))

"""4. Write a Python script to find if “Python” is present in the set  thisset = {"Java",
"Python", "Django"} """

thisset = {"Java","Python", "Django"}
print(True if "Python" in thisset else False)

"""5. Write a python program to add items from another set to the current set. thisset =
{"Java", "Python", "SQL"}
secondset= {"C", "Cpp", "NoSQL"} """

thisset ={"Java", "Python", "SQL"}
secondset= {"C", "Cpp", "NoSQL"}
thisset.update(secondset)
print(thisset)

""" 6. Write a python program to add elements of list to a setthisset = {"Python", "Django", "JavaScript"}
mylist = ["Java", "C"]"""

setthisset = {"Python", "Django", "JavaScript"}
mylist = ["Java", "C"]
setthisset.update(mylist)
print(setthisset)

"""7. Write a python program to remove last item of the given setthisset = {"Python", "Django", "JavaScript", “SQL”} """
setthisset = {"Python", "Django", "JavaScript", "SQL"}
setthisset.remove("SQL")
print(setthisset)

""" 8. Write a python program to delete the set completely."""
setthisset = {"Python", "Django", "JavaScript", "SQL"}
setthisset.clear()
print(setthisset)

"""  9. Write a python program to loop through the set and print valuesthisset = {"Python", "Django", "JavaScript", “SQL”}"""

setthisset = {"Python", "Django", "JavaScript", "SQL"}
for i in setthisset:
    print(i,end="  ")

""" 10. Write a python program to find the maximum and minimum value in a set."""
s1=set()
n=int(input("Enter the no. of value you want to enter : "))
print("Enter the no. one by one :")
while n:
    x=int(input())
    s1.add(x)
    n-=1
print(s1)
print(max(s1))
print(min(s1))