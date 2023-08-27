class Pawn:
    position = ("x", "y")
    color = "white"
    is_queen = False

    def move(self, new_position):
        self.position = new_position
        return self.position

    def eat(self, color, opponent_position):
        print(f"{color.capitalize()} pawn eats opponent at {opponent_position}.")

    def be_eaten(self, color):
        print(f"{color.capitalize()} pawn has been eaten.")

    def become_queen(self, color):
        self.is_queen = True
        print(f"{color.capitalize()} pawn becomes a Queen!")

# Example usage of the Pawn class
white_pawn = Pawn()
white_pawn.move(("a", 2))
white_pawn.eat("black", ("b", 3))
white_pawn.be_eaten("white")
white_pawn.become_queen("white")
