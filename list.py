# -*- coding: utf-8 -*-
# @Author: apple
# @Date:   2019-01-03 12:33:05
# @Last Modified by:   apple
# @Last Modified time: 2019-01-03 14:05:53


# 在Python中,用方括号([])来表示列表,并用逗号来分隔其中的元素。

bicycle=['trek','cannondale','redline','specialized']
print(bicycle)

print(bicycle[0])   # 当只请求元素时，只返回元素，不包括引号及方括号
# index start from 0, which is the same as C language.

print(bicycle[1:3])
print(bicycle[-1])
print(bicycle[-2:])

print(bicycle[0].title())

message="My first bicycle was a "+bicycle[0].title()
print(message)


# modified elements of a list

motorcycle=["honda","yamaha","suzuki"]
print(motorcycle)

motorcycle.append("ducati")
print(motorcycle)


motorcycle=[]
motorcycle.append('honda')
motorcycle.append('yamaha')
motorcycle.append("suzuki")
print(motorcycle)

motorcycle=["honda","yamaha","suzuki"]
motorcycle.insert(0,'ducati')
print(motorcycle)

del motorcycle[0]   # 可以使用del 语句删除列表中的某个元素
print(motorcycle)

del motorcycle[2]
print(motorcycle)

motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()
print("last motorcycle  " + last_owned.title() + ".")


print(motorcycle)

# 根据值删除元素

motorcycle.remove("honda")
#  remove 方法remove()只删除第一个指定的值。
print(motorcycle)

cars=['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

cars.sort(reverse=True)
print(cars)

# sort 排序效果是永久性的
# sorted 可以临时排序。
print("orginal ")
print(cars)
print("after sorted")
print(sorted(cars))
print("now orginal")
print(cars)

# reverse 翻转列表元素的排列次序
cars=['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(cars)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
print(motorcycles[-1])   # -1 指列表中的最后一个元素，仅当列表为空时，error

motorcycles=[]
# print(motorcycles[-1])






