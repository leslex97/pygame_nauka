import pygame,sys
from rocket import Rocket
from star import Star

class Game(object):
    
    
    def __init__(self):
        # Config
        self.max_tps = 85
        self.counter = 0
        #Initialization
        pygame.init()
        
        self.screen_res = (1270,700)
        self.screen =  pygame.display.set_mode(self.screen_res)
        self.tps_clock = pygame.time.Clock()
        self.tps_delta = 0.0
        
        self.player = Rocket(self)
        self.star = Star(self)
        bg = pygame.image.load("space.png")
        bg = pygame.transform.scale(bg, self.screen_res)

        while True:
            #Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)

            self.tps_delta+=self.tps_clock.tick()/1000.0
            while self.tps_delta> 1 / self.max_tps:
                self.tick()
                self.tps_delta -=1 /self.max_tps

            #Drawing
            self.screen.fill((0,0,0))
            
            #Background image 
            self.screen.blit(bg,(0,0))
            #show score
            font = pygame.font.Font('freesansbold.ttf', 32)
            text = font.render(f'Score: {self.counter}', True, (255,255,255))
            textRect = text.get_rect()
            textRect.center = (self.screen_res[0]/2, 25)
            self.screen.blit(text, textRect)
            
            self.draw()
            pygame.display.update()
            self.catch()
        
    def tick(self):
        self.player.tick()
        self.star.tick()
            
    def draw(self):
        self.player.draw()
        self.star.draw()
    
    def catch(self):
        space_delta = 30
        x_catch_pos = abs(self.player.pos[0]-self.star.pos[0])
        y_catch_pos = abs(self.player.pos[1]-self.star.pos[1])
        
        if x_catch_pos < space_delta and y_catch_pos < space_delta:
            self.player.rocket_length+=1
            self.counter +=1
            del self.star
            self.star = Star(self)
        
        


if __name__ == "__main__":
    Game()