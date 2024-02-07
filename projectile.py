import pygame

class Projectile(pygame.sprite.Sprite):

    def __init__(self, player):
        super().__init__()
        self.speed = 8
        self.player = player
        self.image = pygame.image.load('assets/projectile.png')
        self.image = pygame.transform.scale(self.image, (40,40))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 130
        self.rect.y = player.rect.y + 80
        self.origin_image = self.image
        self.angle = 0

    def rotate(self):
        self.angle += 5
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center= self.rect.center)
    def remove(self):
        self.player.all_projectile.remove(self)

    def move(self):
        self.rect.x += self.speed

        self.rotate()

        for monster in self.player.game.check_collision(self, self.player.game.all_monster):
            self.remove()
            monster.damage(self.player.attack)

        if self.rect.x > self.player.rect.x + 600:
            self.remove()