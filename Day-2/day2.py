# ===========================
# Day 2 - Strings & Conditions
# ===========================

# String Indexing
name = "Afan"

print("First character:", name[0])
print("Last character:", name[-1])
print("Middle character:", name[2])
print("Length:", len(name))

# String Slicing
text = "I am learning Python"

print(text[0:4])
print(text[5:13])
print(text[-6:])

# String replace()
text = "Hello World"
print(text.replace("Hello", "Hi"))

text = "Python is easy"
print(text.replace("Python", "Powerful"))

# String find()
text = "Hello World"
print(text.find("World"))

text = "Python is easy"
print(text.find("is"))

# String count()
text = "Hello World"
print(text.count("o"))

text = "fortiigitggkt"
print(text.count("g"))

# String endswith()
text = "easy.py"
print(text.endswith(".py"))

text = "python programming"
print(text.endswith("ing"))

# -------------------------
# Even or Odd Program
# -------------------------

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# -------------------------
# Grade Calculator
# -------------------------

marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
else:
    print("Grade C")