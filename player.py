# creation classe du joueur
import pygame
from projectile import Projectile
import animation

class Player(animation.AnimateSprite):

    def __init__(self, game):
        super().__init__('player')
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 25
        self.velocitySpeed = 5
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 470
        self.all_projectile = pygame.sprite.Group()


    def damage(self, amount):
        if self.health - amount >= amount:
            self.health -= amount

        else:
            self.game.game_over()

    def launch_projectile(self):
        self.all_projectile.add(Projectile(self))
        self.start_animation()
        self.game.sound_manager.play('tir')


    def move_right(self):
        if not self.game.check_collision(self, self.game.all_monster):
            self.rect.x += self.velocitySpeed

    def move_left(self):
        self.rect.x -= self.velocitySpeed

    def update_animation(self):
        self.animate()

    def update_health_bar(self, suface):

        #dessin de la barre de vie
        pygame.draw.rect(suface, (60, 63, 60), [self.rect.x + 50, self.rect.y + 20, self.max_health, 6])
        pygame.draw.rect(suface, (111, 210, 46), [self.rect.x + 50, self.rect.y + 20, self.health, 6])