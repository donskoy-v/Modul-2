#!/usr/bin/env python
# coding: utf-8

# In[ ]:


a = int(input())
b = int(input())
c = int(input())
if a == b and b == c and a == c:
    print("three are equal")
elif a == b or b == c or a == c:
    print('two are equal')
else:
    print('no matches')


# In[ ]:


x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

if x1 == x2 or y1 ==y2:
    print('OK')
    
else:
    print('FAIL')


# In[ ]:


password = input()

if len(password) >= 8 and not password.isupper() and not password.islower():
    print("acceptable")
    
else:
    print("not correct")


# In[ ]:


password = input()

if len(password) >= 8 and not password.isupper() and not password.islower():
    print("acceptable")
    
else:
    print("not correct")


# In[ ]:




