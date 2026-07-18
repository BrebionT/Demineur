import pygame

from settings import *

class Button:

    def __init__(self, x, y, width, height, text):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.hover = False

    def draw(self, screen):
        color = ACCENT if self.hover else CELL_COLOR
        pygame.draw.rect(screen, color, self.rect, border_radius=12)
        font = pygame.font.SysFont(FONT, TEXT_SIZE)
        text = font.render(self.text, True, TEXT)
        text_rect = text.get_rect(center=self.rect.center)
        screen.blit(text, text_rect)

    def update(self):
        self.hover = self.rect.collidepoint(pygame.mouse.get_pos())

    def clicked(self, event):
        return (
            event.type == pygame.MOUSEBUTTONDOWN
            and event.button == 1
            and self.hover
        )


class Menu:

    def __init__(self, screen):
        self.screen = screen
        self.selected_difficulty = None
        self.title_font = pygame.font.SysFont(FONT, 48, bold=True)
        self.small_font = pygame.font.SysFont(FONT, 20)
        center_x = WIDTH // 2 - 125

        self.buttons = [
            Button(center_x, 260, 250, 60, "Facile"),
            Button(center_x, 340, 250, 60, "Moyen"),
            Button(center_x, 420, 250, 60, "Difficile")
        ]

    def events(self, event):
        for button in self.buttons:
            if button.clicked(event):
                self.selected_difficulty = button.text

    def update(self):
        for button in self.buttons:
            button.update()

    def draw(self):
        self.screen.fill(BACKGROUND)
        title = self.title_font.render("DEMINEUR", True, TEXT)
        title_rect = title.get_rect(center=(WIDTH//2,120))
        self.screen.blit(title, title_rect)
        
        subtitle = self.small_font.render(
            "Choisissez une difficulté",
            True,
            (180,180,180)
        )
        
        sub_rect = subtitle.get_rect(center=(WIDTH//2,170))
        self.screen.blit(subtitle, sub_rect)

        for button in self.buttons:
            button.draw(self.screen)
