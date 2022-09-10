from cities import *


original1 = sorted(['Жиздра', 'Жигулёвск', 'Железногорск-Илимский', 'Жуковка', 'Железногорск', 
'Жуковский', 'Жирновск', 'Жердевка', 'Железноводск', 'Жуков'])
original2 = sorted(['Зеленоградск', 'Зеленогорск', 'Заозёрный', 'Зубцов', 'Зерноград', 
'Зеленокумск', 'Звенигород', 'Зуевка', 'Звенигово', 'Змеиногорск', 
'Зима', 'Зарайск', 'Задонск', 'Закаменск', 'Заполярный', 'Знаменск', 
'Зверево', 'Злынка', 'Заинск', 'Заречный', 'Зея', 'Златоуст', 'Заволжье', 
'Заводоуковск', 'Завитинск', 'Зеленодольск', 'Заозёрск', 'Западная Двина', 'Заринск', 'Заволжск'])
original3 = sorted(['Дегтярск', 'Десногорск', 'Дубовка', 'Дзержинский', 'Дудинка', 
'Долгопрудный', 'Давлеканово', 'Донской', 'Дмитров', 'Дагестанские Огни', 
'Данков', 'Донецк', 'Дорогобуж', 'Данилов', 'Дюртюли', 'Далматово', 'Добрянка', 
'Дивногорск', 'Домодедово', 'Димитровград', 'Дзержинск', 'Дмитриев', 'Дно', 'Дубна', 
'ДжанкойОспаривается', 'Дрезна', 'Дербент', 'Дмитровск', 'Дедовск', 'Духовщина', 
'Дальнегорск', 'Демидов', 'Дигора', 'Долинск', 'Дальнереченск', 'Дятьково'])

def test_find_cities():
        
    assert sorted(find_cities("Воронеж", cities=CITIES)) == original1
    assert sorted(find_cities("Агрыз", cities=CITIES)) == original2
    assert sorted(find_cities("Белгород", cities=CITIES)) == original3

def test_get_random_city():
        
    assert get_random_city(original1) in original1
    assert get_random_city(original2) in original2
    assert get_random_city(original3) in original3