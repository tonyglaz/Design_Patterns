from abc import ABC, abstractmethod


class AbstractCar(ABC):
    @abstractmethod
    def deliver_by_land(self):
        pass


class AbstractShip(ABC):
    @abstractmethod
    def deliver_by_sea(self):
        pass


class AbstractTransportFactory(ABC):

    @abstractmethod
    def create_car(self) -> AbstractCar:
        pass

    @abstractmethod
    def create_ship(self) -> AbstractShip:
        pass


class KiaRio(AbstractCar):
    def deliver_by_land(self):
        print("Везу малое кол-во товаров на легковушке")


class HeavyTruck(AbstractCar):
    def deliver_by_land(self):
        print("Везу огромное кол-во товаров на грузовом автомобиле")


class RubberBoat(AbstractShip):
    def deliver_by_sea(self):
        print("Везу малое кол-во товаров на надувной лодке")


class CargoShip(AbstractShip):
    def deliver_by_sea(self):
        print("Везу огромное кол-во товаров на грузовом корабле")


class UsualTransportFactory(AbstractTransportFactory):
    def create_car(self) -> AbstractCar:
        return KiaRio()

    def create_ship(self) -> AbstractShip:
        return RubberBoat()


class CargoTransportFactory(AbstractTransportFactory):
    def create_car(self) -> AbstractCar:
        return HeavyTruck()

    def create_ship(self) -> AbstractShip:
        return CargoShip()


class WareHouse:
    factory: AbstractTransportFactory

    def __init__(self, factory: AbstractTransportFactory):
        self.factory = factory

    def deliver_with_ship(self):
        ship = self.factory.create_ship()
        ship.deliver_by_sea()

    def deliver_with_car(self):
        car = self.factory.create_car()
        car.deliver_by_land()


warehouse = WareHouse(factory=CargoTransportFactory())
warehouse.deliver_with_ship()
warehouse.deliver_with_car()

warehouse = WareHouse(factory=UsualTransportFactory())
warehouse.deliver_with_car()
warehouse.deliver_with_ship()
