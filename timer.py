import pygame
Clock = pygame.time.Clock()


class timer :
    Table = []
    def __init__(self, threshold, function) :
        timer.Table.append(self)
        self.threshold = threshold
        self.time = 0
        self.func = function
        
            
            
    def update(self) :
        #print("updated")
        self.time += Clock.get_time()
        
        if self.time > self.threshold :
            self.time = self.time - self.threshold
            self.func()
        
    def reset(self) :
        self.time = 0

