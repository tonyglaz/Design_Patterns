import datetime
import json
from pprint import pprint


def wrapper(func):
    def log_func(*args, **kwargs):
        start_time = datetime.datetime.now()
        result = func(*args, **kwargs)
        length = len(json.dumps(result))
        delta_time = datetime.datetime.now() - start_time
        result['length'] = length
        result['duration'] = delta_time
        return result

    return log_func

@wrapper
def parse_json(string):
    return json.loads(string)

JSON1 = '{ "items": [{"Название": "Медведь", "Цвет": "Бурый", "Вес": "150"},{"Название": "Лиса", "Цвет": "рыжий", "Вес": "7"}]}'
JSON2 = '{ "items": [{"Название": "Заяц", "Цвет": "Серый", "Вес": "3"},{"Название": "Волк", "Цвет": "белый", "Вес": "70"}]}'

pprint(parse_json(JSON1))
pprint(parse_json(JSON2))
