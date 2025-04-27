import pygame

class AlienLazer():
    def __init__(self, x, y):
        self.image = pygame.image.load("images/lazer.png")
        self.image = pygame.transform.smoothscale_by(self.image, (0.3, 0.3))
        self.speed = 15
        self.x = x
        self.y = y
        self.hitbox = self.image.get_rect(topleft=(self.x,self.y))

    def move(self):
        self.y += self.speed
        self.hitbox = self.image.get_rect(topleft=(self.x,self.y))

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))