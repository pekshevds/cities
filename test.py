from cities import *


def test_find_cities():
    
    for counter in range(3):
        
        random_city = get_random_city(CITIES)
        original = sorted(find_cities(city=random_city, cities=CITIES))        
        
        assert sorted(find_cities(random_city, cities=CITIES)) == original


def test_get_random_city():
        
    for counter in range(3):
        
        random_city = get_random_city(CITIES)
        original = sorted(find_cities(city=random_city, cities=CITIES))
        
        assert get_random_city(original) in original
    