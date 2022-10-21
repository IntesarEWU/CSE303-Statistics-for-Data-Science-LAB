#%%
#LABHW 01

a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
c = b*a
print('1st input: ',a,'\n2nd input: ',b)
if (c > 1000):
    print(a+b)
else: 
    print(c)

#%%
#LABHW 02

import math
radius = float(input('Enter radius of a circle: '))
print('Radius: ',radius)
area = math.pi*radius*radius
perimeter = 2*math.pi*radius
print('Aria: ',area,'\nPerimeter: ',perimeter)

#%%
#LABHW 03

p = float(input("Enter the principal amount: "))
r = float(input("Enter the rate of interest: "))
t = float(input("Enter the number of years: "))
print('principal: ',p,'\nRate of interest: ',r,'\nNumber of years:',t)
ci =  p * (pow((1 + r / 100), t)) 

print("Compound interest : ",ci)

#%%
#LABHW 04

n = int(input("Enter Any Positive Number: "))
print("Entered Number: ",n)
sum=0
for i in range(n):
    i=i+1
    sum=sum+(i*i)
print(sum)

#%%
#LABHW 05

def prime_find_2019160043(N):
    for x in range(2,N):
        if(N%x == 0):
            return 'Not Prime'
        else:
            return 'prime'
N = int(input('Enter a number: '))
print('Entered Number: ',N)
print(N,'is',prime_find_2019160043(N))

#%%
#LABHW 06

def fibonacci(n):
    if(n==0):
        return 0
    elif(n==1 or n==2):
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
n=int(input('Enter integer: '))
print('Entered Number: ',n)
print(n,'\bth Fibonacci:',fibonacci(n))

#%%
#LABHW 07

list = [1,2,3]
sum = 0 
for x in list:
    sum=sum+x
print(sum)

#%%
#LABHW 08

list = [1,3,1,3,1,3]
sum=0
j=0
for x in list:
    if j % 2 == 0:
        sum+=x
    j+=1
print(sum)

#%%
#Python String capitalize(): Converts first character to Capital Letter

str = 'this is a line'
print(str.capitalize())

#%%
#Python String casefold(): converts to case folded strings

str = 'This is a LINE'
print(str.casefold())

#%%
#Python String center(): Pads string with specified character

str = 'This is a LINE'
print(str.center(21, "#"))

#%%
#Python String count(): returns occurrences of substring in string

str = 'This is a LINE'
print(str.count('is'))
print(str.count('is',4))

#%%
#Python String encode(): returns encoded string of given string

str = 'This is a LINE'
print(str.encode())

#%%
#Python String endswith(): Checks if String Ends with the Specified Suffix

str = 'This is a LINE'

print('Text ends with "E": ',str.endswith("E"))
print('Text ends with ".": ',str.endswith("."))

#%%
#Python String expandtabs(): Replaces Tab character With Spaces

str = 'T\this is  a LINE'

print('Text ends with "E": ',str.expandtabs(0))
print('Text ends with "E": ',str.expandtabs()) #by default 8
print('Text ends with "E": ',str.expandtabs(16))

#%%
#Python String find(): Returns the index of first occurrence of substring

str = 'This is  a LINE'

print(str.find("a"))

#%%
#Python String format(): formats string into nicer output

a= int(input("Enter a number: "))
b= input('Enter any string: ')

print('1st input "{}"\n2nd input "{}"'.format(a,b))

#%%
#Python String format_map(): Formats the String Using Dictionary

a = {'x': 'Intesar','y': 'Khan'}

print("{x}'s last name is {y}".format_map(a))

#%%
#Python String index(): Returns Index of Substring

str = 'This is a line'

print("position of 'a': ",str.index("a"))

#%%
#Python String isalnum(): Checks Alphanumeric Character

str = input("Enter anything: ")
print('You Entered: ',str)
print('Alphanumeric: ',str.isalnum())

#%%
#Python String split(): Splits String from Left

str = input("Enter anything: ")
print('You Entered: ',str)
list = str.split()
print(list)

#%%
#Python String join(): Returns a Concatenated String

list = ('This','is','a','line')

print(" ".join(list))

#%%
#Python String replace(): Replaces Substring Inside

str = 'This is a Line'
print('Before Replace: ',str)
str = str.replace('Line', 'sentence')
print('After Replace: ',str)

#%%
#Python String strip(): Removes Both Leading and Trailing Characters

str = 'This is a Line'
print(str.strip('This'))
str1 = 'T'
print(str.strip(str1))
