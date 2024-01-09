
test("fizzbuzz(1) should return '1'", () => {
  expect(fizzbuzz(1)).toBe("1");
});

test("fizzbuzz(3) should return 'Fizz'", () => {
  expect(fizzbuzz(3)).toBe("Fizz");
});

test("fizzbuzz(5) should return 'Buzz'", () => {
  expect(fizzbuzz(5)).toBe("Buzz");
});

test("fizzbuzz(15) should return 'FizzBuzz'", () => {
  expect(fizzbuzz(15)).toBe("FizzBuzz");
});

test("fizzbuzz(100) should return 'Buzz'", () => {
  expect(fizzbuzz(100)).toBe("Buzz");
});