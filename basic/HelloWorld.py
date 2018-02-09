#!/usr/bin/env python3

name = "    hello python     "

# name = input("请在屏幕上输入.....")
print("接收到屏幕输入:", name)
print(name.title())
print(name.upper())
print(name.lower())
print(name.rstrip())
print(name.lstrip())
print(name.strip())

year = 2018

msg = name.strip()+"\t" + str(year) + "年\n"

print(msg)

#