import cities
import pytest

@pytest.mark.repeat(3)
def test_find_cities():    
        
    random_city = cities.get_random_city(cities.CITIES)
    original = sorted(cities.find_cities(city=random_city, cities=cities.CITIES))        
        
    assert sorted(cities.find_cities(random_city, cities=cities.CITIES)) == original