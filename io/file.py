# 打开文件
with open("testfile.txt", "rb") as file:
    # print(file.read())
    for line in file.readlines():
        print(line.strip())
