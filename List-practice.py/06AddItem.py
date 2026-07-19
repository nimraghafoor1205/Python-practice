# Append is used to add item at the  end of the list

fruits=["Apple","Banana","Mango","Grapes","Orange","pear","melon"]
fruits.append("onion")
print(fruits)

# 2. insert()
# Definition

# # insert() method inserts an element at a specific index.
# Syntax
# list_name.insert(index, item)


fruits=["Apple","Banana","Mango","Grapes","Orange","pear","melon"]
fruits.insert(2,"apricot")
print(fruits)

# 3. extend()
# Definition

# extend() method adds all elements of another list to the end of the current list.

# Syntax
# list1.extend(list2)

fruits=["Apple","Banana","Mango","Grapes","Orange","pear","melon"]
more_fruits=["gava","peach"]
fruits.extend(more_fruits)
print(fruits)
