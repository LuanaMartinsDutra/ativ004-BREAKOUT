#comecar
import pygame

pygame.init()

COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
size = (650, 720)
height = 20
width = 160
x = 250
y = 650
vel = 0.5

screen = pygame.display.set_mode(size)
pygame.display.set_caption("MyPong - PyGame Edition - 2021.01.30")
screen.fill(COLOR_BLACK)
font = pygame.font.Font('PressStart2P.ttf', 44)

# making the bricks
Brick = pygame.draw.rect(screen, COLOR_WHITE, [0, 0, 10, 5])

bricks = []
for i in range(100, 375, 25):
    lista_int = []
    for j in range(8):
        lista_int.append(Brick)
    bricks.append(lista_int)

# paddle
paddle = pygame.draw.rect(screen, COLOR_WHITE, [x, y, width, height])

# ball
ball = pygame.draw.rect(screen, COLOR_WHITE, [300, 500, 20, 20])
ball_x = 300
ball_y = 500
ball_dx = 0.2
ball_dy = 0.2

pygame.display.flip()
game_clock = pygame.time.Clock()
game_loop = True

while game_loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            game_loop = False
    ball = pygame.draw.ellipse(screen, COLOR_WHITE, [ball_x, ball_y, 20, 20])

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > 0:
        x -= vel

    if keys[pygame.K_RIGHT] and x < 650 - width:
        x += vel
    screen.fill((0, 0, 0))
    Brick = pygame.draw.rect(screen, COLOR_WHITE, [0, 0, 10, 5])
    ball = pygame.draw.ellipse(screen, COLOR_WHITE, [ball_x, ball_y, 20, 20])

    # ball movement
    ball_x = ball_x + ball_dx
    ball_y = ball_y + ball_dy
    if ball_x > 635:
        ball_dx *= -1
    elif ball_x <= 0:
        ball_dx *= -1

    if ball_y > 720:
        ball_dy *= -1
    elif ball_y <= 0:
        ball_dy *= -1

    paddle = pygame.draw.rect(screen, COLOR_WHITE, [x, y, width, height])
    Brick = pygame.draw.rect(screen, COLOR_WHITE, [0, 0, 20, 10])

    # collision with the paddle
    if paddle.collidepoint(ball_x, ball_y + 10):
        ball_dy *= -1

    pygame.display.update()
    game_clock.tick()
    pygame.display.flip()
