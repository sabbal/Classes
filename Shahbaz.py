class Friend :
    def Shahbaz(self):
        print(f"Friend name is {self.Name}")
        print(f"Shahbaz lives in {self.location}")
        print(f"Shahbaz  Profession is {self.profession}")
        print(f"Shahbaz age is {self.age}")

friend = Friend()
friend.Name = "Shahbaz khan"
friend.location = "Nizamabad"
friend.profession = "Photorapher"
friend.age = 24

friend.Shahbaz()