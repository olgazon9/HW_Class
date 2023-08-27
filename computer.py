class Computer:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.is_on = False
    
    def turn_on(self):
        self.is_on = True
        print(f"The {self.brand} {self.model} computer is now on.")
    
    def turn_off(self):
        self.is_on = False
        print(f"The {self.brand} {self.model} computer is now off.")

# Example usage of the Computer class
laptop = Computer("Dell", "XPS 13")
laptop.turn_on()
laptop.turn_off()
