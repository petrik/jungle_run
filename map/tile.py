import pygame


class Tile(pygame.sprite.Sprite):
    pos_x = 0
    pos_y = 0
    sprites = None
    tile_sprite = None
    rect = None
    width = 20
    height = 20
    code = 0

    t01 = 'Tile01'
    t02 = 'Tile02'
    t03 = 'Tile03'
    t04 = 'Tile04'

    def __init__(self, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
        """load tiles sprite"""
        try:
            self.sprites = pygame.image.load('assets/sprites/jungle_tileset.png').convert_alpha()
        except:
            print("Unable to load tiles assets.")
            raise
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.set_collision_rect()

    def set_collision_rect(self):
        self.rect = pygame.Rect((self.pos_x, self.pos_y, self.width, self.height))

    def get_position(self):
        return self.pos_x, self.pos_y

    def set_tile_code(self, code):
        self.code = code

    def get_tile_code(self):
        return self.code
