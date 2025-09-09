# task 1
number1 = float((input("write the first number:")))
number2 = float((input("write the second number:")))
print("select an operator (+,-,*,/)")
operator = (input("enter an operator"))
if operator == '*':
    print(number1 * number2)
elif operator == '/':
    if number2 == 0:
        print("number cannot be divided by zero")
    else:
        print(number1/number2)
elif operator == '+':
    print(number1 + number2)

    
else:
   print( number1 - number2)

#task 2
numbers= int(input("enter student's numbers:"))
if numbers >= 85:
    print(' Grade is A')
elif numbers >=70:
    print('Grade is B')
elif numbers >= 50:
    print('Grade is C')
else :
    print('Grade is F')

# task 3
year = int(input('Please type in a year: '))

if year % 400 == 0:
    print('year is a leap year.')
elif year % 100 == 0:
    print('year you entered is not a leap year.')
elif year % 4 == 0:
    print(' year you entered is a leap year.')
else:
    print('year you entered  is not a leap year.')


