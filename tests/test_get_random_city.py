import cities
import pytest

@pytest.mark.repeat(3)
def test_get_random_city():    
        
    random_city = cities.get_random_city(cities.CITIES)
    original = sorted(cities.find_cities(city=random_city, cities=cities.CITIES))
        
    assert cities.get_random_city(original) in original    