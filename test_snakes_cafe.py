import snakes_cafe.snakes_cafe as sc
import pytest

def test_order_function_exists():
    assert sc.order_something


def test_csv_decoder():
    expected = {'animal':{'cat':[8.6, 4], 'blue whale':[300000, 2]}}
    actual = sc.menu_decoder('cat,animal,8.6,4\nblue whale,animal,300000,2')
    assert expected == actual


def test_format_num():
    expected = '$13.87'
    actual = sc.format_nums(13.87454321)
    assert expected == actual
