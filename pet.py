class Pet:
    def __init__(self, name, hunger, energy, happiness):
        self.name = name
        self.hunger = hunger
        self.energy = energy
        self.happiness = happiness
    def eat(self):
        self.hunger = min(10, self.hunger -3)
        self.happiness = max(0, self.happiness + 1)
        return f"{self.name} has really enjoyed the meal 🍗🍗."
    def sleep(self):
        self.energy = min(0, self.energy + 5)
        self.energy = max(10, self.energy + 0)
        return f"{self.name} has fully rested and energy levels are upto 🔋%"
    def play(self):
        self.energy = max(10, self.energy + 2)
        self.happiness = max(10, self.happiness + 2)
        self.hunger = min(0, self.hunger - 1)
        return f"{self.name} energy levels are 🪫% and needs to rest😮‍💨."
    