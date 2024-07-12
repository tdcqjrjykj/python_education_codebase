# @Author : mcyj
# @Time : 2024/7/12 上午11:45

# 全局变量
def my_function():
    local_var = "I am a local variable"

my_function() # 输出: I am a local variable
# print(local_var) # 这会引发错误, 因为 local_var 只在函数内部定义
# 尝试访问 local_var 会导致 NameError，因为它只在函数内部定义

# 全局变量
global_var = "I am a global variable"
def my_function():
    print(global_var)

my_function() # 输出: I am a global variable
print(global_var) # 输出: I am a global variable

#修改全局变量

global_var = "I am a global variable"
def my_function():
    global global_var
    global_var = "I was modified inside the function"

my_function()
print(global_var) # 输出: I was modified inside the function

