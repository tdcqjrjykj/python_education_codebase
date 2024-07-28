# 示例：根据用户年龄给出建议
age = int(input("请输入您的年龄："))
if age < 13:
    print("您还是个孩子。")
elif age < 20:
    print("您正在青春期。")
elif age < 65:
    print("您是成年人。")
else:
    print("您是老年人，保重身体。")