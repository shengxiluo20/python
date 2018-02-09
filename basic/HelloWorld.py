#!/usr/bin/env python3

name = "    hello python     "

# name = input("请在屏幕上输入.....")
print("接收到屏幕输入:", name)
print(name.title())
print(name.upper())
print(name.lower())
# rstrip() 删除末尾的空白
# lstrip() 删除头部的空白
# strip() 删除字符串两端的空白
print(name.rstrip())
print(name.lstrip())
print(name.strip())

year = 2018

# 使用函数str()避免类型错误
msg = name.strip()+"\t" + str(year) + "年\n"

print(msg)
