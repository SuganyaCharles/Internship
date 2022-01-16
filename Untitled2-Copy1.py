#!/usr/bin/env python
# coding: utf-8

# In[3]:


X =8 
y = 5
r = X % y

print (r)


# In[4]:


X= 2//3


# In[5]:


print (X)


# In[6]:


Y=6<<2


# In[7]:


print (Y)


# In[8]:


6&2


# In[9]:


6|2


# In[10]:


i=18

if i<13:
    print ('less than 13')
    
elif i >15:
    print ('more than 15')
    
else:
    print ('15 or more')


# In[15]:


num = int(input("Enter a Number"))

if num > 1:
    for i in range (3, num):
        if (num % i) ==0:
            print (num, "is NOT a prime number")
            break
            
    else:
        print (num, "is a PRIME number")
        
elif num == 0 or 1:
    print (num, "is a neither prime or composite number")
 
else: 
    print (num, "is Not a prime number it is a composite number")


# In[12]:


str=input ("Enter a String")

l=len(str)-1

s=""

for i in range (1,-1,-1):
    s+=str[i]
if s==str:
    print("Palindrome!")
    
else:
    print ("Not a Palindrome!")


# In[ ]:





# In[ ]:





# In[ ]:




