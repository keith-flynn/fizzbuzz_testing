# FizzBuzz

def fizz_buzz(input):
    if input == 0:
        return input
    elif input % 15 == 0:
        return "FizzBuzz"
    elif input % 3 == 0:
        return "Fizz"
    elif input % 5 == 0:
        return "Buzz"
    else:
        return input
