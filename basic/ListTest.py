#!/usr/bin/env python3
names = ["张三", "李四", "王五", "赵六"]

print(names)
# 赋值
names[0] = "张三丰"
# 获取元素
print(names[0])

# 在列表末尾添加元素
names.append("join chi")
print(names)
# 在列表中插入元素
names.insert(0,"迟世超")
print(names)
# 删除元素
del names[0]
print(names)
# 出队
names.pop()
names.pop()
print(names)

names.remove("李四")
print(names)

