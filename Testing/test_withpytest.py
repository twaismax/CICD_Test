import pytest
from Calculator.MyCrazyCalculator import myCrazyCalclulator
from freezegun import freeze_time

def test_passes():
    assert True


def test_add():
    calculator = myCrazyCalclulator(crazy_mode=False)
    assert calculator.add(a=1, b=3) == 4

'''def test_fail():
    assert False'''
def test_div_exception():
    calculator = myCrazyCalclulator(crazy_mode=True)
    # so simple!
    with pytest.raises(RuntimeError):
        calculator.div(a=200, b=2)


@pytest.mark.parametrize("crazy_mode, a,b,result", [
    (False, 1, 2, 3),
    (True, 5, 2, 0),
    (True, 2, 2, 4),
    (True, 1, 2, 3),
],    ids=['testA id', 'testB id','testC id','testD id']
)
def test_many_ways_of_plus(crazy_mode, a, b, result):
    calculator = myCrazyCalclulator(crazy_mode=crazy_mode)
    assert calculator.add(a=a, b=b) == result


@freeze_time("2022-06-15")
@pytest.mark.parametrize("crazy_mode, a,b,result", [
    (False, 1, 2, 2),
    (True, 1, 2, 4)]
)
def test_crazy_thursday_calc(crazy_mode, a, b, result):
    calculator = myCrazyCalclulator(crazy_mode=crazy_mode)
    assert calculator.time_mult_calculation(a=a, b=b) == result

@pytest.mark.parametrize("crazy_mode,result", [
    (False, 0),
    (True, 200)]
)
def test_crazy_requests_calculation(crazy_mode,result):
    calculator = myCrazyCalclulator(crazy_mode=crazy_mode)
    assert calculator.requests_calculation() == result
