file = open('example.txt', 'r')

content = file.read()

print(content)

file.close()

file = open('example.txt', 'r')
for line in file:
    print(line.strip())   #strip() 用于去除行末的换行符

file.close()