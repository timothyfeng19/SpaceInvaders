import pygame
import random
from alien import Alien
from ship import Ship
from lazer import Lazer

class SpaceInvaders():

    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption("Space Invaders")
        self.ship = Ship(400, 700)
        self.lazer = Lazer()
        self.aliens = []
        for a in range(4):
            for b in range(10):
                self.aliens.append(Alien(60 * b + 50, 60 * a + 50))
        self.shoot_sound = pygame.mixer.Sound("sounds/laser.mp3")
        self.boom_sound = pygame.mixer.Sound("sounds/boom.mp3")
        self.shoot_sound.set_volume(0.3)
        self.boom_sound.set_volume(0.6)
        self.heart = pygame.image.load("images/heart.png")
        self.heart = pygame.transform.smoothscale_by(self.heart, (0.05, 0.05))
        self.font = pygame.font.SysFont('Verdana', 80, True)
        self.text = self.font.render('You Win', False, (255, 255, 255))
        self.over = self.font.render('Game Over', False, (255, 0, 0))
        self.dead = False


    def detect_alien_collision(self):
        for i in range(len(self.aliens) -1, -1, -1):
            if self.lazer.is_collision(self.aliens[i]):
                self.boom_sound.play()
                self.aliens.remove(self.aliens[i])
                self.lazer.state = "ready"
                self.lazer.x = 400
                self.lazer.y = 700
                self.lazer.hitbox = self.lazer.image.get_rect(topleft=(self.lazer.x, self.lazer.y))

    def detect_ship_collision(self):
        for i in range(len(self.aliens) -1, -1, -1):
            if self.aliens[i].lazer != None:
                if self.aliens[i].lazer.hitbox.colliderect(self.ship.hitbox):
                    self.ship.lives -= 1
                    if self.ship.lives == 0:
                        self.ship.y = 9999
                        self.dead = True
                    self.aliens[i].lazer = None

    def detect_alien_ship_collision(self):
        for i in range(0, len(self.aliens)):
            if self.aliens[i].hitbox.colliderect(self.ship.hitbox):
                pygame.quit()

    def draw_hearts(self, screen):
        for i in range(self.ship.lives):
            screen.blit(self.heart, (28*i+10, 770))

    def move_alien_lazer(self):
        for i in range(len(self.aliens)):
            self.aliens[i].update_lazer()

    def play(self):
        pygame.init()

        screen = pygame.display.set_mode((800, 800))
        clock = pygame.time.Clock()
        
        alien_buffer = 0
        ship_buffer = 50
        die_buffer = 0
        playing = True
        
        while playing == True:
            if alien_buffer == 40 and len(self.aliens) > 0:
                random_alien = random.randint(0, len(self.aliens)-1)
                self.aliens[random_alien].shoot()
                self.shoot_sound.play()
                alien_buffer = 0

            elif len(self.aliens) == 0:
                playing = False

            else:
                alien_buffer += 1
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and ship_buffer >= 50 and self.dead == False:
                        self.shoot_sound.play()
                        self.lazer.shoot(self.ship.x)
                        ship_buffer = 0
            
            ship_buffer += 1
            self.ship.press_down()
            screen.fill((0, 0, 0))

            self.lazer.move()
            self.lazer.draw(screen)
            self.draw_hearts(screen)
            self.move_alien_lazer()

            for i in range(len(self.aliens)):
                self.aliens[i].draw(screen)
                self.aliens[i].move()

            self.ship.draw(screen)
            self.detect_alien_collision()
            self.detect_ship_collision()

            if self.dead == True:
                screen.blit(self.over, (160, 300))
                die_buffer += 1
                if die_buffer > 100:
                    pygame.quit()

            pygame.display.flip()
            clock.tick(60)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            screen.blit(self.text, (220, 300))
            pygame.display.flip()