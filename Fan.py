class Electronics:

    def __init__(self, Brand, wings, Moter , wire , Boltes , Rotates):
        self.Brand = Brand
        self.wings = wings
        self.Moter = Moter
        self.wire = wire
        self.Boltes = Boltes
        self.Rotates = Rotates
    def it_Rotates(self):
        if self.Rotates():
            return True
        else:
            return False

    def catalog(self):

        return "\n\nBrand:" + self.Brand + "\n\tWings :" + str(self.Wings) + "\n\tMoter:" + str(self.Moter) + "\n\tStater:" + str(self.Stater) + "\n\t Gives light:" + str(self.Gives_light)


Tubelight = Electronics("Bajaj Tube Light", 1,1,1,1,True)
print(Tubelight.catalog())


