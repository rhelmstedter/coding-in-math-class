from paper_pool import count_rebounds
import pytest


@pytest.mark.parametrize(
    "base, height, expected",
    [
        (3, 3, 0),
        (4, 4, 0),
        (5, 5, 0),
        (6, 6, 0),
        (7, 7, 0),
        (8, 8, 0),
        (9, 9, 0),
        (10, 10, 0),
    ],
)
def test_squares(base, height, expected):
    assert count_rebounds(base, height) == expected


@pytest.mark.parametrize(
    "base, height, expected",
    [
        (3, 6, 1),
        (6, 3, 1),
        (2, 8, 3),
        (8, 2, 3),
        (31, 62, 1),
    ],
)
def test_multiples(base, height, expected):
    assert count_rebounds(base, height) == expected


@pytest.mark.parametrize(
    "base, height, expected",
    [
        (3, 5, 6),
        (5, 3, 6),
        (3, 7, 8),
        (7, 3, 8),
        (5, 7, 10),
        (7, 5, 10),
        (31, 61, 90),
    ],
)
def test_non_multiples(base, height, expected):
    assert count_rebounds(base, height) == expected
