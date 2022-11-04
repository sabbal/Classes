class Electronics :

    def Computer (self):
        print(f"{self.Keybord}")
        print(f"{self.Mouse}")
        print(f"{self.Cpu}")
        print(f" {self.spiker}")
        print(f" {self.Joystick}")
        print(f"{self.name}")


MyComputer = Electronics()
MyComputer.name = "Zebronics"
MyComputer.Keybord= "Key board has 80 or more Buttons to type"
MyComputer.Mouse = "mouse has 3 Butoons it is an input Device"
MyComputer.spiker = "Spiker is an out put Device"
MyComputer.Joystick = "Joy stick is an input Device which is use to play games"
MyComputer.Cpu = "Cpu takes an input an gives output it has Ram Rom Mother board Etc.."

MyComputer.Computer()