#defining a function no return value amd no argument
def greet():
    print("Hello world")
greet()

# defining a function with argument and no return value
def add(a,b):
    sum_result=a+b
    print(f"the sum of {a} and {b} is {sum_result}")

add(5, 10)

#defining a function with arguments and return type
def add(a,b):
    sum_result=a+b
    return sum_result
result=add(4,8)
print(f"the sum is {result}")

    