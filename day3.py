# ==========================
# Day 3 - Lists and Tuples
# ==========================

# 1. Creating a List
fruits = ["Apple", "Banana", "Mango", "Orange"]
print("List:", fruits)

# 2. Accessing List Elements
print("First Fruit:", fruits[0])
print("Last Fruit:", fruits[-1])

# 3. List Slicing
print("First 2 Fruits:", fruits[0:2])
print("Last 2 Fruits:", fruits[2:4])

# 4. Changing List Item
fruits[1] = "Pineapple"
print("Updated List:", fruits)

# 5. List Methods
fruits.append("Grapes")
print("After Append:", fruits)

fruits.insert(2, "Kiwi")
print("After Insert:", fruits)

fruits.remove("Orange")
print("After Remove:", fruits)

fruits.pop()
print("After Pop:", fruits)

numbers = [5, 3, 8, 1, 9]
numbers.sort()
print("Sorted Numbers:", numbers)

numbers.reverse()
print("Reverse Order:", numbers)

# ==========================
# Tuples
# ==========================

colors = ("Red", "Green", "Blue", "Yellow")
print("Tuple:", colors)

print("First Color:", colors[0])
print("Last Color:", colors[-1])

# Tuple Slicing
print("Tuple Slice:", colors[1:3])

# Tuple Methods
numbers_tuple = (10, 20, 30, 20, 40, 20)

print("Count of 20:", numbers_tuple.count(20))
print("Index of 30:", numbers_tuple.index(30))

# ==========================
# Practice Question 1
# ==========================

movies = []

movies.append(input("Enter Movie 1: "))
movies.append(input("Enter Movie 2: "))
movies.append(input("Enter Movie 3: "))

print("Favorite Movies:", movies)

# ==========================
# Practice Question 2
# ==========================

marks = []

marks.append(int(input("Enter Math Marks: ")))
marks.append(int(input("Enter Science Marks: ")))
marks.append(int(input("Enter English Marks: ")))

marks.sort()

print("Sorted Marks:", marks)

# ==========================
# Practice Question 3
# ==========================

numbers = (1, 2, 3, 2, 4, 2, 5)

print("Count of 2:", numbers.count(2))