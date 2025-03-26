## Functions, arguments, parameters, return values

# def print_name(name: str) ->  None: # None is a special value in Python that represents nothing, this function has no return value
#     print("Ahoj", name)
#     return(1) # This return statement is not necessary, because the function has no return value

# print_name("Robert")

## Function with return value
# def get_number() -> int:
# #     return 237
# x = get_number()
# print(x)

# def get_numbers() -> tuple[int, int]:
#     return 237, 18 # This function returns a tuple, tuple is a sequence of values

# x = get_numbers()
# print(x)

## Function with multiple parameters
# def sum(a: int, b: int) -> int:
#     return a + b

# result_is = sum(a=5, b=7) 
# print(result_is)

# yellow text is my own definition of the function, blue text is the function call

# def work() -> None:
#     x, y = get_numbers()
#     print_name("Robert")
#     print(get_numbers())
    
# work()
# res = get_numbers()
# print(res)

## Default values of parameters

# def greet_user(name: str = "user") -> None:
#     print("Hello, welcome to the system", name)

# greet_user()
# greet_user("Admin")

## Function with variable number of arguments

# x = 1 # x is a global variable, it is defined outside of any function, and should be written outside of any function
# def greet_user(name: str = "user") -> None:
#     x = 5
#     print("Hello, welcome to the system", name)
    

# greet_user()
# greet_user("Admin")

# print(x)

# DRY - Don't Repeat Yourself

# def greet_user(name):
#     print(f"Hello {name}, welcome to the system")
#     print("Glad to see you here!")
#     print("Have a nice day!")
    
# def greet_admin(name):
#     print(f"Hello {name}, welcome to the system")
#     print("Glad to see you here!")
#     print("You have admin rights!")
    
# def greet_guest(name):
#     print(f"Hello {name}, welcome to the system")
#     print("Glad to see you here!")
#     print("You are accessing as s guest!")
    
# # Repeat the same code 3 times, only the role changes - correct but not DRY
#     def greet_user_role(name: str, role: str) -> None:
#         print(f"Hello {name}, welcome to the system")
#         print("Glad to see you here!")
#         if role == "admin":
#             print("You have admin rights!")
#         elif role == "guest":
#             print("You are accessing as a guest!")
#         else:
#             print("Have a nice day!")

#     # Example usage:
#     greet_user_role("Alice", "user")
#     greet_user_role("Bob", "admin")
#     greet_user_role("Charlie", "guest")

#   Recursion
# Recursion is a technique where a function calls itself to solve a smaller version of the same problem.

# def foo(): # This function calls itself
#     print("foo") # This will be printed every time the function is called
#     foo() # This is the recursive call   

# foo() # This will cause a RecursionError

# i want to print the number 1 to 10 using recursion
def print_numbers(n: int) -> None:
    if n == 0:
        return
    print(n)
    print_numbers(n - 1)
    
print_numbers(10)