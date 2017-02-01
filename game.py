import pygame
import functions
pygame.init()
width = 1500
height = 800
screen = pygame.display.set_mode((width,height))
pygame.display.update()


def Game():
    Main_menu=True
    while Main_menu:
        events = pygame.event.get()
        functions.insert_image('MenuBackgound.jpg', 0,0)
        functions.button((0, 89, 90), 650, 300, 200, 70, 'button3.png', functions.intro_game, events)
        functions.button((0, 89, 90), 650, 400, 200, 70, 'button2.png', functions.help, events)
        functions.button((0, 89, 90), 650, 500, 200, 70, 'button1.png', functions.see_highscores, events)
        functions.button((0, 89, 90), 650, 600, 200, 70, 'button5.png', functions.settings,events)
        functions.button((0, 89, 90), 650, 700, 200, 70, 'button4.png', exit, events)

        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.display.update()
Game()

