import pygame

pygame.init()
pygame.mixer.init()

white = (255, 255, 255)
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
text_font = pygame.font.Font("PressStart2P.ttf", 30)
t2xt_font = pygame.font.Font("PressStart2P.ttf", 40)
clock = pygame.time.Clock()

score = 0
balls = 1
velocity = 4

paddle_width = 54
paddle_height = 20

score_surface = text_font.render("000", True, white)
texto_surface = text_font.render("1", True, white)
ttext_surface = text_font.render("000", True, white)
balls_surface = text_font.render("1", True, white)
score_text = text_font.render('00 x 00', True, white)
game_over_text = t2xt_font.render("GAME OVER", True, white)

all_sprites_list = pygame.sprite.Group()

brick_sound = pygame.mixer.Sound('brick.wav')
paddle_sound = pygame.mixer.Sound('paddle.wav')
wall = pygame.mixer.Sound('ball.wav')


class Brick(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()


class Paddle(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()

    def move_right(self, pixels):
        self.rect.x += pixels
        if self.rect.x > width - wall_width - paddle_width:
            self.rect.x = width - wall_width - paddle_width

    def move_left(self, pixels):
        self.rect.x -= pixels
        if self.rect.x < wall_width:
            self.rect.x = wall_width


class Ball(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()
        self.velocity = [velocity, velocity]

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def bounce(self):
        self.velocity[0] = self.velocity[0]
        self.velocity[1] = -self.velocity[1]


paddle = Paddle(blue, paddle_width, paddle_height)
paddle.rect.x = width // 2 - paddle_width // 2
paddle.rect.y = height - 65

ball = Ball(white, 10, 10)
ball.rect.x = width // 2 - 5
ball.rect.y = height // 2 - 5

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


bricks()

all_sprites_list.add(paddle)
all_sprites_list.add(ball)


def main(score, balls):
    step = 0
    game_active = True
    carry = True
    while carry:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                carry = False

        if game_active:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                paddle.move_left(10)
            if keys[pygame.K_RIGHT]:
                paddle.move_right(10)

            all_sprites_list.update()

            if ball.rect.y < 40:
                ball.velocity[1] = -ball.velocity[1]

            if ball.rect.x >= width - wall_width - 10:
                ball.velocity[0] = -ball.velocity[0]

            if ball.rect.x <= wall_width:
                ball.velocity[0] = -ball.velocity[0]

            if ball.rect.y > height:
                ball.rect.x = width // 2 - 5
                ball.rect.y = height // 2 - 5
                ball.velocity[1] = ball.velocity[1]
                balls += 1

            if pygame.sprite.collide_mask(paddle, ball):
                ball.rect.x += ball.velocity[0]
                ball.rect.y -= ball.velocity[1]
                ball.bounce()
                paddle_sound.play()

        brick_collision_list = pygame.sprite.spritecollide(ball, all_bricks, False)
        for brick in brick_collision_list:
            ball.bounce()
            brick_sound.play()
            if len(brick_collision_list) > 0:
                step += 1
                score += 1
                for i in range(0, 448, 28):
                    if step == i:
                        ball.velocity[0] += 1
                        ball.velocity[1] += 1

            brick.kill()

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

        score_surface = text_font.render(str(score), True, white)
        balls_surface = text_font.render(str(balls), True, white)
        screen.blit(score_surface, (100, 45))
        screen.blit(texto_surface, (20, 30))
        screen.blit(ttext_surface, (500, 45))
        screen.blit(balls_surface, (415, 30))

        if balls == 4:
            game_active = False
            screen.blit(game_over_text, (200, 300))

        all_sprites_list.draw(screen)

        pygame.display.update()

        clock.tick(60)

    pygame.quit()


main(score, balls)
