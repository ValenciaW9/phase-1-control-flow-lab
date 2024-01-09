import pytest
from fizzbuzz_ import fizzbuzz 

@pytest.mark.parametrize(
    "n, expected_output",
    [
        (1, ["1"]),
        (3, ["1", "2", "Fizz"]),
        (5, ["1", "2", "Fizz", "4", "Buzz"]),
        (
            15,
            [
                "1",
                "2",
                "Fizz",
                "4",
                "Buzz",
                "Fizz",
                "7",
                "8",
                "Fizz",
                "Buzz",
                "11",
                "Fizz",
                "13",
                "14",
                "FizzBuzz",
            ],
        ),
    ],
)
def test_fizzbuzz(n, expected_output):
    assert fizzbuzz(n) == expected_output