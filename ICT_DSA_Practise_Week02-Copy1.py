#!/usr/bin/env python
# coding: utf-8

# In[4]:


import math as math
rad = float(input("enter the radius"))
area=math.pi * rad**2
print("area is %.3f:"%area)


# In[5]:


name=input("Enter the name ")
roll_number=input("Enter the rollno ")
mark=input("Enter the mark ")

print("Name :",name)
print("Roll No :",roll_number)
print("Marks :",mark)


# In[14]:


print("Enter the numbers :")

numb_list=[]

for i in range(0,5):
    num =input()
    numb_list.append(num)

print("largest number is :",max(numb_list))


# In[25]:


test_str=input("enter the string ")
all_freq = {}
  
for i in test_str:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1
print ("Count of all characters is :\n "
                                        +  str(all_freq))


# In[40]:


tuple1 = (11, 22, 33, 44, 55, 66) 
#tuple2=tuple1[3:-1]
#tuple2
tuple3 = tuple1[-3:-1]
tuple3


# In[ ]:


for i in range(1,11):
    if i==1:
        print("Current Number 1 Previous Number 0 Sum: 1 ")
    else:
        print ("Current Number ",i," Previous Number ",i-1," Sum: ",i+(i-1))


# In[61]:


a,b,c,d,e = input("enter 5 numbers :").split()

a= int(a)
b= int(b)
c= int(c)
d= int(d)
e= int(e)
list1=[a,b,c,d,e]

for i in list1:
    if i%5==0:
        print("numbers divisible by 5 are :",i)


# In[ ]:


# num = int(input("enter a number"))

flag=False

if num ==1:
    flag
elif num>1:
    for n in (2,num):
        if num % n==0:
            flag=True
        break
if flag:
    print("its not a prime number")
else:
    print("its a prime number")


# In[104]:


list1=[10,40,40,70]

list2=[]

for item in list1:
    list2.insert(0, item)
    
print (list2)
    

 
      




# In[107]:


num =int(input("enter no of rows :"))

for i in range(0,num):
    print("*"*i)


# In[109]:


a,b,c = input("enter thre numbers :").split()

a=int(a)
b=int(b)
c=int(c)

list1=[a,b,c]
print(max(list1))


# In[110]:


def exponent(base,exp):
    return base ** exp

a=int(input("enter the base :"))
b=int(input("enter the exponent : "))

exponent(a,b)


# In[111]:


def func1(n):
    sum=0
    for i in range(0,n):
        sum=sum+i**3
    return sum
num = int(input("enter  postve number :"))
func1(num)


# In[128]:


num = int(input("enter the number :"))

for i in range(num+1):
    print("*" *i)
for i in range (num+1,0,-1):
    print("*" *i)


# In[146]:


for i in range(1,11):
        if (i % 2==0 and i % 5 ==0):
            print("FizzBuzz",end=" ")
        elif i % 5 ==0:
            print("Buzz",end=" ")
        elif i % 2 == 0:
            print("Fizz",end=" ")
        else:
            print(i,end=" ")
       


# In[164]:


lis = [2,3,4,2,5,2,5,5,5]

cnt=0

for i in lis:
    freq=lis.count(i)
    #print(freq)
    if freq>cnt:
        cnt=freq
        num=i
print(num)


# In[165]:


lis=[2,1,3,1]

sum=0
for i in lis:
    cnt=i**2
    sum=sum+cnt
print(sum)
    


# In[166]:


for i in range(1,16):
    if i % 2 !=0:
        print(i,"-- odd")
    else:
        print(i,"-- even")


# In[169]:


def fact(num):
    sum=1
    for i in range(num,0,-1):
        sum=sum*i
    return sum

fact(5) 

