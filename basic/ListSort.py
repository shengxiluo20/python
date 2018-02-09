#!/usr/bin/env python3

names = ["张三", "李四", "王五"]
# 排序
names.sort(reverse=True)
print(names)

sorted(names, reverse=True)
print(names)
# 翻转列表
names.reverse()
print(names)

# 判断长度
print("列表长度" + str(len(names)))

for name in names:
    print(name)
    print("一行结束")
print("结束,注意缩进")

for value in range(1, 5):
    print(value)

numbers = list(range(1, 6))
print(numbers)

print(min(numbers))
print(max(numbers))
print(sum(numbers))


# 前一个数从0开始，后一个数从1开始数
# nicks =['zhangsan','lisi','wangwu','zhaoliu']
# print(nicks[0:3])  前一个数从0开始，后一个数从1开始数
# print(nicks[2:3])  从2开始，截止到第4个元素
# print(nicks[2:])   从2开始，没有指定截止数据，直接数到末尾
# print(nicks[:2])   没有指定开始，默认从0开始
# print(nicks[:])    没有指定开始，也没有指定结束的，直接复制整个列表
# print(nicks[-2:])  从倒数第2个开始
#
# 得到：
# ['zhangsan', 'lisi', 'wangwu']
# ['wangwu']
# ['wangwu', 'zhaoliu']
# ['zhangsan', 'lisi']
# ['zhangsan', 'lisi', 'wangwu', 'zhaoliu']
# ['wangwu', 'zhaoliu']
