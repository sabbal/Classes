class Friend2 :
    def Zian(self):
        print(f"Friend name is {self.Name}")
        print(f"Zian lives in {self.location}")
        print(f"Zian Profession is{self.profession}")
        print(f"Zians age is {self.age}")

Zian_friend = Friend2()
Zian_friend.Name = "zian uddin"
Zian_friend.location = "Hydrabad"
Zian_friend.profession = "Teacher"
Zian_friend.age = 23

Zian_friend.Zian()
