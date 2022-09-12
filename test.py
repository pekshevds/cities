import cities


def test_find_cities():
    
    for counter in range(3):
        
        random_city = cities.get_random_city(cities.CITIES)
        original = sorted(cities.find_cities(city=random_city, cities=cities.CITIES))        
        
        assert sorted(cities.find_cities(random_city, cities=cities.CITIES)) == original


def test_get_random_city():
        
    for counter in range(3):
        
        random_city = cities.get_random_city(cities.CITIES)
        original = sorted(cities.find_cities(city=random_city, cities=cities.CITIES))
        
        assert cities.get_random_city(original) in original
    