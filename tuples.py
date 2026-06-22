# Tuple Complete Program

# 1. Creating tuples
student = ("Chitra", 20, "CSE", 8.5)
print("Student tuple:", student)

# 2. Accessing elements (indexing)
print("Name:", student[0])
print("Branch:", student[2])

# 3. Negative indexing
print("Last element:", student[-1])

# 4. Slicing
print("First two elements:", student[:2])
print("From index 1:", student[1:])


# 5. Tuple is immutable (cannot change)
# student[1] = 21  # This gives error


# 6. Tuple with one element
single = (10,)
print("Single element tuple:", single)#if we do not give comma it will be considered as integer not tuple


# 7. Tuple packing
person = "Rahul", 21, "AI"#Tuple packing means putting multiple values into a single tuple without using parentheses.
print("Packed tuple:", person)


# 8. Tuple unpacking
name, age, course = person#taking the values from a tuple and assigning them to separate variables.
print("Name:", name)
print("Age:", age)
print("Course:", course)


# 9. Looping through tuple
print("Looping:")
for item in student:
    print(item)


# 10. Checking element exists
if "CSE" in student:
    print("CSE exists")


# 11. Length of tuple
print("Length:", len(student))


# 12. Count method
numbers = (1, 2, 3, 2, 4, 2, 5)
print("Count of 2:", numbers.count(2))


# 13. Index method
print("Index of 4:", numbers.index(4))


# 14. Nested tuple
college = (
    ("CSE", 100),
    ("ECE", 80),
    ("ME", 60)
)

print("Nested tuple:", college)
print("First department:", college[0])
print("CSE strength:", college[0][1])


# 15. Tuple concatenation
t1 = (1, 2, 3)
t2 = (4, 5, 6)

combined = t1 + t2
print("Concatenated tuple:", combined)


# 16. Tuple repetition
repeat = (1, 2) * 3
print("Repeated tuple:", repeat)


# 17. Convert list to tuple
my_list = [10, 20, 30]
converted = tuple(my_list)

print("List converted to tuple:", converted)


# 18. Tuple comparison
a = (1, 2, 3)
b = (1, 2, 4)

print("Comparison:", a < b)