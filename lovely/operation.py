from variables import first_name

#arithematic operator(+,-,/,*,%)
a = 23
c = 14
total = a + c
print("the total is ", total)
subtraction = a - c
print("the subtraction is ", subtraction)
remainder = a % c

print(f'the remainder is  {remainder}')
multiplication = a * c
print("the multiplication is ", multiplication)
division = a / c
print(f'the division is {division}')



# comparison operator(==,<,>,>=,<=,!=)
age1 = 23
age2 = 12
age1==age2
print(f' is age1 equal to age2?{age1==age2}')
print(f'is age1 greater than age2?{age1>age2}')
print(f'is age1 less than age2?{age1<age2}')
print(f'is age1 not equal to age2?{age1!=age2}')
print(f'is age1 greater or equal to age2?{age1>=age2}')
print(f'is age1 less or equal to age2{age1<=age2}')
# logical operator(and,or,not)
math = 67
science = 56
swahili = 78
french = 59
math>science and swahili>french
print( math>science and swahili>french)
print(math<science and swahili<french)
print(math>=science and swahili<=french)
print(math>science or swahili>french)
print(not(math>=science or swahili<=french))


first_number = float(input(" what's your first_number"))
second_number = float(input(" what's your second_number"))
third_number = float(input(" what's your third_number"))
fourth_number = float(input(" what's your fourth_number"))
division1 = first_number / second_number
print(f'the divide1 is {division1}')
division2 = third_number / fourth_number
print(f'the divide2 is {division2}')

print(f'is division1 greater than division2 {division1>division2}')
print(f'is division1 less than division2 {division1<division2}')
print(f'is division1 equal to division2 {division1==division2}')
print(f'is division1 not equal to division2 {division1!=division2}')

userInput = float(input("enter a secret code?"))
print(userInput>50) and (userInput<100)

