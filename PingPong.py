#Import pygame Library 
import pygame
from paddle import Paddle
from ball import Ball


#Function For Displaying Message
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

    
#Initialise The Game
pygame.init()
 

#Colors
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
BLUE = (0,0,255)


#Sounds
ballhitsound = pygame.mixer.Sound("ballhit.wav")
powerballhitsound = pygame.mixer.Sound("powerballhit.wav")


#Game End Score
ENDSCORE = 15

 
#Window Height,Width And Name
dis_width =700
dis_height = 500
size = (dis_width, dis_height)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Ping Pong - By R. T. Ezhil Azhagan")

font_style = pygame.font.SysFont("comicsansms", 25)
dis = pygame.display.set_mode((dis_width, dis_height))


#Paddles
paddleA = Paddle(WHITE, 10, 100)
paddleA.rect.x = 20
paddleA.rect.y = 200
 
paddleB = Paddle(WHITE, 10, 100)
paddleB.rect.x = 670
paddleB.rect.y = 200


#Balls
ball = Ball(WHITE,10,10)
ball.rect.x = 345
ball.rect.y = 195

powerball = Ball(RED,10,10)
powerball.rect.x = 345
powerball.rect.y = 195
 
#List of All Sprites
all_sprites_list = pygame.sprite.Group()
 
all_sprites_list.add(paddleA)
all_sprites_list.add(paddleB)
all_sprites_list.add(ball)
all_sprites_list.add(powerball)

 
#Clock To Control The Speed Of The Game
clock = pygame.time.Clock()


#Initialise player scores
def gameLoop():
    scoreA = 0
    scoreB = 0

#Initial Values
    gameEnd = False
    carryOn = True
    waitForUser = True

    #Main Loop Of The Program
    while not gameEnd:
        while waitForUser == True :
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT:
                      carryOn = False
                      gameEnd = True
                      waitForUser = False
                      print("Game Exited Smoothly")
                elif event.type==pygame.KEYDOWN:
                        if event.key==pygame.K_x: 
                            carryOn=False
                            gameEnd = True
                            waitForUser = False
                            print("User Pressed X To Quit The Game")
                            break
                        if event.key == pygame.K_q:
                            carryOn=False
                            gameEnd = True
                            waitForUser = False
                            print("User Pressed Q To Quit The Game")
                            break
                        if event.key == pygame.K_c:
                            carryOn= True
                            gameEnd = False
                            waitForUser = False
                            print("User Pressed C To Play Again")
                            scoreA = 0
                            scoreB = 0
                            gameLoop()

            if carryOn == True :
            #Paddle Movement
                keys = pygame.key.get_pressed()
                if keys[pygame.K_w]:
                    paddleA.moveUp(5)
                if keys[pygame.K_s]:
                    paddleA.moveDown(5)
                if keys[pygame.K_UP]:
                    paddleB.moveUp(5)
                if keys[pygame.K_DOWN]:
                    paddleB.moveDown(5)    
         
            all_sprites_list.update()
            
            #Checking Ball Bounce Against Walls
            if ball.rect.x>=690:
                if carryOn == True :
                    scoreA+=1
                ball.velocity[0] = -ball.velocity[0]
            if ball.rect.x<=0:
                if carryOn == True :
                    scoreB+=1
                ball.velocity[0] = -ball.velocity[0]
            if ball.rect.y>490:
                ball.velocity[1] = -ball.velocity[1]
            if ball.rect.y<10:
                ball.velocity[1] = -ball.velocity[1]     

            #For Powerball
            if powerball.rect.x>=690:
                powerball.velocity[0] = -powerball.velocity[0]
            if powerball.rect.x<=0:
                powerball.velocity[0] = -powerball.velocity[0]
            if powerball.rect.y>490:
                powerball.velocity[1] = -powerball.velocity[1]
            if powerball.rect.y<10:
                powerball.velocity[1] = -powerball.velocity[1]
         
            #Detecting Collisions
            if pygame.sprite.collide_mask(ball, paddleA) or pygame.sprite.collide_mask(ball, paddleB):
               ball.bounce()
               pygame.mixer.Sound.play(ballhitsound)
               pygame.mixer.music.stop()
            if pygame.sprite.collide_mask(powerball, paddleA) :
               powerball.bounce()
               pygame.mixer.Sound.play(powerballhitsound)
               pygame.mixer.music.stop()
               if carryOn == True :
                   scoreA-=1
            if pygame.sprite.collide_mask(powerball, paddleB):
               powerball.bounce()
               pygame.mixer.Sound.play(powerballhitsound)
               pygame.mixer.music.stop()
               if carryOn == True :
                   scoreB-=1
 
            screen.fill(BLACK)

            #Drawing The Net
            pygame.draw.line(screen, WHITE, [349, 0], [349, 500], 5)
            
            all_sprites_list.draw(screen) 
         
            #Displaying Scores
            font = pygame.font.Font(None, 74)
            text = font.render(str(scoreA), 1, WHITE)
            screen.blit(text, (250,10))
            text = font.render(str(scoreB), 1, WHITE)
            screen.blit(text, (420,10))

            #Ending The Game
            if scoreA >= ENDSCORE :
                text = font.render("A Won the Game", 1, WHITE)
                screen.blit(text, (100,350))
                carryOn = False
                message("Press  C To Play Again  Q-Quit", RED)
                pygame.display.update()
            if scoreB >= ENDSCORE :
                text = font.render("B Won the Game", 1, WHITE)
                screen.blit(text, (200,250))
                carryOn = False
                message("Press  C To Play Again  Q-Quit", RED)
                pygame.display.update()
                
    
            pygame.display.flip()
             
            clock.tick(60)

     
#Exiting The Game
    pygame.quit()
    quit()

gameLoop()


