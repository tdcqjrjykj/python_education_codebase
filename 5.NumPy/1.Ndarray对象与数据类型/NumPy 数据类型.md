```python
#1定义一个int32类型
import numpy as np
dt = np.dtype(np.int32)
print(dt)
```

    int32
    


```python
#2int8,int16,int32,int64可用字符串'i1','i2','i4','i8'代替
import numpy as np
dt = np.dtype('i8')
print(dt)
```

    int64
    


```python
#3字节序标注
import numpy as np
dt = np.dtype('<i2')
print(dt)
```

    int16
    


```python
#4创建结构化数据类型
import numpy as np
dt = np.dtype([('age', np.int8)])
print(dt)
```

    [('age', 'i1')]
    


```python
#5将数据类型赋值给ndarray对象
import numpy as np
dt = np.dtype([('age',np.int8)])#数据字段的名称为age,转换为字节
a = np.array([(10,),(20,),(30,)], dtype = dt)
print(a)
```

    [(10,) (20,) (30,)]
    


```python
#6字段名可用于存取实际的列
import numpy as np
dt = np.dtype([('age',np.int8)])
a = np.array([(10,),(20,),(30,)], dtype = dt)
print(a['age'])
```

    [10 20 30]
    


```python
#7结构化数据类型student
import numpy as np
student = np.dtype([('name','S20'), ('age', 'i1'), ('score', 'f4')])
print(student)
```

    [('name', 'S20'), ('age', 'i1'), ('score', '<f4')]
    


```python
#8将student数据类型给到ndarray对象
import numpy as np
student = np.dtype([('name','S20'), ('age', 'i1'), ('score', 'f4')])
a = np.array([('mcyj', 18, 100), ('tdcq', 30, 99)], dtype = student)
print(a)
```

    [(b'mcyj', 18, 100.) (b'tdcq', 30,  99.)]
    


```python
#8将student数据类型给到ndarray对象
import numpy as np
student = np.dtype([('name','S20'), ('age', 'i1'), ('score', 'f4')])
a = np.array([('mcyj', 18, 100), ('tdcq', 30, 99)], dtype = 'a')
print(a)
```

    [[b'mcyj' b'18' b'100']
     [b'tdcq' b'30' b'99']]
    


```python

```
