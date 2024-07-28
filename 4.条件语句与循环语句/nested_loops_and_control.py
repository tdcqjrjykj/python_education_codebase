# 示例：使用嵌套循环打印乘法表
for i in range(1, 6):  # 外层循环控制行
    for j in range(1, i + 1):  # 内层循环控制列
        print(f"{j}x{i}={i * j}", end="\t")
    print()  # 换行

# 示例：使用break和continue
for i in range(1, 10):
    if i % 3 == 0:
        continue  # 跳过3的倍数
    if i == 5:
        break  # 当i等于5时退出循环
    print(i)