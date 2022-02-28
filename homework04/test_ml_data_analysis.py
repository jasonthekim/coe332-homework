from ml_data_analysis import compute_average_mass
from ml_data_analysis import check_hemisphere
from ml_data_analysis import count_classes
import pytest


def test_compute_average_mass():
    assert compute_average_mass([{'a': 1.0}, {'a': 2.0}, {'a': 3.0}], 'a') == 2.0
    assert compute_average_mass([{'b': 2.0}, {'b': 3.0}, {'b': 7.0}], 'b') == 4.0
    assert isinstance(compute_average_mass([{'c': 1.0}, {'c': 2.0}, {'c': 3.0}], 'c'), float) == True      
    with pytest.raises(KeyError):
        compute_average_mass([{'a': 1.0}, {'a': 2.0}, {'c': 3.0}], 'a') # dicts don't have same keys
    with pytest.raises(KeyError):
        compute_average_mass([{'a': 1.0}, {'a': 2.0}, {'a': 3.0}], 'b') # key not in dictionaries

def test_check_hemisphere():
    assert check_hemisphere(2.0, 1.0) == 'Northern & Eastern'
    assert check_hemisphere(3.0, -2.0) == 'Northern & Western'
    assert check_hemisphere(-4.0, 5.0) == 'Southern & Eastern'
    assert check_hemisphere(-23.0, -3.0) == 'Southern & Western'
    assert isinstance(check_hemisphere(2.0, 1.0), str) == True


def test_count_classes():
    assert count_classes([{'name': 'jason'}, {'name': 'jason'}, {'name': 'sarah'}, {'name': 'richard'}, {'name': 'bora'}, {'name': 'bora'}, {'name': 'bora'}], 'name') == {'jason': 2, 'sarah': 1, 'richard': 1, 'bora': 3}
    assert isinstance(count_classes([{'name': 'jason'}, {'name': 'jason'}, {'name': 'sarah'}, {'name': 'richard'}, {'name': 'bora'}, {'name': 'bora'}, {'name': 'bora'}], 'name'), dict) == True
    assert isinstance(count_classes([{'name': 'jason'}, {'name': 'jason'}, {'name': 'sarah'}, {'name': 'richard'}, {'name': 'bora'}, {'name': 'bora'}, {'name': 'bora'}], 'name'), list) == False
    with pytest.raises(KeyError):
        count_classes([{'a': 1.0}, {'a': 2.0}, {'c': 3.0}], 'a') # dicts don't have same keys
    with pytest.raises(KeyError):
        count_classes([{'a': 1.0}, {'a': 2.0}, {'a': 3.0}], 'b') # key not in dictionaries



