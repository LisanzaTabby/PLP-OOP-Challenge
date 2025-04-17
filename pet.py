class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []
    def eat(self):
        self.hunger = max(0, self.hunger -3)
        self.happiness = min(10, self.happiness + 1)
        return f"{self.name} has really enjoyed the meal 🍗🍗."
    def sleep(self):
        self.energy = min(10, self.energy + 5)
        return f"{self.name} has fully rested and energy levels are upto 🔋%"
    def play(self):
        if self.energy >= 2:
            self.energy = min(10, self.energy - 2)
            self.happiness = min(10, self.happiness + 2)
            self.hunger = max(0, self.hunger + 1)
            return f"{self.name} energy levels are 🪫% and needs to rest😮‍💨."
        else:
            return f"{self.name} is too tired to play. Let them rest!"
    def get_status(self):
        print(f"🐕 {self.name}'s Status: ")
        print(f"🍖 Hunger Levels: {self.hunger}/10")
        print(f"⚡ Energy Levels: {self.energy}/10")
        print(f"😀 Happiness Levels: {self.happiness}/10")
        print(f"🥳 {self.name}'s Learnt Tricks: {', '.join(self.tricks)}")
    # Bonus Challenge Methods
    def train(self, trick):
        if trick not in self.tricks:
            self.tricks.append(trick)
            self.happiness = min (10, self.happiness + 1) # increases happiness by 1
            print(f"{self.name} learn a new trick: {trick}! 🥳")
        else:
            print(f"{self.name} already knows how to {trick}!")
    def show_tricks(self):
        if self.tricks:
            print(f"{self.name} knows these tricks: {', '.join(self.tricks)}")
        else:
            print(f"{self.name} hasn't learned any tricks yet 😔.")