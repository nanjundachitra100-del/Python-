#list
fruits=["apple","banana","mango","orange","kiwi","grapes"]
print(fruits)
print(len(fruits))
print(fruits[2])
print(fruits[-1])
print(fruits[2:5])
print(fruits[:4])
print(fruits[::2])
print(fruits.pop(3))
print(fruits.append("watermelon"))
print(fruits)
print(fruits.extend(["grapes","mango"]))
print(fruits)
print(fruits.index("apple"))
print(fruits.insert(2,"apple"))
print(fruits.count("apple"))
copy_fruits=fruits.copy()
print(copy_fruits)
new_fruits=copy_fruits+fruits
print(new_fruits)


