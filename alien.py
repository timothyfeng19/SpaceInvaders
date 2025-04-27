import pygame
from alien_lazer import AlienLazer

class Alien:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("images/alien.png")
        self.image = pygame.transform.smoothscale_by(self.image, (0.2, 0.2))
        self.hitbox = self.image.get_rect(topleft=(self.x, self.y))
        self.speed = 1
        self.lazer = None

    def move(self):
        self.x = self.x + self.speed
        if self.x >= 750 or self.x <= 50:
            self.speed *= -1
            self.y += 30
        self.hitbox = self.image.get_rect(topleft=(self.x, self.y))

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
        if self.lazer != None:
            self.lazer.draw(screen)

    def shoot(self):
        self.lazer = AlienLazer(self.x+16, self.y)

    def update_lazer(self):
        if self.lazer != None:
            self.lazer.move()
            if self.lazer.y > 800:
                self.lazer = None
