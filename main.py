# importing the Pet class from the pet.py file
from pet import Pet

my_pet = Pet("buddy")
my_pet.get_status()                      # Show initial state
print("Action Taken:\n", my_pet.sleep())  # Show result of play action
my_pet.get_status()  
print("Action Taken:\n", my_pet.play())  # Show result of play action
my_pet.get_status()  
print("Action Taken:\n", my_pet.eat())  # Show result of play action
my_pet.get_status()  
my_pet.train("roll-over")
my_pet.train("sit")
my_pet.train("jump")
my_pet.train("jump")
my_pet.show_tricks()
my_pet.get_status()




