import random
import pygame

from cell import Cell
from settings import *

NUMBER_COLORS = {
    1: (40, 90, 255),
    2: (30, 160, 70),
    3: (220, 60, 60),
    4: (100, 40, 180),
    5: (170, 40, 40),
    6: (40, 170, 170),
    7: (0, 0, 0),
    8: (120, 120, 120)
}

class Board:

    def __init__(self, difficulty):
        data = DIFFICULTIES[difficulty]
        self.rows = data["rows"]
        self.cols = data["cols"]
        self.mine_count = data["mines"]

        self.grid = [
            [Cell(r, c) for c in range(self.cols)]
            for r in range(self.rows)
        ]

        self.cell_size = min(40, 600 // self.rows)
        self.offset_x = (WIDTH - self.cols * self.cell_size) // 2
        self.offset_y = 80
        self.generated = False
        self.game_over = False
        self.win = False

    def generate(self, safe_row, safe_col):
        placed = 0
        while placed < self.mine_count:
            r = random.randint(0, self.rows - 1)
            c = random.randint(0, self.cols - 1)
            if self.grid[r][c].mine:
                continue
            if r == safe_row and c == safe_col:
                continue
            self.grid[r][c].mine = True
            placed += 1
            
        self.compute_numbers()
        self.generated = True

    def compute_numbers(self):
        for row in self.grid:
            for cell in row:
                if cell.mine:
                    continue
                    
                total = 0
                for dr in (-1, 0, 1):
                    for dc in (-1, 0, 1):
                        nr = cell.row + dr
                        nc = cell.col + dc
                        if 0 <= nr < self.rows and 0 <= nc < self.cols:
                            if self.grid[nr][nc].mine:
                                total += 1

                cell.neighbours = total

    def reveal(self, row, col):
        if not self.generated:
            self.generate(row, col)
            
        cell = self.grid[row][col]
        if cell.flagged or cell.revealed:
            return
            
        cell.reveal()
        if cell.mine:
            self.game_over = True
            return

        if cell.neighbours == 0:
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    nr = row + dr
                    nc = col + dc
                    if 0 <= nr < self.rows and 0 <= nc < self.cols:
                        if not self.grid[nr][nc].revealed:
                            self.reveal(nr, nc)

    def draw(self, screen):
        font = pygame.font.SysFont(FONT, 20, bold=True)
        for r in range(self.rows):
            for c in range(self.cols):
                x = self.offset_x + c * self.cell_size
                y = self.offset_y + r * self.cell_size
                rect = pygame.Rect(
                    x,
                    y,
                    self.cell_size,
                    self.cell_size
                )
                cell = self.grid[r][c]
                if cell.revealed:
                    pygame.draw.rect(
                        screen,
                        CELL_REVEALED,
                        rect
                    )
                    if cell.mine:
                        pygame.draw.circle(
                            screen,
                            RED,
                            rect.center,
                            self.cell_size // 4
                        )
                        
                    elif cell.neighbours > 0:
                        text = font.render(
                            str(cell.neighbours),
                            True,
                            NUMBER_COLORS[cell.neighbours]
                        )
                        screen.blit(
                            text,
                            text.get_rect(center=rect.center)
                        )
                else:
                    pygame.draw.rect(
                        screen,
                        CELL_COLOR,
                        rect
                    )

                    if cell.flagged:
                        pygame.draw.circle(
                            screen,
                            GREEN,
                            rect.center,
                            8
                        )

                pygame.draw.rect(
                    screen,
                    GRID,
                    rect,
                    1
                )

    def click(self, pos, button):
        x, y = pos
        if y < self.offset_y:
            return
            
        col = (x - self.offset_x) // self.cell_size
        row = (y - self.offset_y) // self.cell_size
        if not (0 <= row < self.rows):
            return
            
        if not (0 <= col < self.cols):
            return
            
        if button == 1:
            self.reveal(row, col)
            
        elif button == 3:
            self.grid[row][col].toggle_flag()
