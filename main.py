from config import *; from levels import *; from sprites import *
import pygame, sys, random, time

"""
TODO:

technical:
- write the editor
- write a level manager
- write a sprite manager
- add collision
- add a camera
- delta-time and vector normalization
- raycasting for dark rooms?
- minimap system
- tag system for doors/linked items
- storing level data with json?
- scale down the hitbox by a couple pixels for the player and similar-sized sprites to avoid certain clipping bugs
- shaders, but how?
- inventory system using lists, drag and drop?
- GUI stuff in general
- start menu; edit config file, level editor, debug mode?
- saves using json?
- some form of crash handling?

prospectives:
- animations
- fighting system that isnt boring as hell
- items/runes/trinkets and general RPG elements
- leveling system
- zelda/undertale/enter the gungeon/binding of isaac-like game style
- music?
- bosses?
- minecraft/terraria block-breaking elements?
- secret rooms?
- eventually, i want to make the game extremely interactive and alive, so small changes have big consequences
- fallout-like item placement?
- make some kind of cool story
- make a way to do undertale-like chatboxes

"""

class Game:
    def __init__(self) -> None:
        pygame.init()

        self.run = False
        self.screen = pygame.display.set_mode(RES)

        self.FPSclock = pygame.time.Clock()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
                pygame.quit()
                sys.exit()

    def update(self):
        self.screen.fill(BLACK)
        
        pygame.display.update()


    def start(self):
        self.run = True

        while self.run:
            self.FPSclock.tick(FPS)
            self.events()
            self.update()

def main():
    game = Game()
    game.start()

if __name__ == "__main__":
    main()