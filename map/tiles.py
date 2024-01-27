import pygame
from .tile import Tile


class Tile01(Tile):
    def __init__(self, pos_x, pos_y):
        Tile.__init__(self, pos_x, pos_y)
        self.tile_sprite = pygame.Surface.subsurface(self.sprites, (143, 16, 17, 16))
        self.set_tile_code(1)

    def show(self):
        return pygame.transform.scale(self.tile_sprite, (23, 20))

    def get_position(self):
        return self.pos_x - 2, self.pos_y - 2


class Tile02(Tile):
    def __init__(self, pos_x, pos_y):
        Tile.__init__(self, pos_x, pos_y)
        self.tile_sprite = pygame.Surface.subsurface(self.sprites, (288, 256, 16, 16))
        self.set_tile_code(2)

    def show(self):
        return pygame.transform.scale(self.tile_sprite, (22, 22))


class Tile03(Tile):
    def __init__(self, pos_x, pos_y):
        Tile.__init__(self, pos_x, pos_y)
        self.tile_sprite = pygame.Surface.subsurface(self.sprites, (176, 16, 16, 16))
        self.set_tile_code(3)

    def show(self):
        return pygame.transform.scale(self.tile_sprite, (20, 20))


class Tile04(Tile):
    def __init__(self, pos_x, pos_y):
        Tile.__init__(self, pos_x, pos_y)
        self.tile_sprite = pygame.Surface.subsurface(self.sprites, (13, 16, 20, 20))
        self.set_tile_code(4)

    def show(self):
        return self.tile_sprite