def m(data: list[float]) -> float:
    len = 0
    sum = 0.0
    for d in data:
        len += 1
        sum += d
    if len == 0:
        return 0.0
    return sum / len


# test for m
def test_1():
    assert m([]) == 0.0
    assert m([1.0, 2.0]) == 1.5
    assert m([-1.0, 1.0]) == 0.0


def volsphere_formula(r: float) -> float:
    r3 = r ** 3
    constant = 4 / 3 * 3.141592653589793
    res = constant * r3
    return res


def test_volsphere_formula():
    assert volsphere_formula(1.0) == 4.1887902047863905


def fp(p: int, a: int, plum: float) -> int:
    """
    Apply our price formula for a piece of fruit based on the original price,
    age (days), and plumpness squared
    """
    pDoll = float(p) / 100  # work in dollars

    pDoll = pDoll * (1 - (min(a, 7) / 7)) * sq(plum)

    rp = int(pDoll * 100)
    return rp


def sq(float: float) -> float:
    return float ** 2


def test_final_functino():
    assert fp(100, 0, 1.0) == 100
    assert fp(100, 0, 0.9) == 81
    assert fp(100, 1, 1.0) == 85
    assert fp(30, 7, 1.0) == 0
    assert fp(40, 7, 1.0) == 0
    assert fp(40, 8, 1.0) == 0
    assert fp(200, 2, 0.2) == 5
