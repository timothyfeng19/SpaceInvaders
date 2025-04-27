import pygame

class Lazer:
    def __init__(self):
        self.image = pygame.image.load("images/lazer.png")
        self.image = pygame.transform.smoothscale_by(self.image, (0.3, 0.3))
        self.x = 400
        self.y = 700
        self.speed = 15
        self.state = "ready"
        self.hitbox = self.image.get_rect(topleft=(self.x,self.y))

    def shoot(self, x):
        self.x = x + 20.7
        self.y = 700
        self.state = "shoot"

    def move(self):
        if self.state == "shoot":
            self.y -= self.speed
            self.hitbox = self.image.get_rect(topleft=(self.x,self.y))
        if self.y <= -100:
            self.state = "ready"

    def draw(self, screen):
        if self.state == "shoot":
            screen.blit(self.image, (self.x, self.y))

    def is_collision(self, alien):
        return self.hitbox.colliderect(alien.hitbox)

