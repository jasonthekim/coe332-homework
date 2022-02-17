from analyze_water import calculate_turbidity
from analyze_water import minimum_time_threshold
import pytest

def test_calculate_turbidity():
    assert calculate_turbidity([{'a': 1.2, 'b': 2.0}], 'a', 'b') == 2.4 
    assert calculate_turbidity([{'a': 3.1, 'b': 1.0}], 'a', 'b') == 3.1 
    assert calculate_turbidity([{'a': 5.4, 'b': 2.0}], 'a', 'b') == 10.8 
    assert isinstance(calculate_turbidity([{'a': 3.142, 'b': 1.321}], 'a', 'b'), float) == True
    with pytest.raises(KeyError):
        calculate_turbidity([{'a': 1.0, 'b': 2.0}], 'c', 'd') # key not in dict
    with pytest.raises(KeyError):
        calculate_turbidity([{'a': 3.14}], 'a', 'b') # not enough key's in dict


def test_minimum_time_threshold_exceptions():
    assert minimum_time_threshold(0.5, 0.3, 1.0) == 0.0
    assert minimum_time_threshold(1.3, 0.2, 1.0) == 1.18
    assert isinstance(minimum_time_threshold(1.3, 0.2, 1.0), float) == True
    with pytest.raises(TypeError):
        minimum_time_threshold('1.3', 0.03, 1.0) # value not a float 
    with pytest.raises(ZeroDivisionError):
        minimum_time_threshold(1.3, 0.0, 1.0) # decay factor is zero -> ln(1) = 0 -> cannot divide by zero
    
