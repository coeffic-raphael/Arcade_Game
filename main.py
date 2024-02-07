import pygame
from game import Game
pygame.init()


clock = pygame.time.Clock()
FPS = 60


# generer la fenetre du jeu
pygame.display.set_caption("Comet fall Game")
screen = pygame.display.set_mode((1200, 650))

background = pygame.image.load('assets/bg.jpg')

banner = pygame.image.load('assets/banner.png')
banner = pygame.transform.scale(banner, (500,500))
banner_rect = banner.get_rect()
banner_rect.x = screen.get_width()/4

#boutton play
play_button = pygame.image.load('assets/button.png')
play_button = pygame.transform.scale(play_button, (400,150))
play_button_rect = play_button.get_rect()
play_button_rect.x = screen.get_width()/3.33
play_button_rect.y = screen.get_height()/1.85


# charger joueur
#player = Player()

#charger jeu
game = Game()
game.sound_manager.play('game')
running = True

# boucle qui s'execute tant que running == true
while running:

    screen.blit(background, (-900,-230))
    if game.is_playing:
        game.update(screen)

    else:
        screen.blit(play_button, play_button_rect)
        screen.blit(banner, banner_rect)




    #mettre a jour l'ecran
    pygame.display.flip()

    # si le joueur ferme la fenetre
    for event in pygame.event.get():
        # que l evenement est fermeture de fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.QUIT

        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()


        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if play_button_rect.collidepoint(event.pos):
                game.start()
                game.sound_manager.play('click')

    clock.tick(FPS)