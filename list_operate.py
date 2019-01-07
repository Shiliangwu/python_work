# -*- coding: utf-8 -*-
# @Author: apple
# @Date:   2019-01-03 14:06:11
# @Last Modified by:   apple
# @Last Modified time: 2019-01-03 15:17:10

magicians=['alice','david','carolina']
for magician in magicians:
	print(magician+", that was a great trick!")
	print("I can't wait to see your next trick,"+magician.title()+".\n")
print("Thanks every one . That was a great magic show!")


# 创建数值列表
for value in range(1,5):
	print(value)


# 将数字变换为一个列表list
numbers=list(range(1,6))
print(numbers)


for even_number in range(1,20,2):
	print(even_number)
	

for i in numbers:
	print(i)

digits=[1,2,3,4,5,6,7,8,9,10]
print(min(digits),max(digits),sum(digits))

# 列表解析 .之所以介绍列表解析,是因为等你开始阅读他人编写的代码时,很可能会遇到它们。

squares=[value**2 for value in range(1,11)]
print(squares)
# 

for i in range(1,21):
	print(i)


# 计算 1~1 000 000 的总和:创建一个列表,其中包含数字 1~1 000 000,
# 再使用 min()和 max()核实该列表确实是从 1 开始,
# 到 1 000 000 结束的。
# 另外,对这个列表调 用函数 sum(),看看 Python 将一百万个数字相加需要多长时间。
alargeList=list(range(1,1000001))
print(min(alargeList),max(alargeList),sum(alargeList))


valuelist=[value for value in range(3,30,3)]
print(valuelist)

print([integer**3 for integer in range(1,11)])


# 列表切片
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players)
print(players[-3:])

print(players[0:3])

for player in players[:3]:
	print(player.title())


# 复制列表
my_foods = ['pizza', 'falafel', 'carrot cake'] 
friend_foods = my_foods[:]    # 使用切片复制列表,若不使用：，结果差异。引用而非复制。
print("My favorite foods are:")
print(my_foods)
my_foods.append("my extra food")
print(my_foods)


print("My friend favorite foods are:")
friend_foods.append("friend extra food")
print(friend_foods)


# 元组




