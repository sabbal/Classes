class Hardware :

    def Toolbox(self):
        print(f"Tool box shape is {self.shape}")
        print(f"Tool box size  {self.Size}")
        print(f"Tool box contains {self.Parts}")
        print(f"Tool box is Used {self.Uses}")

Toolbox = Hardware()
Toolbox.shape = "Mostly Square Or Rectangle"
Toolbox.Size= "Smallest 10 inch Larger 20 inches or more"
Toolbox.Parts = "All tools for repairing like Screw driver , hammer etc..."
Toolbox.Uses = "To Make or Repair the Furniture "

Toolbox.Toolbox()