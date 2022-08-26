# 1. Write a python script to add comments and print “Learning Python” on screen

print('"Learning Python"')

""" 2. Write a python script to add multi line comments and print values of four variables,
each in a new line. Variable contains any values """

x=20
y="MySirG"
z=22
a="woW"
print(x,y,z,a,sep='\n')

""" # 3. Write a python script to print types of variables. Create 5 variables each of them
containing different types of data. (like 35, True, “MySirG”,5.46, 3+4j, etc)
"""

a=34
print(a,type(a))
b=True
print(b,type(b))
c=3.45
print(c,type(c))
d="Great DaY"
print(d,type(d))
e=3+4j
print(e,type(e))

""" 4. Write a python script to print the id of two variables containing the same integer
values. """

x=22
print(x,id(x))
y=22
print(y,id(y))

""" 5. Create four variables in a Python script and assign values of different data types to
them. Write a Python script to print value, its type and id of each variable """

a=34
print(a,type(a),id(a))
b=True
print(b,type(b),id(b))
c=3.45
print(c,type(c),id(c))
d="Great DaY"
print(d,type(d),id(d))
e=3+4j
print(e,type(e),id(e))

""" 6. Write a python script to print all the keywords """
import keyword
""" There is a keyword.py module ,we import here that module
    then that module name with dot to access that module
"""
print(keyword.kwlist) 

print(len(keyword.kwlist))


""" 7. On Python shell use help() function and display the list of keywords """

x="keywords"
help(x)

""" 8. Create two Python files A0.py and A1.py. Create a variable in A1.py and assign some
value to it. Write a python script to import A1 module in A0 and print value of the
variable created in A0.py """
""" In A1.py , There is a variables named 'x', x=20"""

import  A1
print(A1.x)

""" 9. Name the keywords, used as data in the Python script"""

# True , False, None

""" 10. Write a python script to display the current date and time. First create variables to
store date and time, then display date and time in proper format (like: 13-8-2022 and
9:00 PM )"""

from datetime import datetime
dt=datetime.today()
print(dt)
d1=dt.strftime("%d-%m-%Y and %I:%M %p")
print(d1)







