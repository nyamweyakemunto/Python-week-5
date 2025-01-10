# Base class representing a generic character
class Character:
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def introduce(self):
        print(f"I am {self.name}, and my power is {self.power}.")

# Subclass representing a Superhero, inheriting from Character
class Superhero(Character):
    def __init__(self, name, power, alias):
        super().__init__(name, power)  # Initialize the base class
        self.alias = alias

    def introduce(self):
        # Overriding the method to add more specific details
        print(f"I am {self.alias}, also known as {self.name}. My superpower is {self.power}!")

    def save_the_day(self):
        print(f"{self.alias} is saving the day!")

# Create an instance of Superhero
hero = Superhero("Clark Kent", "Super Strength", "Superman")
hero.introduce()  # Calls the overridden method
hero.save_the_day()

# Base class representing a generic vehicle
class Vehicle:
    def move(self):
        pass  # Placeholder method to be overridden

# Subclass representing a Car
class Car(Vehicle):
    def move(self):
        print("Driving ")

# Subclass representing a Plane
class Plane(Vehicle):
    def move(self):
        print("Flying ")

# Subclass representing a Boat
class Boat(Vehicle):
    def move(self):
        print("Sailing ")

# Create instances of each vehicle
car = Car()
plane = Plane()
boat = Boat()

# Call the move method on each vehicle
car.move()  # Output: Driving 
plane.move()  # Output: Flying 
boat.move()  # Output: Sailing 

