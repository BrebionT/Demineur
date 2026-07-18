import pygame

pygame.init()

WIDTH = 1280
HEIGHT = 720

FPS = 60

TITLE = "Démineur"

BACKGROUND = (12, 18, 33)

BOARD_BACKGROUND = (21, 30, 52)

CELL_COLOR = (41, 56, 88)

CELL_HOVER = (56, 73, 110)

CELL_REVEALED = (74, 92, 125)

GRID = (31, 44, 70)

TEXT = (245, 245, 245)

ACCENT = (78, 139, 255)

RED = (220, 70, 70)

GREEN = (75, 190, 95)

FONT = "arial"

TITLE_SIZE = 42
TEXT_SIZE = 24
SMALL_SIZE = 18

DIFFICULTIES = {

    "Facile": {

        "rows": 9,
        "cols": 9,
        "mines": 10

    },

    "Moyen": {

        "rows": 16,
        "cols": 16,
        "mines": 40

    },

    "Difficile": {

        "rows": 16,
        "cols": 30,
        "mines": 99

    }

}
