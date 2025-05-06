# Base class for Superhero
class Superhero:
    def __init__(self, name, superpower):
        self.name = name  # Name of the superhero
        self.superpower = superpower  # Superpower of the superhero
    
    def display_info(self):
        # Display superhero details
        print(f"Hero: {self.name}")
        print(f"Superpower: {self.superpower}")
    
    def use_power(self):
        # Display message when the hero uses their power
        print(f"{self.name} is using their power: {self.superpower}!")

# Subclass for Villain, inherited from Superhero
class Villain(Superhero):
    def __init__(self, name, superpower, evil_plan):
        super().__init__(name, superpower)  # Use the Superhero constructor
        self.evil_plan = evil_plan  # Add a new attribute for the villain
    
    def display_info(self):
        super().display_info()  # Use the Superhero display method
        print(f"Evil Plan: {self.evil_plan}")

    def use_power(self):
        # Override to show the villain using their power differently
        print(f"{self.name} is using their evil power: {self.superpower}!")

# Create objects for both Superhero and Villain
hero = Superhero("Captain Swift", "Super Speed")
villain = Villain("Dark Phantom", "Invisibility", "Take over the world!")

# Call methods on the objects
hero.display_info()
hero.use_power()


