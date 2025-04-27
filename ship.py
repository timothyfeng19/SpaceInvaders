import pygame

class Ship:
    def __init__(self, x, y):
        self.image = pygame.image.load("images/ship.png")
        self.image = pygame.transform.smoothscale_by(self.image, (0.1, 0.1))
        self.speed = 10
        self.x = x
        self.y = y
        self.hitbox = self.image.get_rect(topleft=(self.x, self.y))
        self.lives = 3

    def press_down(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            if self.x > 0:
                self.x -= self.speed
            self.hitbox = self.image.get_rect(topleft=(self.x, self.y))

        if keys[pygame.K_RIGHT]:
            if self.x < 750:
                self.x += self.speed
            self.hitbox = self.image.get_rect(topleft=(self.x, self.y))
    
    def draw(self, screen):
        # pygame.draw.rect(screen, (255, 0, 0), self.hitbox) - this draws the ship's hitbox
        screen.blit(self.image, (self.x, self.y))