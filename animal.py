class Animal:
    def __init__(self, species, sound):
        self.species = species
        self.sound = sound
    
    def make_sound(self):
        print(f"The {self.species} makes a {self.sound} sound.")

    def move(self, movement):
        print(f"The {self.species} moves by {movement}.")

# Example usage of the Animal class
dog = Animal("Dog", "bark")
dog.make_sound()
dog.move("running")
