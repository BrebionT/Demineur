class Cell:

    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.mine = False
        self.revealed = False
        self.flagged = False
        self.neighbours = 0

    def reveal(self):
        if self.flagged:
            return
        self.revealed = True

    def toggle_flag(self):
        if self.revealed:
            return
        self.flagged = not self.flagged
