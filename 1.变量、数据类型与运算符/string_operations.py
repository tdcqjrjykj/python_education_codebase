# @Author : mcyj
# @Time : 2024/6/28 下午4:31

"""
字符串操作：连接、切片、查找、替换
连接：使用+运算符连接字符串。
切片：使用[start:stop:step]获取字符串的子串。
查找：使用find()或index()方法查找子串的位置。
替换：使用replace()方法替换字符串中的子串。
"""

# 字符串连接
str1 = "Hello"
str2 = "World"
concatenated_str = str1 + " " + str2
print("连接后的字符串:", concatenated_str)

# 字符串切片
sliced_str = concatenated_str[0:5]  # 切片得到 "Hello"
print("切片后的字符串:", sliced_str)

# 字符串查找
index_position = concatenated_str.find("World")
print("World 在字符串中的位置:", index_position)

# 字符串替换
replaced_str = concatenated_str.replace("World", "Python")
print("替换后的字符串:", replaced_str)