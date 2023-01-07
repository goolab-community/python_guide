import pytest


def sum(a, b):
    return a + b


def square(l):
    return l**3


def division(a, b):
    if b == 0:
        raise ZeroDivisionError("Can't divide by zero!")
    return a / b


def test_sum():
    a = 0
    b = 1
    assert sum(0, 1) == (a + b)
    assert sum(1, 0.2) == 1.2
    assert sum(4, 6) == 10


@pytest.mark.parametrize('a, expected', [(0, 0), (1, 1), (4, 64), (5, 125)])
def test_square(a, expected):
    assert square(a) == expected


def test_division():
    assert division(1, 1) == 1
    assert division(20, 5) == 4


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        division(4, 0)


def test_fixrture1(my_fixture):
    assert 'hello' == my_fixture


def test_capsys(capsys):
    print("something")
    out, err = capsys.readouterr()
    assert 'something\n' == out
