# A procedure is like a recipe: it does work but doesn’t always return a result.
def greet_user(name):
    print("Hello,", name)   


greet_user("Alice")
greet_user("Bob")






def add_numbers(a, b):
    return a + b  
# Use the function
result = add_numbers(3, 5)
print("The sum is:", result)







def show_sum(a, b):        
    print("The sum is:", a + b)

def get_sum(a, b):       
    return a + b


show_sum(2, 4)           
value = get_sum(2, 4)       
print("Returned value:", value)







def square(x):
    return x * x

def sum_of_squares(a, b):
    return square(a) + square(b)

print(sum_of_squares(3, 4))  







def greet(name="friend"):
    print("Hello,", name)

greet()            
greet("Charlie")   








def divide_and_remainder(a, b):
    return a // b, a % b  

q, r = divide_and_remainder(17, 5)
print("Quotient:", q, "Remainder:", r)
  
