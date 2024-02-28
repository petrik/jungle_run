import pygame

class Character(pygame.sprite.Sprite):
    pos_x = None
    pos_y = None

    pos_center_x = None
    pos_center_y = None

    """velocity"""
    vel_x = 0
    vel_y = 0

    """speed"""
    speed = 0

    """character sprite"""
    height = 0
    width = 0

    """collision rectangle"""
    rect = None

    """sight radius"""
    sight_radius = 0

    """character state params"""
    on_ground = True
    direction_right = True

    def __init__(self, start_position_x, start_position_y):
        pygame.sprite.Sprite.__init__(self)

        self.pos_x = start_position_x
        self.pos_y = start_position_y

    def get_sight_radius(self):
        return self.sight_radius

    def set_sight_radius(self, value):
        self.sight_radius = value

    def get_position(self):
        return self.pos_x, self.pos_y

    def debug_get_info(self):
        """generates debug information about character"""
        info = []
        info.append("Sight radius: %d" % (self.sight_radius))
        info.append("Current position x,y: %d,%d" % (self.pos_x, self.pos_y))
        info.append("Current X velocity: %d" % (self.vel_x))
        info.append("Current Y velocity: %d" % (self.vel_y))
        info.append("On ground: " + str(self.on_ground))
        return info

    def debug_draw_collision_box(self, surface):
        """Draws collision box"""
        pygame.draw.rect(surface, (255, 0, 0), self.rect)

    def debug_draw_light_radius(self, surface):
        """Draws light radius"""
        pygame.draw.circle(surface, (100, 100, 100), (self.pos_x + self.width / 2, self.pos_y + self.height / 2), self.sight_radius)

    def get_updated_position(self):
        """Updates position and returns, new calculated position x,y"""

        return self.pos_x, self.pos_y
