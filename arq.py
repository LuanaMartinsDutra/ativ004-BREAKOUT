import pygame

pygame.init()

write = (255, 255, 255)
grey = (212, 210, 212)
black = (0, 0, 0)
blue = (0, 97, 148)
red = (162, 8, 0)
orange = (183, 119, 0)
green = (0, 127, 33)
yellow = (197, 199, 37)

width = 800
height = 600
size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("BREAKOUT")
clock = pygame.time.Clock()

paddle_width = 54
paddle_height = 20

all_sprites_list = pygame.sprite.Group()

class Brick(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()

all_bricks = pygame.sprite.Group()

brick_width = 55
brick_height = 10
x_gap = 4.5
y_gap = 4
wall_width = 16

def bricks():
    for j in range(8):
        for i in range(14):
            if j < 2:
                if i == 0:
                    brick = Brick(red, brick_width, brick_height)
                    brick.rect.x = wall_width
                    brick.rect.y = 100 + j * (y_gap + brick_height)
                    all_sprites_list.add(brick)
                    all_bricks.add(brick)
                else:
                    brick = Brick(red, brick_width, brick_height)
                    brick.rect.x = wall_width + brick_width + x_gap + (i - 1) * (brick_width + x_gap)
                    brick.rect.y = 100 + j * (y_gap + brick_height)
                    all_sprites_list.add(brick)
                    all_bricks.add(brick)
            if 1 < j < 4:
                if i == 0:
                    brick = Brick(orange, brick_width, brick_height)
                    brick.rect.x = wall_width
                    brick.rect.y = 100 + j * (y_gap + brick_height)
                    all_sprites_list.add(brick)
                    all_bricks.add(brick)
                else:
                    brick = Brick(orange, brick_width, brick_height)
                    brick.rect.x = wall_width + brick_width + x_gap + (i - 1) * (brick_width + x_gap)
                    brick.rect.y = 100 + j * (y_gap + brick_height)
                    all_sprites_list.add(brick)
                    all_bricks.add(brick)
            if 3 < j < 6:
                if i == 0:
                    brick = Brick(green, brick_width, brick_height)
                    brick.rect.x = wall_width
                    brick.rect.y = 100 + j * (y_gap + brick_height)
                    all_sprites_list.add(brick)
                    all_bricks.add(brick)
                else:
                    brick = Brick(green, brick_width, brick_height)
                    brick.rect.x = wall_width + brick_width + x_gap + (i - 1) * (brick_width + x_gap)
                    brick.rect.y = 100 + j * (y_gap + brick_height)
                    all_sprites_list.add(brick)
                    all_bricks.add(brick)
            if 5 < j < 8:
                if i == 0:
                    brick = Brick(yellow, brick_width, brick_height)
                    brick.rect.x = wall_width
                    brick.rect.y = 100 + j * (y_gap + brick_height)
                    all_sprites_list.add(brick)
                    all_bricks.add(brick)
                else:
                    brick = Brick(yellow, brick_width, brick_height)
                    brick.rect.x = wall_width + brick_width + x_gap + (i - 1) * (brick_width + x_gap)
                    brick.rect.y = 100 + j * (y_gap + brick_height)
                    all_sprites_list.add(brick)
                    all_bricks.add(brick)

brick_wall = bricks()

def main():
    clock.tick(60)

    carry = True
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                carry = False
        all_sprites_list.update()

        screen.fill(black)

        pygame.draw.line(screen, grey, [0, 10], [width, 10], 30)
        pygame.draw.line(screen, grey, [(wall_width / 2) - 1, 0], [(wall_width / 2) - 1, height], wall_width)
        pygame.draw.line(screen, grey, [(width - wall_width / 2) - 1, 0], [(width - wall_width / 2) - 1, height],
                         wall_width)

        pygame.draw.line(screen, blue, [(wall_width / 2) - 1, height - 65 + paddle_height / 2 - 54 / 2],
                         [(wall_width / 2) - 1, height - 65 + paddle_height / 2 - 54 / 2 + 54], wall_width)
        pygame.draw.line(screen, blue, [(width - wall_width / 2) - 1, height - 65 + paddle_height / 2 - 54 / 2],
                         [(width - wall_width / 2) - 1, height - 65 + paddle_height / 2 - 54 / 2 + 54], wall_width)

        pygame.draw.line(screen, red, [(wall_width / 2) - 1, 100],
                         [(wall_width / 2) - 1, 100 + 2 * brick_height + 2 * y_gap], wall_width)
        pygame.draw.line(screen, red, [(width - wall_width / 2) - 1, 100],
                         [(width - wall_width / 2) - 1, 100 + 2 * brick_height + 2 * y_gap], wall_width)

        pygame.draw.line(screen, orange, [(wall_width / 2) - 1, 100 + 2 * brick_height + 2 * y_gap],
                         [(wall_width / 2) - 1, 100 + 4 * brick_height + 4 * y_gap], wall_width)
        pygame.draw.line(screen, orange, [(width - wall_width / 2) - 1, 100 + 2 * brick_height + 2 * y_gap],
                         [(width - wall_width / 2) - 1, 100 + 4 * brick_height + 4 * y_gap], wall_width)

        pygame.draw.line(screen, green, [(wall_width / 2) - 1, 100 + 4 * brick_height + 4 * y_gap],
                         [(wall_width / 2) - 1, 100 + 6 * brick_height + 6 * y_gap], wall_width)
        pygame.draw.line(screen, green, [(width - wall_width / 2) - 1, 100 + 4 * brick_height + 4 * y_gap],
                         [(width - wall_width / 2) - 1, 100 + 6 * brick_height + 6 * y_gap], wall_width)

        pygame.draw.line(screen, yellow, [(wall_width / 2) - 1, 100 + 6 * brick_height + 6 * y_gap],
                         [(wall_width / 2) - 1, 100 + 8 * brick_height + 8 * y_gap], wall_width)
        pygame.draw.line(screen, yellow, [(width - wall_width / 2) - 1, 100 + 6 * brick_height + 6 * y_gap],
                         [(width - wall_width / 2) - 1, 100 + 8 * brick_height + 8 * y_gap], wall_width)

        all_sprites_list.draw(screen)

        pygame.display.update()

    pygame.quit()

main()

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

