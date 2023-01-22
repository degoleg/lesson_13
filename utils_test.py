import pytest, conftest

from utils import get_period, sum_func

grade_exceptions = [(-1, ValueError), (25, ValueError),
                    ("6", TypeError), (6.0, TypeError)]


@pytest.mark.parametrize("grade_int, exception", grade_exceptions)
def test_grade_exceptions(grade_int, exception):
    with pytest.raises(exception):
        get_period(grade_int)

grade_parameters = [(0, "ночь"),(7, "утро"), (12, "день"), (18, "вечер")]

@pytest.mark.parametrize("grade_int, grade_str", grade_parameters)
def test_grade_parameters(grade_int, grade_str):
    assert get_period(grade_int) == grade_str


def test_sum_func( two_numbers_sum):  # обратите внимание на имя

    sum_result = sum_func(two_numbers_sum[0], two_numbers_sum[1])
    assert sum_result == two_numbers_sum[2]

