class Configuration: # abstracte klasse voor puzzels en simpele spellen
    def cost(self):
        pass

    def possible_new_configurations(self):
        pass

    def log(self):
        pass

class SlidingPuzzle(Configuration):
    GRIDSIZE = 3
    EMPTY = 0

    def __init__(self, game):
        # game is typisch een Gridsize-op-Gridsize array met waardes van de puzzel.
        self.Game = game 

    def cost(self):
        # totale kost van het bord
        pass

    def tile_cost(self, goal_row, goal_col, row, col):
        # cost om 1 tegel op zijn plaats te krijgen
        pass
        

    def possible_new_configurations(self):
        #geef een array terug van alle nieuwe mogelijke spelposities vanaf hier (transities)
        pass

    def can_move_to(self, row, col):
        # check of naar deze rij kan worden gemoved
        pass

    def locate_empty(self):
        # geef de locatie terug van het lege vakje
        for row in range(self.GRIDSIZE):
            for col in range(self.GRIDSIZE):
                if self.Game[row][col] == self.EMPTY:
                    return [row, col]
        raise Exception("Something went wrong!")

    def duplicate(self):
        new_game = [[self.Game[row][col] for col in range(self.GRIDSIZE)] for row in range(self.GRIDSIZE)]
        return new_game

    def log(self):
        print("---")
        for row in range(self.GRIDSIZE):
            for col in range(self.GRIDSIZE):
                print(self.Game[row][col], end=", ")
            print()
        print("---")

if __name__ == "__main__":
    game = [ # een voorbeeld van een simpele puzzel
        [1, 2, 3],
        [4, 5, 0],
        [7, 8, 6]
    ]

    puzzle = SlidingPuzzle(game)

    print("Original:")
    puzzle.log()