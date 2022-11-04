class Friend :
    def Arman(self):
        print(f"Friend name is {self.Name}")
        print(f"Arman lives in {self.location}")
        print(f"Arman  Profession is {self.profession}")
        print(f"Arman age is {self.age}")

friend = Friend()
friend.Name = "Manik Arman"
friend.location = "Nizamabad"
friend.profession = "Gold Merchant"
friend.age = 25

friend.Arman()