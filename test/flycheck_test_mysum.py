import pytest
from mysum import mysum


# create a fixture, random_numbers,
# which returns a tuples -- 


def test_mysum_simple():
    assert mysum([10, 20, 30]) == 60
    assert mysum([10.5, 20, 30]) == 60.5


@pytest.mark.negative
def test_mysum_neg():
    assert mysum([-5, -10, -15]) == -30


@pytest.mark.nonint
def test_mysum_float():
    assert mysum([10.5, 20.5, 30.5]) == 61.5


@pytest.mark.nonint
@pytest.mark.negative
def test_mysum_float2():
    assert mysum([10.5, -20.5, 30.5]) == 20.5


def test_mysum_bad_floats():
    assert pytest.approx(mysum([0.1, 0.2])) == 0.3
