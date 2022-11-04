class Friend2 :
    def Arbaz(self):
        print(f"Friend name is {self.Name}")
        print(f"Arbaz lives in {self.location}")
        print(f"Arbaz Profession is {self.profession}")
        print(f"Arbaz age is {self.age}")

friend = Friend2()
friend.Name = "Arbaz khan"
friend.location = "Nizamabad"
friend.profession = "Body Bilder"
friend.age = 23

friend.Arbaz()