import json
from abc import ABC, abstractmethod

CSV = 'Название;Цвет;Вес;\nКот;Редкий окрас(скумбрия на снегу);3\nПес;Черный;15'
JSON = '{ "items": [{"Название": "Медведь", "Цвет": "Бурый", "Вес": "150"},{"Название": "Лиса", "Цвет": "рыжий", "Вес": "7"}]}'


class Adapter(ABC):
    @abstractmethod
    def get_data(self, source) -> dict:
        pass


class CSVReader(Adapter):
    def get_data(self, source):
        lines = self._split_lines(source) # разделяем строку на отдельные списки строк
        headers, data = self._split_header_with_data(lines) # отделяем заголовки от данных
        return self._format_result(headers, data) # преобразуем данные в требуемый формат данных

    def _split_lines(self, source) -> list:
        return source.split('\n')

    def _split_header_with_data(self, lines) -> tuple:
        return lines[0].split(';'), [x.split(';') for x in lines[1:]]

    def _format_result(self, headers, data) -> list:
        items = []
        for line in data:
            items.append(dict(zip(headers, line)))
        return items


class JSONReader(Adapter):
    def get_data(self, source):
        return json.loads(source)['items']


class Printer:
    def __init__(self, adapter: Adapter):
        self.adapter = adapter
        self.data = []

    def _get_data(self, source):
        self.data = self.adapter.get_data(source)

    def print(self, source):
        self._get_data(source)
        for line in self.data:
            print(f"В наличии: {line['Название']}, Окрас: {line['Цвет']}, Масса: {line['Вес']}")


csv_printer = Printer(adapter=CSVReader())
json_printer = Printer(adapter=JSONReader())

csv_printer.print(CSV)
json_printer.print(JSON)
