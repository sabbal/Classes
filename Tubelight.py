class Electronics:

    def __init__(self, Brand, Tube, Holder , wire , Stater, Gives_light):
        self.Brand = Brand
        self.Tube = Tube
        self.Holder = Holder
        self.wire = wire
        self.Stater = Stater
        self.Gives_light = Gives_light
    def itGives_light(self):
        if self.Gives_light():
            return True
        else:
            return False

    def catalog(self):

        return "\n\nBrand:" + self.Brand + "\n\tTube :" + str(self.Tube) + "\n\tHolder:" + str(self.Holder) + "\n\tStater:" + str(self.Stater) + "\n\t Gives light:" + str(self.Gives_light)


Tubelight = Electronics("Bajaj Tube Light", 1,1,1,1,True)
print(Tubelight.catalog())


