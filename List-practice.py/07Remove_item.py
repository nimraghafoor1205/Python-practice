
# 1️⃣ remove()
# Definition

# remove() removes a specific item (by value) from the list.

# Syntax
# list_name.remove(item)

fruits=["Apple","Banana","Mango","Grapes","Orange","pear","melon"]
fruits.remove("pear")
print(fruits)

# 2️⃣ pop()
# Definition

# pop() removes an item using its index.

# Syntax
# list_name.pop(index)

fruits=["Apple","Banana","Mango","Grapes","Orange","pear","melon"]
fruits.pop(0)
print(fruits)

# 3️⃣ clear()
# Definition

# clear() removes all elements from the list.

# Syntax
# list_name.clear()

fruits=["Apple","Banana","Mango","Grapes","Orange","pear","melon"]
fruits.clear()
print(fruits)

# 4️⃣ del
# Definition

# del is used to delete an item, a slice, or even the entire list.

fruits=["Apple","Banana","Mango","Grapes","Orange","pear","melon"]
del fruits[0:3]
print(fruits)
