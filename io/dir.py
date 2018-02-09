import os
import time

name = os.environ
print(name)

# 要获取某个环境变量的值，可以调用os.environ.get('key')
get = os.environ.get('PATH')
print(get)

# 查看当前目录的绝对路径:
abspath = os.path.abspath('.')
print(abspath)

path = os.path.join(abspath, "testDir")
# 新建文件夹
# try:
#     os.mkdir(path)
# except:
#     print("文件已创建")
# finally:
#     print("lkdsjflkd")

# 删除文件夹
# os.rmdir(path)

# 拆分路径
split = os.path.split(path)
print(split)



