```python
#1.numpy.empty
import numpy as np

x = np.empty([2,2], dtype = 'i1')
print(x)#输出的结果为未初始化的随机值
```

    [[ -70 -122]
     [   2 -113]]
    


```python
#2.numpy.zeros
import numpy as np

x = np.zeros(6)
print(x)#默认的数据类型为浮点型

y = np.zeros((6), dtype = int)#设置为整型
print(y)

z = np.zeros((3,3), dtype = [('x', 'i1'), ('y', 'i4')])
print(z)
```

    [0. 0. 0. 0. 0. 0.]
    [0 0 0 0 0 0]
    [[(0, 0) (0, 0) (0, 0)]
     [(0, 0) (0, 0) (0, 0)]
     [(0, 0) (0, 0) (0, 0)]]
    


```python
#3.numpy.ones
import numpy as np
 
x = np.ones(5) #默认的数据类型为浮点型
print(x)
 
y = np.ones([1,1], dtype = int)
print(y)
```

    [1. 1. 1. 1. 1.]
    [[1]]
    


```python
#4.numpy.zeros_like
import numpy as np
 
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

zeros_arr = np.zeros_like(arr)
print(zeros_arr)
```

    [[0 0 0]
     [0 0 0]
     [0 0 0]]
    


```python
#5.numpy.ones_like
import numpy as np
 
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])# 创建一个 3x3 的二维数组
 
ones_arr = np.ones_like(arr)# 全1二维数据,和array大小一样3x3
print(ones_arr)
```

    [[1 1 1]
     [1 1 1]
     [1 1 1]]
    


```python
#6.numpy.asarray
import numpy as np 
 
x1 = [1,2,3] #将列表转换为ndarray
a1 = np.asarray(x1)
print(a1)

x2 = (4,5,6) #将元组转为ndarray
a2 = np.asarray(x2)
print(a2)

x3 = [(1,2,3), (4,5)]#将元组列表转换为ndarray
a3 = np.asarray(x3, dtype = object)#类型为object防止大小不一致报错
print(a3)
```

    [1 2 3]
    [4 5 6]
    [(1, 2, 3) (4, 5)]
    


```python
#7.numpy.frombuffer
import numpy as np 
 
s =  b'Hello World' 
a = np.frombuffer(s, dtype =  'S1')  
print (a)
```

    [b'H' b'e' b'l' b'l' b'o' b' ' b'W' b'o' b'r' b'l' b'd']
    


```python
#8.numpy.fromiter
import numpy as np 
  
list=range(5)# 使用 range 函数创建列表对象
it=iter(list)
 
x=np.fromiter(it, dtype=float)# 使用迭代器创建 ndarray 
print(x)
```

    [0. 1. 2. 3. 4.]
    


```python
#9.numpy.arange
import numpy as np
 
x1 = np.arange(5)  
print(x1)
x2 = np.arange(5, dtype = float)#设置为浮点型  
print(x2)
x3 = np.arange(10,20,2)#步长设置为2  
print(x3)
```

    [0 1 2 3 4]
    [0. 1. 2. 3. 4.]
    [10 12 14 16 18]
    


```python
#10.numpy.linspace
import numpy as np
a1 = np.linspace(1,10,10)#公差为1
print(a1)

a2 = np.linspace(1,1,10)#公差为0
print(a2)

a3 = np.linspace(10, 20, 5, endpoint =  False)#不包含20，公差为2  
print(a3)

a4 =np.linspace(1,10,19,retstep= True)#显示公差0.5
print(a4)

b =np.linspace(1,10,10).reshape([10,1])# 结合reshape使用
print(b)
```

    [ 1.  2.  3.  4.  5.  6.  7.  8.  9. 10.]
    [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
    [10. 12. 14. 16. 18.]
    (array([ 1. ,  1.5,  2. ,  2.5,  3. ,  3.5,  4. ,  4.5,  5. ,  5.5,  6. ,
            6.5,  7. ,  7.5,  8. ,  8.5,  9. ,  9.5, 10. ]), 0.5)
    [[ 1.]
     [ 2.]
     [ 3.]
     [ 4.]
     [ 5.]
     [ 6.]
     [ 7.]
     [ 8.]
     [ 9.]
     [10.]]
    


```python
#11.numpy.logspace
import numpy as np

a1 = np.logspace(1.0,  2.0, num =  10)  # 默认底数是 10，数值从10^1~10^2
print(a1)

a2 = np.logspace(0,9,10,base=2)#设置底数为2,数值从2^0~2^9
print(a2)
```

    [ 10.          12.91549665  16.68100537  21.5443469   27.82559402
      35.93813664  46.41588834  59.94842503  77.42636827 100.        ]
    [  1.   2.   4.   8.  16.  32.  64. 128. 256. 512.]
    


```python

```
