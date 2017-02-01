import pygame
# import psycopg2
# conn = psycopg2.connect("dbname= Project_2_Highscore name = postgres password = 1")
# cursor = conn.cursor()
pygame.init()
pygame.font.init()
events = pygame.event.get()
width = 1000
height = 1000
screen = pygame.display.set_mode((width,height))
pygame.mixer.init()
text_type = pygame.font.get_default_font()
font = pygame.font.Font(text_type, 25)
boot = pygame.image.load('Boot-1-offense-mode.png')
boot2 = pygame.image.load('Boot-2-offense-mode.png')
boot3 = pygame.image.load('Boot-2.1-offense-mode.png')
boot4 = pygame.image.load('Boot-3-offense-mode.png')
player2_boot = pygame.image.load('Player-1-Boot-1-offense-mode.png')
player2_boot2 = pygame.image.load('Player-2-Boot-2-offense-mode.png')
player2_boot3 = pygame.image.load('Player-2-Boot-3-offense-mode.png')
player2_boot4 = pygame.image.load('Player-2-Boot-4-offense-mode.png')
enter_button = pygame.image.load('enter.png')
gameboard = pygame.image.load('gameboard.png')


pygame.mixer.music.load('MainMenuTheme.wav')
pygame.mixer.music.play(-1)

def button(color, p_x, p_y, width,height, image,loop, events):
    buttons = pygame.draw.rect(screen,color,[p_x, p_y, width, height])
    if image != None:
        screen.blit(pygame.image.load(image), (p_x, p_y))
    pressed = pygame.mouse.get_pressed()
    if loop != None:
        if pressed[0] == 1 and buttons.collidepoint(pygame.mouse.get_pos()):
            if loop == intro_game:
                pygame.mixer.music.load('StartGameButtonSound.wav')
                pygame.mixer.music.play(0)
            if loop == see_highscores:
                pygame.mixer.music.load('highscores_soundtrack.wav')
                pygame.mixer.music.play(0)
            loop()


    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
def insert_image(image, positionx, positiony):
    screen.blit(pygame.image.load(image),(positionx,positiony))


class Player:
    def __init__(self):
        self.name = "**"
        self.score = 0
        self.boats = []
    def show_name(self, x, y):
        screen.blit(font.render(self.name,1,(255,255,255)), (x, y))

player1 = Player()
player2 = Player()

class Boat:
    def __init__ (self, img, x, y, hp, type, text_pos_x, text_posy, moves):
        self.image = img
        self.p_x = x
        self.p_y = y
        self.text_pos_x = text_pos_x
        self.text_pos_y = text_posy
        self.health = hp
        self.moves = moves
        self.turn = moves
        self.boat_type = type
    def show_state(self):
        screen.blit(font.render(' Boot %d : ' % (self.boat_type), 1, (0, 0, 0)),(self.text_pos_x, self.text_pos_y))
        screen.blit(font.render(' Health = %d ' % (self.health), 1, (0, 0, 0)), (self.text_pos_x, self.text_pos_y + 30))
        screen.blit(font.render(' Moves = %d ' % (self.turn), 1, (0, 0, 0)), (self.text_pos_x, self.text_pos_y + 60))
    def reset_turn(self):
        self.turn == self.moves
       #for boat in player.boats:
            #if boat.turn <0 or boat.turn== 0:
                #for boat in player2.boats:
                    #boat.turn == boat.moves
        #for boat in player2.boats:
            #if boat.turn <0 or boat.turn==0:
                #for boat in player.boats:
                    #boat.turn== boat.moves

    def move(self):
        if self.turn > 0:
            move_key = pygame.key.get_pressed()
            if self.p_x < 902 and self.p_x > 199:
                if move_key[pygame.K_RIGHT]:
                    self.p_x = self.p_x + 37
                    self.turn-=1
                elif move_key[pygame.K_LEFT]:
                    self.p_x = self.p_x - 37
                    self.turn -=1
            elif self.p_x == 199:
                if move_key[pygame.K_RIGHT]:
                    self.p_x += 37
                    self.turn -= 1
            elif self.p_x == 902:
                if move_key[pygame.K_LEFT]:
                    self.p_x -= 37
                    self.turn -= 1
            if self.p_y <600 and self.p_y > 109:
                if move_key[pygame.K_UP]:
                    self.p_y = self.p_y + 37
                    self.turn -= 1
                elif move_key[pygame.K_DOWN]:
                    self.p_y = self.p_y - 37
                    self.turn -= 1
            elif self.p_y == 109:
                if move_key[pygame.K_UP]:
                    self.p_y += 37
                    self.turn -= 1
            elif self.p_y == 600:
                if move_key[pygame.K_DOWN]:
                    self.p_x -= 37
                    self.turn -= 1
            print(self.turn)

