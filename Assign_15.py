"""1. Write a python script to create a String in 3 different possible ways """

print("1st way is :")
s1='Amit kumar'
print(s1)
print("2nd way is :")
s2="DiyA kumari"
print(s2)
print("3rd way is ")
s3='''Amit'''
print(s3)

""" 2. Write a python script to Get the characters from the start to position 5 (Given String
“iNeuron” using the slice syntax)"""
s1="iNeuron"
print(s1[5:])

""" 3. Write a python script to Get the characters from position 2 to position 5 (Given String
“Hello Learners” using the slice syntax)"""
s1="Hello Learners"
print(s1[2:6:])

""" 4. Write a python script to demonstrate String Concatenation adding space in between (
Given Strings a=”Learning” b=”Python” )"""
a="Learning"
b="Python"
c=" "
print(a+c+b)

""" 5. Write a python script to get the count of total number of characters in String a=
“iNeuron”"""
a="iNeuron"
x=0
for i in a:
    x+=1
print(x)

""" 6. Write a python script to reverse a String. (“iNeuron”)"""
a="iNeuron"
print(a[::-1])

""" 7. Write a python script to determine whether a string contains a specific substring."""

s=input("Enter a string :\n")
x=input("Enter a substring to check wherter it is in string or not:\n ")
print(True if x in s else False )

""" 8. Write a python script to check if a string contains only numbers."""
s=input("Enter a string :\n")
print(s.isdigit())


"""9. Write  a python script to check if a string contains only characters of the alphabet."""
s=input("Enter a string :\n")
print(s.isalpha())

""" 10. Write a python script to convert an integer to a string."""

x=int(input("Enter a integer to convert that in string \n"))
print(x,type(x))
y=str(x)
print(y,type(y))