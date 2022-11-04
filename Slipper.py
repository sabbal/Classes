class Slipper:

    def __init__(self, model, price, color, length, width, height, strips, rubber_strength,):
        self.model = model
        self.price = price
        self.color = color
        self.length = length
        self.width = width
        self.height = height
        self.strips = strips
        self.rubber_strength = rubber_strength


    def isBoucy(self):
        if(self.rubber_strength > 100):
            return "Hai"
        else:
            return "Nai Hai"

    def catalog(self):
        return "\n\nModel:"+self.model + "\n\t" + str(self.price)+" rupay ki hai \n\t"+"Bouncy:"+self.isBoucy()

paragon  = Slipper("hawai chappal",100, "white", 10, 1, 7, 2, 99)
skechers  = Slipper("slides",3000,"white", 10, 1, 7, 2, 101)
Bata  = Slipper("chigusa",300,"white", 10, 1, 7, 2, 80)
gucci  = Slipper("super slide",6000,"white", 10, 1, 7, 2, 200)

print(paragon.catalog())
print(skechers.catalog())
print(Bata.catalog())
print(gucci.catalog())