import random


class Car:
    def __init__(self, engine, wheels, type_car):
        self.engine = engine
        self.wheels = wheels
        self.type = type_car

    @staticmethod
    def __random_car():
        n = random.randint(0, 4)
        return n

    def drive(self, place):
        place = place
        random_event = self.__random_car()
        if random_event > 0:
            print('We are driving to {}, Our engine is: {}'.format(place, self.engine))
        else:
            print(f'You crashed your {self.engine} car ')

    def park(self):
        print(f'Parking the car {self.engine}')
