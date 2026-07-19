
#  Definition

# sort() method list ko ascending order (chhote se bade) mein arrange karta hai.

# Syntax
# list_name.sort()

fruits=["Apple","Banana","Mango","Grapes","Orange","pear","melon"]
fruits.sort()
print(fruits)

# 2️⃣ reverse()
# Definition

# reverse() list ke order ko ulta kar deta hai.

# Syntax
# list_name.reverse()

fruits=["Apple","Banana","Mango","Grapes","Orange","pear","melon"]
fruits.reverse()
print(fruits)

# 3️⃣ count()
# Definition

# count() batata hai ke koi item list mein kitni baar aaya hai.

# Syntax
# list_name.count(item)

fruits=["10","4","22","22","22","22","111","33"]
print(fruits.count("22"))


# 4️⃣ index()
# Definition

# index() kisi item ka pehla index batata hai.

# Syntax
# list_name.index(item)


fruits=["10","4","22","22","22","22","111","33"]
print(fruits.index("10"))


# 5️⃣ copy()
# Definition

# copy() list ki duplicate copy banata hai.

# Syntax
# new_list = old_list.copy()



fruits=["Apple","Banana","Mango","Grapes","Orange","pear","melon"]
new_fruits=fruits.copy()
print(new_fruits)

# 6️⃣ len()
# Definition

# len() list ke total elements count karta hai.

# Syntax
# len(list_name)

fruits=["Apple","Banana","Mango","Grapes","Orange","pear","melon"]
print(len(fruits))

