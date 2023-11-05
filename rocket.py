import pygame,random
from pygame.math import Vector2


class Rocket(object):
    
    
    def __init__(self,game):
        
        self.rocket_length = 1
        self.game = game
        self.gravity =  0.8
        self.speed = 1
        self.pos_list = []
        self.direction = Vector2(0,0)
        self.size = self.game.screen.get_size()
        
        start_pos_x = random.randint(0,self.size[0]-1)
        start_pos_y =  random.randint(0,self.size[1]-1)
        
        self.pos = Vector2(start_pos_x, start_pos_y)
        self.vel = Vector2(0,0)
        self.acc = Vector2(0,0)
        #first position bug  fix xd
        self.pos_list.append(Vector2(9999, 9999))

        
    def add_force(self,force):
        self.acc += force
    

    def tick(self):
        #input
        
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_w]:
            if self.pos[1] > 30:
                self.add_force(Vector2(0,-self.speed))
                self.direction= Vector2(0,+0.2)
        if pressed[pygame.K_s]:
            if self.pos[1] < self.size[1]-100:
                self.add_force(Vector2(0,self.speed ))
                self.direction= Vector2(0,-0.2)
        if pressed[pygame.K_a]:
            if self.pos[0] >30:
                self.add_force(Vector2(-self.speed,0 ))
                self.direction = Vector2(0.2,0)
        if pressed[pygame.K_d]: 
            if self.pos[0] < self.size[0]-100:
                self.rotate()
                self.add_force(Vector2(self.speed,0))
                self.direction = Vector2(-0.2,0)
        #Physics
        self.vel *= self.gravity
        diff_x = self.pos.x - self.pos_list[-1][0]
        diff_y = self.pos.y - self.pos_list[-1][1]
        
        self.slow_move(self.direction)

        
        self.vel += self.acc
        self.pos += self.vel
        self.acc *= 0
        
        
        
        if abs(diff_x) >=25 or abs(diff_y) >= 25: 
            self.pos_list.append([self.pos.x,self.pos.y])

    def slow_move(self, direction):
        if direction.x > 0 :
            if self.pos[0] > 30:
                self.vel -= direction
        elif direction.x < 0 :
            if self.pos[0] <self.size[0]-100 :
                self.vel -= direction
        elif direction.y > 0 :
            if self.pos[1] > 30:
                self.vel -= direction
        elif direction.y < 0 :
            if self.pos[1] < self.size[1]-100:
                self.vel -= direction
           


        
    def rotate(self):
        pass
        
        
    def draw(self):
        rocket_img = pygame.image.load('spaceship.png')
        angle = self.vel.angle_to(Vector2(0,-1))
        rocket = pygame.transform.rotate(rocket_img, angle)
        
        self.game.screen.blit(rocket, self.pos)
        #if len(self.pos_list) > 0:
        #    self.pos_list.pop()
        #star_positions = list(reversed(self.pos_list))
        
        for i in range(self.rocket_length):
            star_pos= Vector2(self.pos_list[-i][0]+15,self.pos_list[-i][1]+15)         
            star_img = pygame.image.load('star_smile.png')

            self.game.screen.blit(star_img,star_pos)
        
        
        
        
        #Base triangle
        #points = [Vector2(0,-10), Vector2(5,5),Vector2(-5,5)]
        
        #rotate points
        
        #points = [p.rotate(angle) for p in points]
        
        #Fix y axis
        #points = [Vector2(p.x,p.y*-1) for p in points]
        
        #add current position
        #points = [self.pos+p*3 for p in points]
        
        
        #draw triangle
        #pygame.draw.polygon(self.game.screen, (255,255,0),points)
        

        #rect = pygame.Rect(self.pos.x, self.pos.y, 50,50)
        #pygame.draw.rect(self.game.screen,(50,100,200),rect)