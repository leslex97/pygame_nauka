import pygame,random
from pygame.math import Vector2

class Rocket(object):
    
    
    def __init__(self,game):
        self.game = game
        self.gravity =  0.8
        self.speed = 1
        
        self.size = self.game.screen.get_size()
        
        self.pos = Vector2(random.randint(0,self.size[0]-1), random.randint(0,self.size[1]-1))
        self.vel = Vector2(0,0)
        self.acc = Vector2(0,0)
    
    def add_force(self,force):
        self.acc += force
    
    
    def tick(self):
        #input
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_w]:
            if self.pos[1] > 30:
                self.add_force(Vector2(0,-self.speed))
                
        if pressed[pygame.K_s]:
            if self.pos[1] < self.size[1]-50:
                self.add_force(Vector2(0,self.speed ))
        
        if pressed[pygame.K_a]:
            if self.pos[0] >30:
                self.add_force(Vector2(-self.speed,0 ))
                
        if pressed[pygame.K_d]: 
            if self.pos[0] < self.size[0]-30:
                self.add_force(Vector2(self.speed,0))
        
        #Physics
        self.vel *= self.gravity
        if self.pos[1] < self.size[1]-30:
            self.vel -= Vector2(0,-0.2)
        
        self.vel += self.acc
        self.pos += self.vel
        self.acc *= 0
    

    
    def draw(self):
        
        #Base triangle
        points = [Vector2(0,-10), Vector2(5,5),Vector2(-5,5)]
        
        #rotate points
        angle = self.vel.angle_to(Vector2(0,1))
        points = [p.rotate(angle) for p in points]
        
        #Fix y axis
        points = [Vector2(p.x,p.y*-1) for p in points]
        
        #add current position
        points = [self.pos+p*3 for p in points]
        
        #draw triangle
        pygame.draw.polygon(self.game.screen, (255,255,0),points)
        

        #rect = pygame.Rect(self.pos.x, self.pos.y, 50,50)
        #pygame.draw.rect(self.game.screen,(50,100,200),rect)