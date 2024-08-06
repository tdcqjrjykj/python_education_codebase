```python
#1.ndarray.ndim
import numpy as np 

a = np.arange(6)#一维数组0~5
print(a.ndim)
print(a)

b = a.reshape(1,2,3)#三维数组(一层,两行,三列)
print(b.ndim)
print(b)
```

    1
    [0 1 2 3 4 5]
    3
    [[[0 1 2]
      [3 4 5]]]
    


```python
#2.ndarray.shape
import numpy as np  
 
a = np.array([[1,2,3],[4,5,6]])  
print (a.shape)
```

    (2, 3)
    


```python
#2.ndarray.shape
import numpy as np 
 
a = np.array([[1,2,3],[4,5,6]]) 
a.shape =  (3,2)  
print (a)
```

    [[1 2]
     [3 4]
     [5 6]]
    


```python
#3.reshape
import numpy as np 
 
a = np.array([[1,2,3],[4,5,6]]) 
b = a.reshape(2,3)  
print (b)
```

    [[1 2 3]
     [4 5 6]]
    


```python
#4.ndarray.itemsize
import numpy as np 
   
x = np.array([1,2,3,4,5], dtype = np.int8)#一个字节
print (x.itemsize)
 
y = np.array([1,2,3,4,5], dtype = np.int64)#8个字节
print (y.itemsize)
```

    1
    8
    


```python
#5.ndarray.flags
import numpy as np 
 
x = np.array([1,2,3,4,5])  
print (x.flags)
```

      C_CONTIGUOUS : True
      F_CONTIGUOUS : True
      OWNDATA : True
      WRITEABLE : True
      ALIGNED : True
      WRITEBACKIFCOPY : False
    
    


```python

```