def choose_name():
    choose= True
    first_player= True
    while choose:
        screen.fill((255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and first_player == True:
                if event.unicode.isalpha():
                    player1.name += event.unicode
                elif event.unicode.isdigit():
                    player1.name += event.unicode
                elif event.key == pygame.K_BACKSPACE:
                    player1.name = player1.name [:-1]
                elif event.key == pygame. K_SPACE:
                    player1.name += " "
                elif event.key == pygame.K_RETURN:
                    first_player = False
            elif event.type == pygame.KEYDOWN and first_player == False:
                screen.blit(font.render(player2.name, 1, (0, 0, 0)), (650, 300))
                if event.unicode.isalpha() :
                    player2.name += event.unicode
                elif event.unicode.isdigit():
                    player2.name += event.unicode
                elif event.key == pygame.K_BACKSPACE:
                    player2.name = player2.name [:-1]
                elif event.key == pygame. K_SPACE:
                    player2.name += " "
                elif event.key == pygame.K_RETURN:
                    choose = False
            elif event.type == pygame.QUIT:
                pygame.quit()
                quit()

        if first_player == True:
            screen.blit(font.render('Player 1: Type your name', 1, (0, 0, 0)), (600, 200))
            screen.blit(font.render(player1.name, 1, (0, 0, 0)), (650, 300))
        elif first_player == False:
            screen.blit(font.render('Player 2: Type your name', 1, (0, 0, 0)), (600, 200))
            screen.blit(font.render(player2.name, 1, (0, 0, 0)), (650, 300))



        pygame.display.update()

def intro_game():
    choose_name()
    x = 199
    y = 109
    gameExit = False
    pygame.mixer.music.load('Elevator_Music.wav')
    pygame.mixer.music.play(-1)
    while not gameExit:
        surface = pygame.draw.rect(screen, (0, 0, 0), [200, 100, 750, 600])
        screen.blit(gameboard, (0, 0))
        insert_image('pause_button.png', 1442, 0)
        player1.show_name(20, 20)
        player2.show_name(1000, 20)
        pause_button= pygame.image.load('pause_button.png').get_rect(x=1442,y=0)
        if len(player1.boats) < 4:
            if len(player1.boats) < 1:
                screen.blit(boot, (x, y))
            elif len(player1.boats) < 2:
                screen.blit(boot2, (x, y))
            elif len(player1.boats) < 3:
                screen.blit(boot3, (x, y))
            elif player1.boats.count(boot4) < 1:
                screen.blit(boot4, (x, y))
        elif len(player2.boats) < 4:
            if len(player2.boats) < 1:
                screen.blit(player2_boot, (x, 637))
            elif len(player2.boats) < 2:
                screen.blit(player2_boot2, (x, 608))
            elif len(player2.boats) < 3:
                screen.blit(player2_boot3, (x, 608))
            elif player2.boats.count(boot4) < 1:
                screen.blit(player2_boot4, (x, 579))
        move_key = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and pause_button.collidepoint(pygame.mouse.get_pos()):
                pause_loop()
            elif x < 902 and x > 199:
                if move_key[pygame.K_RIGHT]:
                    x = x + 37
                    p = x
                elif move_key[pygame.K_LEFT]:
                    x -= 37
            elif x == 199:
                if move_key[pygame.K_RIGHT]:
                    x += 37
            elif x == 902:
                if move_key[pygame.K_LEFT]:
                    x -= 37
            if len(player1.boats) < 4:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and surface.collidepoint(pygame.mouse.get_pos()):
                    if len(player1.boats) == 0:
                        player1.boats.append(Boat(boot,x,y,2,1,20,100,3))
                    elif len(player1.boats) < 2:
                        player1.boats.append(Boat(boot2,x,y,3,2,20, 210,2))
                    elif len(player1.boats) < 3:
                        player1.boats.append(Boat(boot3, x,y,3,3,20, 320,2))
                    elif player1.boats.count(boot4) < 1:
                        player1.boats.append(Boat(boot4, x,y,4,4,20, 430,1))
            elif len(player2.boats) < 4:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and surface.collidepoint(pygame.mouse.get_pos()):
                    if len(player2.boats) == 0:
                        player2.boats.append(Boat(player2_boot,x,637,2,1,1000, 100,3))
                    elif len(player2.boats) < 2:
                        player2.boats.append(Boat(player2_boot2,x,608,3,2,1000, 210,2))
                    elif len(player2.boats) < 3:
                        player2.boats.append(Boat(player2_boot3, x, 608,3,3,1000, 320,2))
                    elif player2.boats.count(player2_boot4) < 1:
                        player2.boats.append(Boat(player2_boot4, x, 579,4,4, 1000, 430,1))
        for boat in player1.boats:
            screen.blit(boat.image,(boat.p_x,boat.p_y), boat.show_state())
        for boat in player2.boats:
            screen.blit(boat.image,(boat.p_x,boat.p_y),  boat.show_state())
        if len(player1.boats) == 4 and len(player2.boats) == 4:
            if player1.boats[0].turn > 0:
                move_boat((0,80,80),50,700,80,50,player1,0,'Player1Boat1Button.png')
                move_boat((90, 90, 0), 50, 650, 80, 50, player1, 1,'Player1Boat2Button.png' )
                move_boat((50, 100, 0), 50, 600, 80, 50, player1, 2,'Player1Boat3Button.png' )
                move_boat((60, 60, 60), 50, 550, 80, 50, player1, 3, 'Player1Boat4Button.png')
                if player1.boats[0].turn == 0:
                    player2.boats[0].turn = player2.boats[0].moves
            elif player2.boats[0].turn > 0:
                move_boat((0,80,80),1000,700,80,50,player2,0,'Player1Boat1Button.png')
                move_boat((90, 90, 0), 1000, 650, 80, 50, player2, 1, 'Player1Boat2Button.png')
                move_boat((50, 100, 0), 1000, 600, 80, 50, player2, 2, 'Player1Boat3Button.png')
                move_boat((60, 60, 60), 1000, 550, 80, 50, player2, 3, 'Player1Boat4Button.png')
                if player2.boats[0].turn == 0:
                    player1.boats[0].turn = player1.boats[0].moves

        pygame.display.flip()






def move_boat(color,px,py,h,w,player,boat_x, image):
    boot=pygame.draw.rect(screen,color,[px,py, h,w])
    insert_image(image, px, py)
    if boot.collidepoint(pygame.mouse.get_pos()):
        player.boats[boat_x].move()



def see_highscores():
    see_highscores = True
    while see_highscores:
        insert_image('highscore.png', 0, 0)
        insert_image('back_button.png', 1379, 0)
        exit_button = pygame.image.load('back_button.png').get_rect(x=1379, y=0)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and exit_button.collidepoint(pygame.mouse.get_pos()):
                see_highscores= False
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


def pause_loop():
    pause=True
    while pause:
        insert_image('pauses1.png', 0, 0)
        insert_image('pause_scherm.png', 330, 200)
        button((0, 89, 90), 590, 353, 180, 65,'pause3.png',help,events)
        insert_image('pause1.png', 390, 353)
        exit_button= pygame.image.load('pause1.png').get_rect(x=390, y=353)
        insert_image('pause2.png', 800, 353)
        resume_button = pygame.image.load('pause2.png').get_rect(x=800, y=353)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and resume_button.collidepoint(pygame.mouse.get_pos()):
                pause= False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and exit_button.collidepoint(pygame.mouse.get_pos()):
                player1.name= " "
                player2.name = " "
                Game()
            elif event.type == pygame.QUIT:
                pygame.quit()
                quit()

def Game():
    Main_menu=True
    pygame.mixer.music.load('MainMenuTheme.wav')
    pygame.mixer.music.play(-1)
    while Main_menu:
        events = pygame.event.get()
        insert_image('back_button.png', 1379, 0)
        insert_image('MenuBackgound.jpg', 0,0)
        button((0, 89, 90), 650, 300, 200, 70, 'button3.png',intro_game, events)
        button((0, 89, 90), 650, 400, 200, 70, 'button2.png',help, events)
        button((0, 89, 90), 650, 500, 200, 70, 'button1.png',see_highscores,events)
        button((0, 89, 90), 650, 600, 200, 70, 'button4.png',exit, events)
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.display.update()

def settings():
    rules_page1 = pygame.image.load('Gameboard 1.1.png')
    next_button = pygame.image.load('pijl1.png').get_rect(x=1100, y=700)
    exit_button = pygame.image.load('back_button.png').get_rect(x=1379, y=0)
    enter_choose = pygame.image.load('back_button.png').get_rect(x=600, y=700)
    settings = True
    while settings:
        screen.fill((255,255,255))
        screen.blit(rules_page1,(300,10))
        insert_image('back_button.png', 1379, 0)
        insert_image('pijl1.png', 1100, 700)
        insert_image('enter.png', 600, 700)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and exit_button.collidepoint(pygame.mouse.get_pos()):
                settings= False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and enter_choose.collidepoint(pygame.mouse.get_pos()):
                settings= False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and next_button.collidepoint(pygame.mouse.get_pos()):
                settings2()
            elif event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.display.update()

def settings2():
    rules_page1 = pygame.image.load('Gameboard 2.1.png')
    next_button = pygame.image.load('pijl1.png').get_rect(x=1100, y=700)
    exit_button = pygame.image.load('back_button.png').get_rect(x=1379, y=0)
    enter_choose = pygame.image.load('back_button.png').get_rect(x=600, y=700)
    previous_button = pygame.image.load('pijl2.png').get_rect(x=200, y=700)
    settings = True
    while settings:
        screen.fill((255,255,255))
        screen.blit(rules_page1,(300,10))
        insert_image('back_button.png', 1379, 0)
        insert_image('pijl1.png', 1100, 700)
        insert_image('enter.png', 600, 700)
        insert_image('pijl2.png', 200, 700)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and exit_button.collidepoint(pygame.mouse.get_pos()):
                settings= False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and enter_choose.collidepoint(pygame.mouse.get_pos()):
                settings= False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and previous_button.collidepoint(pygame.mouse.get_pos()):
                settings = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and next_button.collidepoint(pygame.mouse.get_pos()):
                settings3()
            elif event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.display.update()

def settings3():
    rules_page1 = pygame.image.load('Gameboard 3.1.png')
    next_button = pygame.image.load('pijl1.png').get_rect(x=1100, y=700)
    exit_button = pygame.image.load('back_button.png').get_rect(x=1379, y=0)
    enter_choose = pygame.image.load('back_button.png').get_rect(x=600, y=700)
    previous_button = pygame.image.load('pijl2.png').get_rect(x=200, y=700)
    settings = True
    while settings:
        screen.fill((255,255,255))
        screen.blit(rules_page1,(300,10))
        insert_image('back_button.png', 1379, 0)
        insert_image('enter.png', 600, 700)
        insert_image('pijl2.png', 200, 700)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and exit_button.collidepoint(pygame.mouse.get_pos()):
                settings = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and enter_choose.collidepoint(pygame.mouse.get_pos()):
                settings = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and previous_button.collidepoint(pygame.mouse.get_pos()):
                settings = False
            elif event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.display.update()

def help():
    rules_page1 = pygame.image.load('rules.png')
    next_button = pygame.image.load('pijl1.png').get_rect(x=1100, y=600)
    exit_button = pygame.image.load('back_button.png').get_rect(x=1379, y=0)
    rules = True
    while rules:
        screen.fill((255,255,255))
        screen.blit(rules_page1,(500,0))
        insert_image('back_button.png', 1379, 0)
        insert_image('pijl1.png', 1100, 600)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and exit_button.collidepoint(pygame.mouse.get_pos()):
                rules= False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and next_button.collidepoint(pygame.mouse.get_pos()):
                rules_page2()
            elif event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.display.update()

def rules_page2():
    rules_pages2 = pygame.image.load('rules1.png')
    previous_button = pygame.image.load('pijl2.png').get_rect(x=200, y=600)
    exit_button = pygame.image.load('back_button.png').get_rect(x=1379, y=0)
    rules = True
    while rules:
        screen.fill((255,255,255))
        screen.blit(rules_pages2, (500, 0))
        insert_image('back_button.png', 1379, 0)
        insert_image('pijl2.png', 200, 600)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and exit_button.collidepoint(pygame.mouse.get_pos()):
                rules= False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and previous_button.collidepoint(pygame.mouse.get_pos()):
                help()
            elif event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.display.update()
