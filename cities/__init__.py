import pathlib
import random
from .parser import init_parser


def _read_cities_from_file() -> list[str]:
    """
    read file with cities
    """
    file_name = pathlib.Path(pathlib.Path.cwd(), 'cities', 'cities.txt')
    with open(file_name, mode='r', encoding='utf-8') as file:
        cities = set(
            line.strip() for line in file.readlines() if line.strip() != ""
            )
    return list(cities)


def find_cities(city: str, cities: list) -> list[str]:
    """
    finds cities by last city character
    """
    return [_ for _ in cities if _.lower().startswith(city.lower()[-1])]


def get_random_city(cities: list) -> str:
    """
    get random city from city list
    """

    return random.choice(cities)


CITIES = _read_cities_from_file()
