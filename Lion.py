
class Animals:
    Animals = "WildAnimals"
    def Lion(self):
        print(f"Name of Animal is {self.name}")
        print(f"Animal type is {self.type}")
        print(f"Eats  {self.eat}")
        print(f"Legs Tiger Have {self.Legs}")
        print(f"Tiger Has a long{self.tail}")
        print(f"Lion is known as{self.king}")
Animal2 = Animals()
Animal2.name = "Lion"
Animal2.type = "Carnivorous Animal"
Animal2.eat  = "Meat"
Animal2.tail = "Tail"
Animal2.Legs = 4
Animal2.king = "King Of The Jungle"


Animal2.Lion()

