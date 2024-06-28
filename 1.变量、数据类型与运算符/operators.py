# @Author : mcyj
# @Time : 2024/6/28 下午4:30

"""
运算符：算术运算符、赋值运算符、比较运算符、逻辑运算符、位运算符、成员运算符、身份运算符。
算术运算符：如+、-、*、/、//（整除）、%（取余）**（幂）。
赋值运算符：=。
比较运算符：如==、!=、<、>、<=、>=。
"""

# operators_example.py

# 声明变量
a = 10
b = 5

# 算术运算符
print("加法:", a + b)  # +
print("减法:", a - b)  # -
print("乘法:", a * b)  # *
print("除法:", a / b)  # /
print("整除:", a // b)  # //
print("取余:", a % b)  # %
print("幂运算:", a ** 2)  # **

# 赋值运算符
c = a + b
print("赋值结果:", c)  # =

# 复合赋值运算符 (这里仅展示一个作为例子)
c += 10  # 等同于 c = c + 10
print("复合赋值结果:", c)

# 比较运算符
print("等于:", a == b)  # ==
print("不等于:", a != b)  # !=
print("大于:", a > b)  # >
print("小于:", a < b)  # <
print("大于等于:", a >= b)  # >=
print("小于等于:", a <= b)  # <=

# 逻辑运算符
print("逻辑与:", a > 5 and b < 10)  # and
print("逻辑或:", a < 5 or b > 5)  # or
print("逻辑非:", not (a == b))  # not

# 位运算符
# 注意：这些运算符在整数上操作，并改变它们的二进制表示
print("按位与:", a & b)  # &
print("按位或:", a | b)  # |
print("按位异或:", a ^ b)  # ^
print("按位取反:", ~a)  # ~ (注意按位取反的结果可能是负数，因为它是对整个整数进行的)
print("左移:", a << 1)  # <<
print("右移:", a >> 1)  # >>

# 成员运算符
list_example = [1, 2, 3, 4, 5]
print("成员测试（in）:", b in list_example)  # in
print("成员测试（not in）:", 6 not in list_example)  # not in

# 身份运算符
print("身份运算符（is）:", a is 10)  # is
print("身份运算符（is not）:", a is not 10.0)  # is not