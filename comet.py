import pygame
import random

class Comet(pygame.sprite.Sprite):

    def __init__(self, comet_event):
        super().__init__()

        self.image = pygame.image.load('assets/comet.png')
        self.image = pygame.transform.scale(self.image, (120,120))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(20,1100)
        self.rect.y = - random.randint(0,500)
        self.comet_event = comet_event

    def remove(self):
        self.comet_event.all_comets.remove(self)
        if len(self.comet_event.all_comets) <= 0:
            self.comet_event.reset_percent()
            self.comet_event.game.start()

    def fall(self):
        self.rect.y += 4
        self.comet_event.game.sound_manager.play('meteorite')
        if self.rect.y >= 500:
            self.remove()
            if len(self.comet_event.all_comets) <= 0:
                self.comet_event.reset_percent()
                self.comet_event.fall_mode = False

        if self.comet_event.game.check_collision(self, self.comet_event.game.all_player):
            self.remove()
            self.comet_event.game.player.damage(20)
