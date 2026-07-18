import pygame

from settings import *


class Button:

    def __init__(self, x, y, width, height, text):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.hover = False
        self.font = pygame.font.SysFont(
            FONT,
            22,
            bold=True
        )

    def update(self):
        self.hover = self.rect.collidepoint(
            pygame.mouse.get_pos()
        )

    def draw(self, screen):
        color = ACCENT if self.hover else CELL_COLOR
        pygame.draw.rect(
            screen,
            color,
            self.rect,
            border_radius=10
        )
        pygame.draw.rect(
            screen,
            GRID,
            self.rect,
            2,
            border_radius=10
        )
        text = self.font.render(
            self.text,
            True,
            TEXT
        )
        screen.blit(
            text,
            text.get_rect(center=self.rect.center)
        )

    def clicked(self, event):
        return (
            event.type == pygame.MOUSEBUTTONDOWN
            and event.button == 1
            and self.hover
        )


class TopBar:

    def __init__(self):
        self.font = pygame.font.SysFont(
            FONT,
            24,
            bold=True
        )

    def draw(self, screen, difficulty, timer, mines):
        pygame.draw.rect(
            screen,
            BOARD_BACKGROUND,
            (0, 0, WIDTH, 60)
        )
        title = self.font.render(
            f"Démineur - {difficulty}",
            True,
            TEXT
        )
        screen.blit(title, (20, 18))
        chrono = self.font.render(
            f"Temps : {timer}s",
            True,
            TEXT
        )
        screen.blit(
            chrono,
            (WIDTH // 2 - 70, 18)
        )
        mine = self.font.render(
            f"Mines : {mines}",
            True,
            TEXT
        )
        screen.blit(
            mine,
            (WIDTH - 180, 18)
        )


class Popup:

    def __init__(self):
        self.title_font = pygame.font.SysFont(
            FONT,
            42,
            bold=True
        )
        self.text_font = pygame.font.SysFont(
            FONT,
            22
        )
        self.button = Button(
            WIDTH // 2 - 90,
            HEIGHT // 2 + 50,
            180,
            55,
            "Rejouer"
        )

    def draw(self, screen, title):
        overlay = pygame.Surface(
            (WIDTH, HEIGHT),
            pygame.SRCALPHA
        )
        overlay.fill((0, 0, 0, 150))
        screen.blit(overlay, (0, 0))
        panel = pygame.Rect(
            WIDTH // 2 - 220,
            HEIGHT // 2 - 120,
            440,
            250
        )
        pygame.draw.rect(
            screen,
            BOARD_BACKGROUND,
            panel,
            border_radius=18
        )
        pygame.draw.rect(
            screen,
            ACCENT,
            panel,
            3,
            border_radius=18
        )
        text = self.title_font.render(
            title,
            True,
            TEXT
        )
        screen.blit(
            text,
            text.get_rect(
                center=(WIDTH // 2, HEIGHT // 2 - 40)
            )
        )
        self.button.update()
        self.button.draw(screen)
