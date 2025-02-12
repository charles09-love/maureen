# def my_function():
#     print("Hello World")
#     print("Hello again")
# my_function()
# my_function()
#
#
# def my_function2():
#     salute = "Hello world , I hate you"
#     print(salute)
#
# my_function2( )
#
# def customers(salute):
#     print(salute)
#
# customers("Hello world")
# customers("Hello charles")
#
# def employees(first_name, last_name,age):
#     print(f'Hello {first_name}.{last_name}, you are {age} years old')
# employees("King",  "Clay",40)
# employees("Queen",  "Esther",50)
# employees("princess", "Grace",23)
# def clam (number1,number2):
#     print(f'The sum is {number1 + number2}')
#     print(f'The product is {number1 * number2}')
#     print(f'The quotient is {number1 / number2}')
#     print(f'The remainder is {number1 % number2}')
# clam(30,5)
# def king(num1, num2):
#     total = num1 + num2
#     product = num1 * num2
#     return (f'the product of {num1} and {num2} is:{product} and total:{total}.')
# king(5,5)
# print(king(5,5))
# def age_calculator(current_age):
#     new_age = current_age + 36
#     return new_age
# print(age_calculator(30))
# def bet_bonus(name,correct_score):
#     if correct_score >= 9 and correct_score <= 13:
#         return f'{name} your bonus is 5000'
#     elif correct_score >= 6 and correct_score <= 9:
#         return f'{name} your bonus is 3000'
#     elif correct_score >= 4 and correct_score <= 6:
#         return f'{name} your bonus is 2000'
#     else:
#         return f'{name} your bonus is 0'
#
# print(bet_bonus("Paul",11))
# print(bet_bonus("Maria",6))
# print(bet_bonus("John",4))
# print(bet_bonus("Collins",2))

# def greet(name):
#     if name == "Alice":
#         return "Hello, Alice!"
#     elif name == "Bob":
#         return "Hello, Bob!"
#     else:
#         return "Hello , G!"
#
# print(greet("Alice"))
# print(greet("Bob"))
# print(greet("king"))
def greet(name):
    name=input("Enter your name: ")
    if name=="Alice" or name=="Bob":
        return f'Hello,{name} have a nice time'
    else:
        return f'Hello new guest '
print(greet("alice"))
print(greet("Bob"))

