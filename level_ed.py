import pygame
import pickle
import sys
from map.tiles import *


class LevelEd:
    SHOW_TILES_HUD = False

    screen = None
    clock = None
    width = 0
    height = 0

    active_square_x = 0
    active_square_y = 0

    active_x = 0
    active_y = 0

    """stores information about all 640x480 tiles"""
    tiles = []

    def __init__(self, width, height):
        pygame.init()
        pygame.display.set_caption('JungleRun! - Level Editor')
        self.clock = pygame.time.Clock()
        self.width = width
        self.height = height
        self.active_tile = Tile.t04
        self.screen = pygame.display.set_mode([self.width, self.height])

        """fill tiles list"""
        self.tiles = [[0 for i in range(32)] for j in range(24)]

    def show_info(self, info, start_pos, line_height=10):
        font = pygame.font.Font("assets/fonts/m5x7.ttf", 16)
        font_color = (255, 255, 255)
        for line in info:
            self.screen.blit(font.render(line, 1, font_color), start_pos)
            start_pos[1] = start_pos[1] + line_height

    def debug_info(self):
        mouse_pos = pygame.mouse.get_pos()
        line = []
        line.append("Mouse x,y: %d,%d" % (mouse_pos[0], mouse_pos[1]))
        line.append("Potential x,y: %d,%d" % ((mouse_pos[0] / 20) + 1, (mouse_pos[1] / 20) + 1))
        line.append("Active x,y: %d,%d" % (self.active_x, self.active_y))
        self.show_info(line, [5, 5])

    def show_grid(self):
        """Shows grid - for editor"""
        grid_color = (60, 60, 60)
        for i in range(20, self.height, 20):
            pygame.draw.line(self.screen, grid_color, (0, i), (self.width, i), 1)
        for i in range(20, self.width, 20):
            pygame.draw.line(self.screen, grid_color, (i, 0), (i, self.height), 1)

    def highlight_active_square(self):
        """"""
        color = (180, 180, 180)
        points = []
        points.append((self.active_x, self.active_y))
        points.append((self.active_x - 20, self.active_y))
        points.append((self.active_x - 20, self.active_y - 20))
        points.append((self.active_x, self.active_y - 20))
        pygame.draw.lines(self.screen, color, True, points, 1)

    def show_tiles_hud(self):
        pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect((500, 0, 140, 480)))

        """show hud grid"""
        # grid_color = (30, 30, 30)
        # for i in range(20, self.height, 20):
        #     pygame.draw.line(self.screen, grid_color, (500, i), (self.width, i), 1)
        # for i in range(500, self.width, 20):
        #     pygame.draw.line(self.screen, grid_color, (i, 0), (i, self.height), 1)

        font = pygame.font.Font("assets/fonts/m5x7.ttf", 22)
        font_color = (255, 255, 255)
        self.screen.blit(font.render("1x1", 1, font_color), (560, 10))
        grass_tile = Tile01(520, 40)
        self.screen.blit(grass_tile.show(), grass_tile.get_position())
        bush_tile = Tile04(560, 40)
        self.screen.blit(bush_tile.show(), bush_tile.get_position())
        bush_tile = Tile02(600, 40)
        self.screen.blit(bush_tile.show(), bush_tile.get_position())

        mouse_pos = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed() == (1, 0, 0):
            if mouse_pos[0] >= 520 and mouse_pos[0] <= 540 and mouse_pos[1] >= 40 and mouse_pos[1] <= 60:
                self.active_tile = Tile.t01
            if mouse_pos[0] >= 560 and mouse_pos[0] <= 580 and mouse_pos[1] >= 40 and mouse_pos[1] <= 60:
                self.active_tile = Tile.t04
            if mouse_pos[0] >= 600 and mouse_pos[0] <= 620 and mouse_pos[1] >= 40 and mouse_pos[1] <= 60:
                self.active_tile = Tile.t02

            """save button"""
            if mouse_pos[0] >= 520 and mouse_pos[0] <= 620 and mouse_pos[1] >= 400 and mouse_pos[1] <= 480:
                self.save_level_data()

    def save_level_data(self):
        print("save to file")
        tmp_tiles = []
        for x in range(0, 32):
            for y in range(0, 24):
                if self.tiles[y][x].__class__ is int:
                    value = 0
                else:
                    value = self.tiles[y][x].get_tile_code()
                tmp_tiles.append(value)

        print(tmp_tiles)
        with open("level01.lvl", "wb") as fp:
            pickle.dump(tmp_tiles, fp)

    def show_active_tile(self, pos_x, pos_y):
        pygame.draw.circle(self.screen, (100, 100, 100), (pos_x + 12, pos_y + 11), 20, 2)
        pygame.draw.circle(self.screen, (125, 125, 125), (pos_x + 12, pos_y + 11), 19, 1)
        pygame.draw.circle(self.screen, (150, 150, 150), (pos_x + 12, pos_y + 11), 18, 1)
        tile_class = getattr(__import__("map.tiles", globals(), locals(), self.active_tile), self.active_tile)
        active_tile = tile_class(0, 0)
        self.screen.blit(active_tile.show(), (pos_x, pos_y))

    def refresh(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_x = mouse_pos[0] + 20
        mouse_y = mouse_pos[1] + 20
        self.active_square_x = (mouse_pos[0] // 20) + 1
        self.active_square_y = (mouse_pos[1] // 20) + 1
        self.active_x = self.active_square_x * 20
        self.active_y = self.active_square_y * 20

        """load tiles from list"""
        for i in range(0, 32, 1):
            for j in range(0, 24, 1):
                if self.tiles[i][j]:
                    self.screen.blit(self.tiles[i][j].show(), self.tiles[i][j].get_position())

        self.highlight_active_square()

        if self.SHOW_TILES_HUD:
            self.show_tiles_hud()

        self.show_active_tile(mouse_x, mouse_y)

        self.clock.tick(FPS)
        pygame.display.flip()

    def add_tile(self):
        if not self.SHOW_TILES_HUD or self.SHOW_TILES_HUD and self.active_x <= 500:
            tile_class = getattr(__import__("map.tiles", globals(), locals(), self.active_tile), self.active_tile)
            self.tiles[self.active_square_x - 1][self.active_square_y - 1] = tile_class(self.active_x - 20, self.active_y - 20)

    def remove_tile(self):
        if not self.SHOW_TILES_HUD or self.SHOW_TILES_HUD and self.active_x <= 500:
            self.tiles[self.active_square_x - 1][self.active_square_y - 1] = False


if __name__ == '__main__':
    FPS = 25

    leveled = LevelEd(640, 480)
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_TAB: leveled.SHOW_TILES_HUD = leveled.SHOW_TILES_HUD == False
                if event.key == pygame.K_q: sys.exit()

        leveled.screen.fill((40, 40, 40))
        leveled.show_grid()

        if pygame.mouse.get_pressed() == (1, 0, 0):
            leveled.add_tile()
        elif (pygame.mouse.get_pressed() == (0, 0, 1)):
            leveled.remove_tile()

        leveled.debug_info()

        info = []
        info.append("Help:")
        info.append("  h - help")
        info.append("  tab - tiles")
        info.append("  left click - add tile")
        info.append("  right click - remove tile")
        info.append("  g - grid")
        info.append("  b - background")
        info.append("  s - save - TODO")
        info.append("  q - quit")
        leveled.show_info(info, [5, 380])

        leveled.refresh()
