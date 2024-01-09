def fizzbuzz(n):
    output = []
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            output.append("FizzBuzz")
        elif i % 3 == 0:
            output.append("Fizz")
        elif i % 5 == 0:
            output.append("Buzz")
        else:
            output.append(str(i))
    return output

# Test cases
print(fizzbuzz(1))  # ['1']
print(fizzbuzz(3))  # ['1', '2', 'Fizz']
print(fizzbuzz(5))  # ['1', '2', 'Fizz', '4', 'Buzz']
print(fizzbuzz(15))  # ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']
print(fizzbuzz(100))  # long list of FizzBuzz output