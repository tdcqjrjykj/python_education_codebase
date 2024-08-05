```python
#1.创建一个ndarray对象
import numpy as np
a = np.array([1,2,3])
print(a)
```

    [1 2 3]
    


```python
#2.创建一个二维ndarray
import numpy as np
a = np.array([[1,2], [3, 4]])#二维就是两层方括号
print(a)
```

    [[1 2]
     [3 4]]
    


```python
#3.指定生成的最小维度参数
import numpy as np
a = np.array([1,2,3,4], ndmin = 2)#传入一维数组,但指定生成的最小维度是2
print(a)#输出变成了两个方括号,二维数组
```

    [[1 2 3 4]]
    


```python
#4.dtype参数
import numpy as np
a = np.array([1,2,3], dtype = complex)#指定数据类型为复数
print(a)#输出为复数添加了虚部
```

    [1.+0.j 2.+0.j 3.+0.j]
    
