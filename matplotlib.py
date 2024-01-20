#!/usr/bin/env python
# coding: utf-8

# In[11]:


import matplotlib.pyplot as plt
import numpy as np
x = np.array([1, 10])
y = np.array([1,10])
plt.plot(x, y)
plt.show()


# In[12]:


import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([6,7])
ypoints = np.array([10,12])
plt.plot(xpoints,ypoints,)
plt.show


# In[13]:


import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([6,7])
ypoints = np.array([10,12])
plt.plot(xpoints,ypoints, 'o')
plt.show


# In[49]:


import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([6,7,2,12])
ypoints = np.array([10,12,12,23])
plt.plot(xpoints,ypoints,marker = 'o')
plt.show


# In[18]:


import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10, 5, 7])

plt.plot(ypoints)
plt.show


# In[44]:


import matplotlib.pyplot as plt
plt.plot([1,3,4,5]),([6,7,8,9])
plt.title("JAMSHAID'S DATA")
plt.xlabel("This is X")
plt.ylabel("This is Y")
plt.show


# In[19]:


import matplotlib.pyplot as plt
from matplotlib import style
style.use ('ggplot')
x = [1,2,3,]
y = [17,18,19]
x1 = [11,21,31]
y1 = [61,71,81]
plt.plot(x,y,label = "first",linewidth= 3)
plt.plot(x1,y1,label = "second",linewidth = 5)
plt.legend()
plt.show()


# In[32]:


import matplotlib.pyplot as plt
from matplotlib import style

x = ([1,21,2])

y = ([10,20,25])
plt.scatter(x,y,label = "first")

plt.show()


# In[55]:


import matplotlib.pyplot as plt
x =[1,2,3]
y = [33,72,63]

plt.plot(x,y,'o:r')
plt.show()
    


# 

# In[56]:


import matplotlib.pyplot as plt
x =[1,2,3]
y = [33,72,63]

plt.plot(x,y,'o:y')
plt.show()


# In[59]:


import matplotlib.pyplot as plt
x =[1,2,3]
y = [33,72,63]

plt.plot(x,y,marker = 'o', ms = 20)
plt.show()


# In[65]:


import matplotlib.pyplot as plt
x =[1,2,3]
y = [33,72,63]

plt.plot(x,y,marker = '*', ms = 20, color = "black",mfc = 'red',mec= 'orange')
plt.show()


# In[66]:


import matplotlib.pyplot as plt
x =[1,2,3]
y = [33,72,63]

plt.plot(x,y,marker = 'o',linestyle = 'dotted')
plt.show()


# In[70]:


import matplotlib.pyplot as plt
x =[1,2,3]
y = [33,72,63]

plt.plot(x,y,marker = 'o',linestyle = 'dashed')
plt.grid(axis = 'x')
plt.show()


# In[75]:


import matplotlib.pyplot as plt
x =[1,2,3]
y = [33,72,63]

plt.plot(x,y,marker = 'o',linestyle = 'dashed')
plt.grid(axis = 'y')
plt.xlabel("x axis data")
plt.ylabel("y axis data")
plt.title("Jamshaid data")
plt.suptitle=("jamo")
plt.show()


# In[1]:


import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(170, 10, 250)

plt.hist(x)
plt.show() 


# In[2]:


import numpy as np
x = np.random.normal(150,10,250)
print(x)


# In[4]:


import matplotlib.pyplot as plt
import numpy as np 
x = np.random.normal(10,70,100)

plt.hist(x)
plt.show()


# In[9]:


import matplotlib.pyplot as plt
import numpy as np
mylable = ["apple","banana","orange","grapes"]
y = np.array([35, 25, 25, 15])

plt.pie(y,labels = mylable)
plt.show() 


# In[14]:


import matplotlib.pyplot as plt 
y = ([10,30,40])
x = ([20,30,60])
mylabels = ["EARTH","WATER","NO OF PEOPLE"]

plt.pie(y,labels = mylabels,startangle = 90)
plt.show()


# In[19]:


import matplotlib.pyplot as plt 
y = ([10,30,40])
x = ([20,30,60])
mylabels = ["EARTH","WATER","NO OF PEOPLE"]
myexplode = [0.2, 0,0]
plt.pie(y,labels = mylabels,startangle = 90,explode = myexplode)
plt.show()


# In[21]:


import matplotlib.pyplot as plt 
y = ([10,30,40])
x = ([20,30,60])
mylabels = ["EARTH","WATER","NO OF PEOPLE"]
myexplode = [0.2, 0,0]
plt.pie(y,labels = mylabels,startangle = 90,explode = myexplode,shadow= True)

plt.show()


# In[32]:


import matplotlib.pyplot as plt 
y = ([10,30,40])
x = ([20,30,60])
mylabels = ["EARTH","WATER","NO OF PEOPLE"]
myexplode = [0.2, 0,0]
plt.pie(y,labels = mylabels,startangle = 90,explode = myexplode,shadow= True,colors = "mycolors" )
mycolors = ["red","orange","pink"]
plt.legend(title = "graph")
plt.show()


# In[34]:


import matplotlib
print(matplotlib.__version__)


# In[ ]:




