# write a python program to add two numbers 
num1 = 1.5
num2 = 6.3
sum = num1 + num2
print(f'Sum: {sum}')


# write a python function to add two user provided numbers and return the sum
def add_two_numbers(num1, num2):
    sum = num1 + num2
    return sum


# write a program to find and print the largest among three numbers

num1 = 10
num2 = 12
num3 = 14
if (num1 >= num2) and (num1 >= num3):
   largest = num1
elif (num2 >= num1) and (num2 >= num3):
   largest = num2
else:
   largest = num3
print(f'largest:{largest}')

