class Car:
    def __init__(self, model, color, volume):
        if isinstance(model, str):
            self.model = model
        else:
            raise ValueError('Model must be of type str')
        if isinstance(color, str):
            self.color = color
        else:
            raise ValueError('Color must be of type str')
        if isinstance(volume, float):
            self.volume = volume
        else:
            raise ValueError('Volume must be of type float')

    def drive(self, speed):
        return f'This car drives {speed} km/h'

    def __str__(self):
        return (f'model - {self.model}\n'
                f'color - {self.color}\n'
                f'volume - {self.volume}\n')


print('Простые машины!!!!')
car_1 = Car('Ford', 'blue', 2.5)
car_2 = Car(model='Lexus', color='yellow', volume=5.0)
print(f'{car_1}\n'
      f'-------------\n'
      f'{car_2}')
print(car_1.drive(200))
print(car_2.drive(500))


class HybridCar(Car):
    def __init__(self, model, color, volume, battery, comfort):
        super().__init__(model, color, volume)
        if isinstance(battery, float):
            self.battery = battery
        else:
            raise ValueError('Battery must be of type float')
        if isinstance(comfort, bool):
            self.comfort = comfort
        else:
            raise ValueError('Comfort must be of type bool')

    def call(self):
        return f'This car can call parents'

    def __str__(self):
        return super().__str__() + (f'\nBattery {self.battery}\n'
                                    f'Comfort {self.comfort}\n')


hybrid_1 = HybridCar(model='Toyota Prius', color='black', volume=1.5, battery=72.5, comfort=False)
hybrid_2 = HybridCar(model='Volkswagen ID4', color='white', volume=1.8, battery=100.3, comfort=True)
print(f'----------\n'
      f'{hybrid_1}\n'
      f'{hybrid_2}')
print(hybrid_1.drive(300))
print(hybrid_2.drive(120))
print(hybrid_1.call())
