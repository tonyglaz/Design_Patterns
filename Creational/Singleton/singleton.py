import datetime
import time


class Cache(object):
    # Здесь хранится сам объект кэша, который будет либо создан либо возвращаться при попытке создать новый экземпляр
    _instance = None
    # хранилище кэша
    vault: dict = {}

    # __new__ вызывается перед __init__ поэтому здесь подменяем возвращаемый объект
    def __new__(cls, *args, **kwargs):
        # если объект еще не создан
        if not cls._instance:
            # создадим новый экземпляр класса передав ему класс и параметры инициализации
            cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance

    def set_value(self, key, value):
        self.vault[key] = value

    def get_value(self, key):
        return self.vault[key]

    def check(self, key) -> bool:
        return key in self.vault


class Source:
    def get_smth(self, key):
        """Метод заглушка ждущий 3 секунды и возващающий одну и ту же стркоу"""
        time.sleep(3)
        return 'result'


class App:
    def __init__(self):
        self.cache = Cache()
        self.source = Source()

    def process(self, key):
        start_time = datetime.datetime.now()
        if self.cache.check(key):
            result = self.cache.get_value(key)
        else:
            result = self.source.get_smth(key)
            self.cache.set_value(key, result)
        print(datetime.datetime.now() - start_time)
        return result


app = App()
app2 = App()

print("Are two objects the same:", id(app) == id(app2))
print("Are their caches the same", id(app.cache) == id(app2.cache))
print("Run the execution for the first time and our getting info from source will be ~ 3 sec")

app.process(1)
print("After repeated execution our data will be getting from cache and that's why they will be getting instantly")

app.process(1)
print("data for other source will be ~ 3 sec")

app.process(2)
print("Since we have a cache physically one for two different objects (although each of them has created an instance for itself \
independently) then the second object will no longer access the data source, but will take them immediately from the cache")

app2.process(1)
print("if we run this again data will be getting instantly because objects app and app2 will have same cache")
