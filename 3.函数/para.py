# @Author : mcyj
# @Time : 2024/7/12 上午11:25

#位置参数
def greet(name, greeting):
    print(f"{greeting}, {name}!")

greet("Alice", "Hello") # 正确
# greet("Hello", "Alice") # 错误，因为顺序不匹配

#关键字参数
def greet(name, greeting):
    print(f"{greeting}, {name}!")

greet(name="Alice", greeting="Hello") # 正确，顺序不重要
greet(greeting="Hi", name="Bob") # 也正确，顺序同样不重要

#默认参数
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Alice") # 输出: Hello, Alice!
greet("Bob", "Hi") # 输出: Hi, Bob!

#可变参数
def sum_numbers(*args):
    return sum(args)

print(sum_numbers(1, 2, 3)) # 输出: 6
print(sum_numbers(10, 20)) # 输出: 30

def greet_person(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


greet_person(name="Alice", age=30, job="Engineer")
# 输出:
# name: Alice
# age: 30
# job: Engineer

def func(*args, **kwargs):
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print(f"{key}: {value}")


func(1, 2, 3, name="Alice", age=30)
# 输出:
# 1
# 2
# 3
# name: Alice
# age: 30