import functools
import operator

import pytest


def is_even(number: int) -> bool:
    if number % 2 == 0:
        result = True
    else:
        result = False
    return result


def test_is_even():
    assert is_even(0)
    assert is_even(2)
    assert is_even(-2)
    assert not is_even(1)
    assert not is_even(-1)


def harmonic_mean(numbers: list[float]) -> float:
    if len(numbers) == 0:
        raise ValueError("numbers must be non-empty")
    return (
        functools.reduce(
            operator.add,
            [n ** -1 for n in numbers],
        )
        / len(numbers)
    ) ** -1


def test_harmonic_mean():
    with pytest.raises(ValueError):
        harmonic_mean([])

    assert harmonic_mean([1, 2]) == 1.3333333333333333
    assert harmonic_mean([1, 2, 7]) == 1.8260869565217392


def should_activate(temperature_c: float, day_of_week: int) -> bool:
    return (not temperature_c >= 19.0) and (not (day_of_week == 6 or day_of_week == 7))


def test_should_activate():
    assert should_activate(16.0, 1)
    assert not should_activate(19.0, 3)
    assert not should_activate(11.0, 6)
    assert not should_activate(-3.0, 7)
