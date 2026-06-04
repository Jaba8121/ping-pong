import pygame
import sys


pygame.init()

#размер игры
widih = 800
height = 600

screen = pygame.display.set_mode((widih, height))
pygame.display.set_caption("Пинг-Понг")

clock = pygame.time.Clock()

#cveta igri
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

#harakterictika racetoc
raket_WIDTH = 15
raket_HEIGHT = 100
raket_SPEED = 7

left = pygame.Rect(
    30,
    250,
    raket_WIDTH,
    raket_HEIGHT
)

right = pygame.Rect(
    750,
    250,
    raket_WIDTH,
    raket_HEIGHT
)

#mya4
BALL_size = 20

ball = pygame.Rect(
    490,
    290,
    BALL_size,
    BALL_size
)

ball_speed_x = 5
ball_speed_y = 5

#scare
left_score = 0
right_score = 0

font = pygame.font.Font(None, 74)


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

#dvijenie
    keys = pygame.key.get_pressed()


    if keys[pygame.K_w] and left.top > 0:
        left.y -= raket_SPEED

    if keys[pygame.K_s] and left.bottom < height:
        left.y += raket_SPEED


    if keys[pygame.K_UP] and right.top > 0:
        right.y -= raket_SPEED

    if keys[pygame.K_DOWN] and right.bottom < height:
        right.y += raket_SPEED

#движение мяча
    ball.x += ball_speed_x
    ball.y += ball_speed_y

#отскок от стен
    if ball.top <= 0 or ball.bottom >= height:
        ball_speed_y *= -1

#отскок от ракеток
    if ball.colliderect(left) or ball.colliderect(right):
        ball_speed_x *= -1

#гол игроку
    if ball.left <= 0:
        right_score += 1
        ball.center = (widih // 2, height // 2)
        ball_speed_x *= -1

        left = pygame.Rect(
        30,
        250,
        raket_WIDTH,
        raket_HEIGHT
        )

        right = pygame.Rect(
        750,
        250,
        raket_WIDTH,
        raket_HEIGHT
        )


    if ball.right >= widih:
        left_score += 1
        ball.center = (widih // 2, height // 2)
        ball_speed_x *= -1

        left = pygame.Rect(
        30,
        250,
        raket_WIDTH,
        raket_HEIGHT
        )

        right = pygame.Rect(
        750,
        250,
        raket_WIDTH,
        raket_HEIGHT
        )

    screen.fill(BLACK)

    pygame.draw.rect(screen, WHITE, left)
    pygame.draw.rect(screen, WHITE, right)
    pygame.draw.ellipse(screen, WHITE, ball)

    pygame.draw.aaline(
        screen,
        WHITE,
        (400, 0),
        (400, 600)
    )

    left_text = font.render(str(left_score), True, WHITE)
    right_text = font.render(str(right_score), True, WHITE)


#рестарт
#    if left_score >= 5 or right_score >= 5:
#        left_score=0
#        right_score=0


    screen.blit(left_text, (200, 20))
    screen.blit(right_text, (600, 20))

    pygame.display.flip()
    clock.tick(60)