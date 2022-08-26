""" 
1. Write a python script to convert a number into str type """
x="45"
y=23
z=str(y)
print(type(x))
print(type(y))
print(type(z))

""" 2. Write a python script to print Unicode of the character ‘m’"""


print(ord("m"))



""" 3. Write a python script to print character representation of a given unicode 100."""

print(chr(100))


""" 4. Write a python script to print any number and its binary equivalent"""

A=22
B=37
print(A,bin(A))
print(B,bin(B))

""" 5. Write a python script to print any number and its octal equivalent."""


print(A,oct(A))
print(B,oct(B))

""" 6. Write a python script to print any number and its hexadecimal equivalent """

print(A,hex(A))
print(B,hex(B))

"""  7. Write a python script to store binary number 1100101 in a variable and print it in
decimal format """

M=0b1100101
print(M)

""" 8. Write a python script to store a hexadecimal number 2F in a variable and print it in
octal format """

N=0x2F
print(N)

""" 9. Write a python script to store an octal number 125 in a variable and print it in binary
format."""

O=0o125
print(O)

""" 10. Write a python script to add two numbers 25 (in octal) and 39 (in hexadecimal) and
display the result in binary format."""

G=0o25
# print(G)
H=0x39
# print(H)
I=G+H
print(I,bin(I))