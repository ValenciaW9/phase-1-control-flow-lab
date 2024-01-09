def happy_new_year():
    countdown = 10
    while countdown > 0:
        print(countdown)
        countdown -= 1
    print("Happy New Year!")

square_integers()
def square_integers(numbers):
    squared_numbers = []
    for num in numbers:
        squared_numbers.append(num ** 2)
    return squared_numbers

    
fizzbuzz()
def fizzbuzz():
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)