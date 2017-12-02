# Snake Game !
import pygame, sys, random, time

# Check for initializing errors
check_errors = pygame.init()
if check_errors[1] :
    print ("(!) Had {0} initializing errors, exiting...".format(check_errors[0]))
    exit(-1)
else:
    print ("(+) PyGame Initialized Successfully !")

# Play Surface
playSurfaceDimensions = (720,460)
playSurface = pygame.display.set_mode(playSurfaceDimensions)
pygame.display.set_caption("Snake Game") 

# Color
red = pygame.Color(255, 0, 0) #game over
green = pygame.Color(0, 250, 0) #snake body
black = pygame.Color(0, 0, 0) # score
white = pygame.Color(255, 255, 255) #background
brown = pygame.Color(165, 40, 40) # food

# FBS Controller
fpsController = pygame.time.Clock()

# Important Variables
snakePos = [100, 50]
snakeBody= [[100,50], [90,50], [80,50]]

foodPos = [random.randrange(1,72)*10 , random.randrange(1,46)*10  ]
foodSpawn = True

direction = 'RIGHT'
changeto = direction

score = 0

# Game Over Function
def gameOver():
    myFont = pygame.font.SysFont('monaco', 72)
    GOSurf = myFont.render('Game Over !', True, red)
    GORect = GOSurf.get_rect()
    GORect.midtop = (360, 15)
    playSurface.blit(GOSurf, GORect)
    showScore(isFinal=True)
    pygame.display.flip() 
    time.sleep(3)
    pygame.quit()
    sys.exit()

def showScore(isFinal = 0):
    myFont = pygame.font.SysFont('monaco', 24)
    ScoreSurf = myFont.render('Score : %d'%score, True, black)
    ScoreRect = ScoreSurf.get_rect()
    if isFinal:
        ScoreRect.midtop = (360, 120)  # below the game over message
    else:
        ScoreRect.midtop = (80, 10)
    playSurface.blit(ScoreSurf, ScoreRect) 
# Main Logic Of Game
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                changeto = 'RIGHT' 
            elif event.key == pygame.K_LEFT or event.key == ord('a'):
                changeto = 'LEFT'
            elif event.key == pygame.K_UP or event.key == ord('w'):
                changeto = 'UP'
            elif event.key == pygame.K_DOWN or event.key == ord('s'):
                changeto = 'DOWN'
            elif event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))

    # validate directions
    if changeto == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'
    if changeto == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if changeto == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if changeto == 'DOWN' and direction != 'UP':
        direction = 'DOWN'

    # Update Snake Position
    if direction == 'RIGHT':
        snakePos[0] += 10 
    elif direction == 'LEFT':
        snakePos[0] -= 10
    elif direction == 'UP':
        snakePos[1] -= 10
    elif direction == 'DOWN':
        snakePos[1] += 10
                
    # Snake Body Mechanism
    snakeBody.insert(0, list(snakePos))
    if snakePos[0] == foodPos[0] and snakePos[1] == foodPos[1]:
        score += 1
        foodSpawn = False
    else:
        snakeBody.pop()
    if foodSpawn == False:
        foodPos = [random.randrange(1,72)*10 , random.randrange(1,46)*10  ]
    foodSpawn = True

    # Background
    playSurface.fill(white)
    
    # Draw Snake 
    for pos in snakeBody:  
        pygame.draw.rect(playSurface, green, pygame.Rect(pos[0], pos[1], 10, 10 ))
    # Draw Food
    pygame.draw.rect(playSurface, brown, pygame.Rect(foodPos[0], foodPos[1], 10, 10 ))

    # Boundries
    if snakePos[0] > 710 or snakePos[0] < 0 :
        gameOver()
    if snakePos[1] > 450 or snakePos[1] < 0:
        gameOver()
    for block in snakeBody[1:]:
        if block[0] == snakePos[0] and block[1] == snakePos[1]:
            gameOver()
    # Show Score
    showScore()
    pygame.display.flip()
    fpsController.tick(17)