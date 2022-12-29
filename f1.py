#import math
print("bmjhadjvc ehajsgvhc")
fo = 2.30
print("float value of f is: ",fo)
p=type(fo)
print(p)
print(type(p))
num=[10,20,30]
s=sum(num,100)
print(s)
print(pow(10,2))

#print addition os multiple numbers
print(10+20)
#print(sum(20,30))

#print length of string
print(len("rafi"))

#print "Python is Amezing
print("\n \t Python is Amezing")

#read two strings in two different variables, concat them and print
s1=" Rafi"
s2="Rebal"
print(s2+ s1)

#print remainder, quotient of the divison.Print both integer and float
a=10%20
b=10/20
c=a+b
print(c)

#print type() function varioua kinds of variables
print(type(10))
print(type("rafi"))
print(type(10.1))
print(type(1000.101010101))
print("Rebal Rafi"*23," \n rafi"*10)

#complex value
c=10+20j
print(type(c))

#copying
import copy
l1=[10,20]
l2=copy.deepcopy(l1)
l3.copy.copy(l1)
print(id(l2))
print(id(l1))

#data types in python
a=10
b=20.10
c=True
d="strings are here"
dic={"k1":10,"k2":20}
li=[10,20,30]
tup=(10,20,30,"30")
set={10,20,30}
print(dic)
print(li)
print(tup)
print(set)

#Every object stored in a memory
#---variables are storing only one value at a time, if i want to store multiple values in a single variable then i choose collections

"""
---- Data types Brief-------------------
List is a Collection which is orderd and changeable. Allows duplicate members.[]
Tuple is a collection which is odered and Unchangeable. Allows duplicate members.()
Set is a collection which is unodeted, unchangeable*, and unindexed. No duplicate members.{}
Dictionary is a collection which is unodered** and changeable. No duplicate members.{}
"""

#Print id of data
print(id("Rafi"))

#referring the same object
list_a=[1,2,3,5]
list_b=list_a

print(id(list_a))
print(id(list_b))

list_b[3]=4

print(list_a)
print(list_b)

#Compound assignment example
list_a=[1,2]
list_b=list_a
list_a=list_a+[6,7]

print(str(list_a))
print(str(list_b))

list_a=[1,2]
list_b=list_a
list_a+=[6,7]

print(str(list_a))
print(str(list_b))

list_a[1,2]
list_b=[3,list_a]
list_a[1]=4

print(list_a)
print(list_b)

#Splitting a string

#str_var.split(seperator), default seperator is whitspacew
#multiple whitespaces are considered as single whitespace
numbers="1 2 3   4"
num_list=numbers.split()
print(num_list)

numbers="1  2 3 4"
num_list=numbers.split(',')
print(num_list)

string_a="Python is stronishing"
list_a=string_a.split('a')
print(list_a)

list_a=['Python is','progr','mmingl','ngu','ge']
string_a="a".join(list_a)
print(string_a)

list_a=list(range(4))
print(list_a)

s="program"
s1=s[6:0:-2]
print(s1)


#negative indexing
#Using negative index returns the nth item from the end of the list
#list item in the list can be accessed with index -1
list_a=[1,2,3,4,5]

print(list_a[4])
print(list_a[-1])

#slicing
#To extract part of object
list_a=[1,2,3,4,5]

list_b=list_a[-5:-1]
print(list_b)

#Negative Step Size
#Negative Step determines the decrement between each index for slicing. Start> End
list_a=[5,4,3,2,1]

list_b=list_a[4:0:-2]
print(list_b)

list_b=list_a[1:4:-1]
print(list_b)

list_b=list_a[::-1]
print(list_b)

#slicing & indexing strings
string_1="program"
string_2=string_1[6:0:-2]
print(string_2)

#Take two integers M and N,write a program to create a list with element M repeated ny N times.
#Write a program to read N inputs and prints a list containing the first and last three inputs.

a=[1,2,3,4,5]
print(a[0:2]+a[-2:])

