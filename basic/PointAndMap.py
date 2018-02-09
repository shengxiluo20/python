#!/usr/bin/env python3

point = (100, 30, 323, 23)
for p in point:
    print(p)

point = (1, 21, 32, 23)
for p in point:
    print(p)
    if p == 1:
        print("=====")
    elif p == 21:
        print("+++++")
print("end")

map = {"key": "value===", "key1": "value1", "key2": "value2"}

key_ = map["key"]
print(key_)
map["key"] = "value==后"
print(map["key"])

del map["key"]
print(map)

for key, value in map.items():
    print(key)
    print(value)
