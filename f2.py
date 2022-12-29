a=[1,2,3,4,5,6]
print(a[0:2]+a[-2:])


print(10==10)
print(10==10.0)
print(10==10.1)
print("abc"=="abc")
print("abc"=="ABC")
print("abc"=="abd")

print("abc"!="abc")
print("abc"!="abd")

print(10<20)
print(10>20)
print(10<=20)
print(10>=20)

l=786
n=123
l=str(l)
n=str(n)
print(l[0]<n[-1]

n=123
m=n%10
print(m)#3

x=786
y=x//100
print(i)#7
print(i<m)

m=70
p=60
c=60
if((m>=70 and p>=60 and c>=60) or (m+p+c>=180)):
    print("pass")
else:
    print("re read")

#slicing
a="Waterfall"
part=a[0:7:2]
print(part)

#isdigit
is_digit="123".isdigit()
print(is_digit)

#strip
mobile=" 93988 74960    "
mobile=mobile.strip()
print(mobile)

#replace
sentence="teh cat and teh dog"
sentence=sentence.replace("teh","the")
print(sentence)
#advanced for strip
sentence=" 93988 74960 "
sentence=sentence.replace(" ","")
print(sentence)

name=".Rafi."
name=name.strip(".")
print(name)

name=",...rafi,,...."
name=name.strip(",.")
print(name)

#starts with
Url="https://hcl.com"
Url=Url.startswith("https://")
print(Url)

#endswith
Gmail="pmrafi789@gmail.com"
Gmail=Gmail.endswith("@gmail.com")
print(Gmail)

#upper
Name="Rafi"
print(Name.upper())

#lower
Name="Rafi"
print(Name.lower())

Code="rafi shooo"
code="rafi"
print(Code.__contains__(code))

one="rafi"
two="saho"
one,two=two,one
print("two is ",two)
print("one is ",one)

import re
st1="rafi"
p=re.findall("[a-z]",st1)
print(p)
print(re."[a-z]" in st1)


l=10
m=[23]
print(m*l)


#take a  list,youre program should create new list with all the elements in existing list that are greater than given list
l=[1,2,3,7,23,45,18]
m=[]
n=int(input("enter a number"))
for i in l:
    if n<=i:
       m.append(i)
print(m)

s=[32,2,3,4,5]
print(s)
t=[]
t = [1,2,3,4,5]
#intExample = t[0]
i = [12,13,14]
t += i
print(t)
#x = list(t[0])
#print(x)

#reverse each string in list, after converting string into list.
s=input("enter a string: ")
x=s.split()
print(x)
z=[]
for i in x:
    a=i[::-1]
    z.append(a)
print(z)


i=123
#j=[]
#j.append(i)
#print(j)
print([i])
l=















