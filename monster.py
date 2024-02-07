import pygame
import random
import animation

class Monster(animation.AnimateSprite):

    def __init__(self, game, name, size, offset=0):
        super().__init__(name, size)
        self.game = game
        self.health = 100
        self.maxHealth = 100
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 300)
        self.rect.y = 512 - offset
        self.loot_amount = 10
        self.start_animation()

    def damage(self, amount):
        self.health -= amount
        # il meurt en reapparessant comme un nouveau monstre
        if self.health <= 0:
            self.rect.x = 1000 + random.randint(0, 500)
            self.speed = random.randint(1, self.default_speed)
            self.health = self.maxHealth
            self.game.add_score(self.loot_amount)
            if self.game.comet_event.is_full_loaded():
                self.game.all_monster.remove(self)
                self.game.comet_event.attempt_fall()


    def set_speed(self, speed):
        self.default_speed = speed
        self.speed = random.randint(3,5)

    def set_loot_amount(self, amount):
        self.loot_amount = amount


    def update_animation(self):
        self.animate(loop=True)

    def update_health_bar(self, suface):

        #dessin de la barre de vie
        pygame.draw.rect(suface, (60, 63, 60), [self.rect.x + 10, self.rect.y - 10, self.maxHealth, 4])
        pygame.draw.rect(suface, (111, 210, 46), [self.rect.x + 10, self.rect.y - 10, self.health, 4])


    def forward(self):
        if not self.game.check_collision(self, self.game.all_player):
            self.rect.x -= self.speed

        else:
            self.game.player.damage(self.attack)


class Mummy(Monster):

    def __init__(self, game):
        super().__init__(game, "mummy", (130,130))
        self.set_speed(5)
        self.attack = 0.3
        self.set_loot_amount(20)



class Alien(Monster):
    def __init__(self, game):
        super().__init__(game, "alien", (250,250), 100)
        self.health = 250
        self.maxHealth = 250
        self.set_speed(3)
        self.attack = 0.8
        self.set_loot_amount(80)
