"""1. Write a python script to print MySirG 5 times on the screen """
x="MySirG"
i=0
while i<5:
    print(x)
    i+=1

""" 2. Write a python script to print first 10 natural numbers """
i=0
while i<10:
    print(i+1,end=" ")
    i+=1

""" 3. Write a python script to print first 10 natural numbers in reverse order."""
i=10
while i>0:
    print(i,end=" ")
    i-=1
""" 4. Write a python script to print first 10 odd natural numbers """
i=0
count=0
while count!=10:
    if i%2!=0:
        print(i,end=" ")
        count+=1
    i+=1

# OR
i=0
while i<20:
    if i%2!=0:
        print(i,end=" ")
    i+=1

""" 5. Write a python script to print first 10 odd natural numbers in reverse order """

i=20
while i>0:
    if i%2!=0:
        print(i,end=" ")
    i-=1

"""6. Write a python script to print first 10 even natural numbers """
i=1
count=0
while count!=10:
    if i%2==0:
        print(i,end=" ")
        count+=1
    i+=1
""" 7. Write a python script to print first 10 even natural numbers in reverse order"""
i=20
while i>0:
    if i%2==0:
        print(i,end=" ")
    i-=1

"""8. Write a python script to print squares of first 10 natural numbers """

i=0
while i<10:
    print((i+1)**2,end=" ")
    i+=1

""" 9. Write a python script to print cubes of first 10 natural numbers """

i=0
while i<10:
    print((i+1)**3,end=" ")
    i+=1

""" 10. Write a python script to print first 10 multiples of 5"""
i=0
while i<10:
    print((i+1)*5,end=" ")
    i+=1