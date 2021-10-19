import math


def mean(numbers: list[float]) -> float:
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)


def test_mean() -> None:
    assert mean([]) == 0.0
    assert mean([1.0, 2.0]) == 1.5
    assert mean([-1.0, 1.0]) == 0.0


SPHERE_CONSTANT = 4 / 3 * math.pi


def sphere_volume(radius: float) -> float:
    return SPHERE_CONSTANT * radius ** 3


def test_sphere_volume():
    assert sphere_volume(1.0) == 4.1887902047863905


DAYS_IN_WEEK = 7


def fruit_price(
    original_price_cents: int,
    age_days: int,
    plumpness: float,
) -> int:
    if age_days >= DAYS_IN_WEEK:
        return 0
    age_factor = 1 - age_days / DAYS_IN_WEEK

    return int(original_price_cents * age_factor * plumpness ** 2)


def test_fruit_price():
    assert fruit_price(100, 0, 1.0) == 100
    assert fruit_price(100, 0, 0.9) == 81
    assert fruit_price(100, 1, 1.0) == 85
    assert fruit_price(30, 7, 1.0) == 0
    assert fruit_price(40, 7, 1.0) == 0
    assert fruit_price(40, 8, 1.0) == 0
    assert fruit_price(200, 2, 0.2) == 5
