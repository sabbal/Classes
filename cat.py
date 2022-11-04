class Cat:
    animal = 'Cat'

    def __init__(self, breed, color,):
        self.breed = breed
        self.color = color

Mimi = Cat("Persian", "White")
Pumpkin = Cat("Persian", "Brown")

print('Mimi details:')
print('Mimi is a', Mimi.animal)
print('Breed: ', Mimi.breed)
print('Color: ', Mimi.color)

print('\nPumpkin details:')
print('Nora is a', Pumpkin.animal)
print('Breed: ', Pumpkin.breed)
print('Color: ', Pumpkin.color)

print("\nAccessing class variable using class name")
print(Cat.animal)
