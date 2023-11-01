import pygame, random
from pygame.math import Vector2

class Star(object):
    
    def __init__(self,game):
        self.game = game
        self.size = self.game.screen.get_size()
        self.x = random.randint(0,self.size[0]-1)
        self.y = random.randint(0,self.size[1]-1)
        self.pos = Vector2(self.x,self.y)
    
    def tick(self):
        pass
    
    def draw(self):
        rect = pygame.Rect(self.pos.x, self.pos.y, 30,30)
        pygame.draw.rect(self.game.screen,(150,200,0),rect)
