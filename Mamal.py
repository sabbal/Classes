class Mamal:

    def __init__(self, Name, Face, Hands, Legs, Tail, Eats_meet):
        self.Name = Name
        self.Face = Face
        self.Hands = Hands
        self.Legs = Legs
        self.Tail = Tail
        self.Eats_meet = Eats_meet

    def Carnivorus(self):
        if self.Eats_meet:
            return True
        else:
            return False

    def catalog(self):
        return "\n\nName:" + self.Name + "\n\tFace:" + str(self.Face) + "\n\tHands:" + str(self.Hands) + "\n\tlegs:" + str(self.Legs) + "\n\tTail:" +str(self.Tail) + "\n\tEat Meat:" + str(self.Eats_meet)


Monkey = Mamal("Monkey", 1, 2, 2, 1, False)
Tiger = Mamal("Tiger", 1, 0, 4, 1, True)

print(Monkey.catalog())
print(Tiger.catalog())
