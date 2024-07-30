def abnormal_oper():
    try:

        file = open('example.txt', 'r')

        content = file.read()

        print(content)

    except FileNotFoundError:

        print("文件未找到")

    except IOError:

        print("读取文件时出错")

    finally:

        file.close()

abnormal_oper()