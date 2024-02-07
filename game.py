#creation classe du jeu
import pygame

from player import Player
from monster import Monster, Mummy, Alien
from comet_event import CometFallEvent
from sounds import SoundManager


class Game:

    def __init__(self):

        #def si le jeu a commence
        self.is_playing = False

        self.all_player = pygame.sprite.Group()
        self.player = Player(self)
        self.all_player.add(self.player)

        self.comet_event = CometFallEvent(self)

        self.all_monster = pygame.sprite.Group()

        self.sound_manager = SoundManager()

        self.font = pygame.font.Font("assets/my_custom_font.ttf", 25)


        self.score = 0
        self.pressed = {}


    def start(self):
        self.is_playing = True
        self.spawn_monster(Mummy)
        self.spawn_monster(Mummy)
        self.spawn_monster(Mummy)
        self.spawn_monster(Alien)


    def add_score(self, points=10):
        self.score += points

    def game_over(self):
        self.sound_manager.play('game_over')
        self.all_monster = pygame.sprite.Group()
        self.comet_event.all_comets = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.comet_event.reset_percent()
        self.is_playing = False
        self.score = 0


    def update(self, screen):

        #Google font
        score_text = self.font.render(f"Score : {self.score}", 1, (0,0,0))
        screen.blit(score_text, (20,20))

        screen.blit(self.player.image, self.player.rect )

        self.player.update_health_bar(screen)

        self.comet_event.update_bar(screen)

        self.player.update_animation()

        for projectile in self.player.all_projectile:
            projectile.move()

        for monster in self.all_monster:
            monster.forward()
            monster.update_health_bar(screen)
            monster.update_animation()

        for comet in self.comet_event.all_comets:
            comet.fall()

        self.player.all_projectile.draw(screen)

        self.all_monster.draw(screen)

        self.comet_event.all_comets.draw(screen)

        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()


    def spawn_monster(self, monster_class_name):
        self.all_monster.add(monster_class_name.__call__(self))


    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)
