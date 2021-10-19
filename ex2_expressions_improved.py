import pytest


def is_even(number: int) -> bool:
    return number % 2 == 0


def test_is_even():
    assert is_even(0)
    assert is_even(2)
    assert is_even(-2)
    assert not is_even(1)
    assert not is_even(-1)


def harmonic_mean(numbers: list[float]) -> float:
    if len(numbers) == 0:
        raise ValueError("numbers must be non-empty")
    total_inverts = sum(1 / n for n in numbers)
    # return (total_inverts / len(numbers)) ** -1
    return len(numbers) / total_inverts


def test_harmonic_mean():
    with pytest.raises(ValueError):
        harmonic_mean([])

    assert harmonic_mean([1, 2]) == 1.3333333333333333
    assert harmonic_mean([1, 2, 7]) == 1.8260869565217392


def should_activate(temperature_c: float, day_of_week: int) -> bool:
    return (temperature_c < 19.0) and day_of_week not in (6, 7)


def test_should_activate():
    assert should_activate(16.0, 1)
    assert not should_activate(19.0, 3)
    assert not should_activate(11.0, 6)
    assert not should_activate(-3.0, 7)
