""" 2. Write a function called fizz_buzz that takes a number.
- If the number is divisible by 3, it should return “Fizz”.
- If it is divisible by 5, it should return “Buzz”.
- If it is divisible by both 3 and 5, it should return “FizzBuzz”.
- Otherwise, it should return the same number.
"""

def fizz_buss (a):
    if a == 0 or type(a) != int:
        return 0
    else:
        if a % 3 == 0 and a % 5 == 0:
            return 'fizzBuzz'
        elif a % 3 == 0:
            return 'Fizz'
        elif a % 5 == 0:
            return 'Buzz'
        else:
            return 'Null'


print(fizz_buss(24))
print(fizz_buss(13))
print(fizz_buss(15))
print(fizz_buss(9))
print(fizz_buss(20))
print(fizz_buss(0))
print(fizz_buss('string'))