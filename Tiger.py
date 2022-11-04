
class Animals:
    Animals = "WildAnimals"
    def Tiger(self):
        print(f"Name of Animal is {self.name}")
        print(f"Animal type is {self.type}")
        print(f"Eats  {self.eat}")
        print(f"Legs Tiger Have {self.Legs}")
        print(f"Tiger Has a long{self.tail}")

Animal1 = Animals()
Animal1.name = "Tiger"
Animal1.type = "Carnivorous Animal"
Animal1.eat  = "Meat"
Animal1.tail = "Tail"
Animal1.Legs = 4
Animal1.Tiger()