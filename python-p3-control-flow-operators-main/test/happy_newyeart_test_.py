import pytest
from happy_newyear_ import happy_new_year


@pytest.mark.parametrize(
    "expected_output", ["10\n9\n8\n7\n6\n5\n4\n3\n2\n1\nHappy New Year!\n"]
)
def test_happy_new_year(capsys, expected_output):
    happy_new_year()
    captured = capsys.readouterr()
    assert captured.out == expected_output
