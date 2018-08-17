from snakes_cafe.snakes_cafe import order_something, menu_decoder
import pytest

def test_order_function_exists():
    assert order_something

def test_csv_decoder():
    expected = {'animal':{'cat':[8.6, 4], 'blue whale':[300,000, 2]}}
    actual = menu_decoder('Tots,Antipasto,2.50,25\nCaviar,Antipasto,25.99,12')
    assert expected == actual

