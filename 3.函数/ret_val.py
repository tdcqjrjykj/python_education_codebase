# @Author : mcyj
# @Time : 2024/7/12 上午11:30

#基本返回值
def add(x, y):
    return x + y

result = add(5, 3)
print(result)  # 输出: 8

#返回多个值
def get_person_info(name, age):
    return name, age, "Human"

person_info = get_person_info("Alice", 30)
print(person_info)  # 输出: ('Alice', 30, 'Human')

name, age, species = get_person_info("Bob", 25)
print(name, age, species) # 输出: Bob 25 Human

#返回None
def say_hello():
    print("Hello, world!")

result = say_hello()
print(result)  # 输出: None

