import pygame, sys; from config import *

"""
TODO:

$ find some way to switch between colours to draw, maybe using the keyboard?
$ write the drawing function
$ make erasing possible
-~$ make it able to save the current self.grid list
- write the load_map function
- include ways to link doors? or perhaps, make the entire map function without loading different rooms constantly
- be able to playtest the map?
- add more textures and find a way to encode them

$ add wasd support to traverse bigger maps?
- zoom in and out functions?
- zone editors?
- add GUI?
- initialize a massive matrix with assigned tiles, then moving them and updating them wont be a problem?

- define a null tile that is just black, so that i can do some things like carving and whatnot

"""
def load_map(tilemap):
    """
    TODO:
    Should be able to load a previous tilemap
    from the folders, returning a 2d list for
    the editor.
    """
    pass

class Tile:
    def __init__(self, editor, x: int, y: int, col: int) -> None:
        self.editor = editor
        self.ts = TS - 2
        self.x, self.y = x, y
        self.ox, self.oy = x, y

        self.rect = pygame.Rect(
                            self.x * TS + 1, 
                            self.y * TS + 1, 
                            self.ts, 
                            self.ts)  # the -2 creates a natural looking grid pattern. the +1 centers it

        self.colour = self.editor.colours[col]

    def scale_rect(self, ts_scaled):
        self.ts = ts_scaled
        self.rect.width = self.ts - 2
        self.rect.height = self.ts - 2

        self.rect.x = self.x * self.ts + 1
        self.rect.y = self.y * self.ts + 1

    def reset_pos(self):
        self.rect.x = self.ox * TS + 1
        self.rect.y = self.oy * TS + 1

    def set_colour(self, new_colour):
        self.colour = self.editor.colours[new_colour]

    def draw(self):
        pygame.draw.rect(self.editor.screen, self.colour, self.rect)

class Editor:
    def __init__(self, different_map=None) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode(RES)
        self.run = False

        self.current_res = RES  # for scaling stuff

        if different_map is None:
            self.grid = []
            for row in range(MAPSIZE_Y):
                self.grid.append(
                    [0] * MAPSIZE_X
                )
        else:
            self.grid = load_map(different_map)

        self.tiles = []

        self.colours = {
            0: GRAY,
            1: WHITE,
            2: BLACK,
            3: RED,
            4: GREEN,
            5: BLUE
        }

        self.selected_colour = 1

        self.FPSclock = pygame.time.Clock()
        
        # for scaling/zoom
        self.TS_scaled = TS

    def decode_graphics_code(self, code):
        # format is as follows: TL#000$S - 'topleft, id 000, solid block'
        # could possibly encode this in binary? or is that too hardore?
        # eg, 00100001 would be read looking at the first 3 bits, then the next 4 as id, then the last for the solid/nonsolid?
        pass

    def movement(self, keys):
        #TODO: 
        # implement bounds
        # normalize the vectors

        # each direction is flipped to make it look like a camera is moving rather than the sprites
        if keys[pygame.K_w]:
            for tile in self.tiles:
                tile.rect.y += 2

        if keys[pygame.K_a]:
            for tile in self.tiles:
                tile.rect.x += 2

        if keys[pygame.K_s]:
            for tile in self.tiles:
                tile.rect.y += -2

        if keys[pygame.K_d]:
            for tile in self.tiles:
                tile.rect.x += -2

        if keys[pygame.K_LSHIFT] and keys[pygame.K_LCTRL] and keys[pygame.K_r]:
            for tile in self.tiles:
                tile.reset_pos()

    def keyboard_listener(self):
        if pygame.KEYDOWN:
            keys = pygame.key.get_pressed()

            self.change_selected_colour(keys)
            self.movement(keys)

    def paint_tiles(self):
        if pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            for tile in self.tiles:
                if tile.rect.collidepoint(pos):

                    if pygame.mouse.get_pressed()[0]:  # left click
                        tile.set_colour(self.selected_colour)
                        self.grid[tile.y][tile.x] = self.selected_colour

                    elif pygame.mouse.get_pressed()[2]:  # right click
                        tile.set_colour(0)  # default colour
                        self.grid[tile.y][tile.x] = 0

                    break

    def change_selected_colour(self, keys):
        if keys[pygame.K_LSHIFT]:
            if keys[pygame.K_0]:
                self.selected_colour = 0

            elif keys[pygame.K_1]:
                self.selected_colour = 1

            elif keys[pygame.K_2]:
                self.selected_colour = 2

            elif keys[pygame.K_3]:
                self.selected_colour = 3

            elif keys[pygame.K_4]:
                self.selected_colour = 4

            elif keys[pygame.K_5]:
                self.selected_colour = 5

    def generate_tiles(self):
        for i, row in enumerate(self.grid):
            for j, col in enumerate(row):
                self.tiles.append(
                    Tile(self, j, i, col)
                )

    def offset_by_mouse(self):
        """
        It is what it is. its still broken,
        but it serves its purpose (kind of)
        """
        mx, my = pygame.mouse.get_pos()

        for tile in self.tiles:
            tile.rect.x += (mx - WWIDTH // 2) / 2
            tile.rect.y += (my - WHEIGHT // 2) / 2

    def scale_tiles(self, y):
        #TODO: this is broken
        
        y = y / abs(y)  # normalize to +-1
        self.TS_scaled += y

        for tile in self.tiles:
            tile.scale_rect(self.TS_scaled)

        self.offset_by_mouse()


    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEWHEEL:
                self.scale_tiles(event.y)
                
            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                self.print_tilemap(keys)

    def draw_all(self):
        for tile in self.tiles:
            tile.draw()

        # "crosshair" (its a circle lol)
        pygame.draw.circle(self.screen, GREEN, (WWIDTH//2, WHEIGHT//2), 3)

    def update(self):
        self.screen.fill(BLACK)

        self.draw_all()

        pygame.display.update()

    def print_tilemap(self, keys):
        if keys[pygame.K_LSHIFT] and keys[pygame.K_s]:
            print('\n')
            for i in self.grid:
                print(i)
            print('\n')
            

    def start(self):

        self.generate_tiles()

        self.run = True
        while self.run:
            self.FPSclock.tick(FPS)
            self.events()

            self.keyboard_listener()
            self.paint_tiles()

            self.update()

if __name__ == '__main__':
    editor = Editor()
    editor.start()