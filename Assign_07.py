""" 1. Write a python script to display the number of days in a given month number. """


x=eval(input("Enter the month name to display the numbers of the days  :"))
match x:
    case 1:
        print("31")
    case 2:
        print("28 or 29")
    case 3:
        print("31")
    case 4:
        print("30")
    case 5:
        print("31")
    case 6:
        print("30")
    case 7:
        print("31")
    case 8:
        print("31")
    case 9:
        print("30")
    case 10:
        print("31")
    case 11:
        print("30")
    case 12:
        print("31")
    case _:
        print("Invalid ")

""" 2. Write a menu driven program to perform following operations - Addition, Subtraction,
Multiplication, Division """
print("1. Additon \n2. Subtraction \n3. Multiplication\n4. Division\n5. Exit")
x=int(input("Choose from 1-5 :"))
a=int(input("Enter the first operand : "))
b=int(input("Enter the second operand :"))
match x:
    case 1:
        print(a+b)
    case 2:
        print(a-b)
    case 3:
        print(a*b)
    case 4:
        print(a/b)
    case 5:
        print("Thanku")
    case _:
        print("Invalid option ")

""" 3. Write a menu driven program with the following options:
a. Check whether a given set of three numbers are lengths of an isosceles
triangle or not
b. Check whether a given set of three numbers are lengths of sides of a right
angled triangle or not
c. Check whether a given set of three numbers are equilateral triangle or not
d. Exit."""

print("a. To check the isosceles triangle b. To check the right angled triangle c. To check the equilateral triangle d. Exit")
n=str(input("Choose character form a-d :"))
match n:
    case "a" :
        print("Enter the side of the triangle a,b,c respectively :")
        x=int(input())
        y=int(input())
        z=int(input())
        if x==y or y==z or z==x :
            print("the given lengths are the sides of the isosceles triangle")
        else:
            print("the given lengths are NOT the sides of the isosceles triangle")
    case "b" :
        print("Enter the side of the triangle a,b,c respectively :")
        x=int(input())
        y=int(input())
        z=int(input())
        if x**2==y**2+z**2 or y**2==x**2+z**2 or z**2==x**2+y**2 :
            print("The give lengths are the sides of the right angled triangle")
        else :
            print("The given lengths are NOT the sides of thr right angled triangle ")
    case "c":
        print("Enter the side of the triangle a,b,c respectively :")
        x=int(input())
        y=int(input())
        z=int(input())
        if x==y==z:
            print("The given lengths are the sides of the equilaleral triangle ")
        else :
            print("The given length are NOT the sides of the equilateral triangle")

    case "d":
        print("Thanku")
    case _:
        print("Invalid option")

""" 4. Write a program which takes user’s age and display the category of person. Age
below 10 years- Kid, Age below 20 - Teen, Age below 40 - young, Age below 60 -
Experienced, Age above or equal 60 - Senior Citizen."""

x=int(input("Enter the age of the person :"))
match x:
    case x if x<10 :
        print("Kids")
    case x if x>=10 and x<20 :
        print("Teen")
    case x if x<40 and x>=20:
        print("Young")
    case x if x<60 and x>=40:
        print("Experienced")
    case x if x>=60:
        print("Senior Citizen")

"""5. Write a program which takes a number from user. Print Saurabh Shukla if the number
is even, print Prateek Jain if the number is negative odd number and print Aditya
Choudhary if number is positive odd number."""

x=int(input("Enter a number :"))
match x:
    case x if  x%2==0 :
        print("Saurabh Shukla")
    case x if x<0 and x%2!=0:
        print("Prateek Jain")
    case x if x>=0 and x%2!=0:
        print("Aditya Choudhary")

"""6. Write a python program to check whether a given string is a multiword string or single
word string using match case statement"""

x=input("Enter string :")
x=x.strip()  # Remove the spaces from the starting and ends  
match x:
    case x if " " in x:
        print(x," is multistring  ")
    case x if " " not in x:
        print(x," is singlestring ")

""" 7. Write a python program to check whether a given number is positive, negative or
zero using match case statement""" 

x=int(input("Enter a number :"))
match x:
    case x if x>0:
        print("Positive")
    case x if x<0:
        print("Negative")
    case x if x==0:
        print("Zero")

""" 8. Write a python script to check whether two given strings are identical, first string
comes before the second in dictionary order or first string comes after the second
string in dictionary order using match case statement"""
print("Enter the two strings ")
x,y=input(),input()
match (x,y):
    case (x,y) if x==y:
        print(x,y," are identical "  )
    case (x,y) if x>y:
        print(x," is greater than ",y)
    case(x,y) if x<y:
        print(y," is greater than ",x)


""" 9. Write a python script to check whether a given year is
a. Non century leap year
b. Century leap year
c. Non century non leap year
d. Century non leap year"""


print("Enter the a year : ")
x=int(input())
match x:
    case x if x%400!=0:
        print(x,"Non century leap year")
    case x if x%400==0:
        print(x,"is century leap year")
    case x if x%400!=0 and x%4!=0:
        print(x,"is non century non leap year")
    case x if x%100==0:
        print(x,"is century non leap year")

"""10. Write a program to display day name on the basis of user’s liking of a colour. Ask
user for his favorite colour. User can answer in a sentence like “I like red colour”.
Assuming all colour name entered by user is in lowercase. Use match case to display
day name associated with the colour.
a. Yellow - Monday
b. Blue - Tuesday
c. Orange - Wednesday
d. White - Thursday
e. Black - Friday
f. Red - Saturday
g. All other colours - Sunday """

print("Enter the colour name you like ")
x=input()
match x:
    case x if x in ['yellow','blue','orange','white','black','red']:
        match x:
            case 'yellow':
                print(x,"- Monday")
            case 'blue':
                print(x,"- Tuesday")
            case 'orange':
                print(x,"- Wednesday")
            case 'white':
                print(x,"- Thursday")
            case 'black':
                print(x,"- Friday")
            case 'red':
                print(x,"-Saturday")
    case x if x not in ['yellow','blue','orange','white','black','red']:
        print(x,"- Sunday")
