import pygame
import time

from settings import *
from board import Board
from ui import TopBar, Popup

class Game:


    def __init__(self, screen, difficulty):
        self.screen = screen
        self.difficulty = difficulty
        self.board = Board(difficulty)
        self.start_time = None
        self.finished = False
        self.result = None
        self.font = pygame.font.SysFont(
            FONT,
            TEXT_SIZE,
            bold=True
        )
        self.topbar = TopBar()
        self.popup = Popup()


    def events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if not self.finished:
                self.board.click(
                    event.pos,
                    event.button
                )
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.finished = True
                self.result = "menu"
                
        if self.finished:
            if self.popup.button.clicked(event):
                self.__init__(
                    self.screen,
                    self.difficulty
                )


    def update(self):
        if self.start_time is None:
            self.start_time = time.time()

        if self.board.game_over:
            self.finished = True
            self.result = "defeat"

        if self.check_win():
            self.finished = True
            self.result = "win"

    def check_win(self):
        total = self.board.rows * self.board.cols
        revealed = 0

        for row in self.board.grid:
            for cell in row:
                if cell.revealed:
                    revealed += 1

        return (
            revealed ==
            total - self.board.mine_count
        )

    def draw(self):
        self.screen.fill(BACKGROUND)
        self.board.draw(
            self.screen
        )

        if self.start_time:
            elapsed = int(
                time.time()
                -
                self.start_time
            )
        else:
            elapsed = 0

        timer = self.font.render(
            f"Temps : {elapsed}s",
            True,
            TEXT
        )

        self.screen.blit(
            timer,
            (30,20)
        )
        
        flags = 0

        for row in self.board.grid:
            for cell in row:
                if cell.flagged:
                    flags += 1

        self.topbar.draw(
            self.screen,
            self.difficulty,
            elapsed,
            self.board.mine_count - flags
        )



        if self.finished:

            if self.result == "win":
                self.popup.draw(
                    self.screen,
                    "VICTOIRE !"
                )

            elif self.result == "defeat":
                self.popup.draw(
                    self.screen,
                    "GAME OVER"
                )
