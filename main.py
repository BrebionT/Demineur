import pygame
import asyncio
from settings import *

from menu import Menu

from game import Game


async def main():

    pygame.init()

    screen = pygame.display.set_mode(
        (WIDTH, HEIGHT)
    )
    pygame.display.set_caption(
        TITLE
    )
    
    clock = pygame.time.Clock()
    state = "menu"
    menu = Menu(screen)
    game = None
    running = True
    
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if state == "menu":
                menu.events(event)
            elif state == "game":
                game.events(event)
        
        if state == "menu":
            menu.update()
            menu.draw()

            if menu.selected_difficulty:
                game = Game(
                    screen,
                    menu.selected_difficulty
                )
                menu.selected_difficulty = None
                state = "game"

        elif state == "game":
            game.update()
            game.draw()

            if game.finished:
                if game.result == "menu":
                    menu = Menu(screen)
                    state = "menu"

        pygame.display.flip()
        await asyncio.sleep(0)

    pygame.quit()

asyncio.run(main())
