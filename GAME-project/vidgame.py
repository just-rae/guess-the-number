import pygame
import os
pygame.font.init()
pygame.mixer.init()

#unique gameplay is in lines 180 and 185(score display)

WIDTH, HEIGHT = 950, 550
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Screaming spirit")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

BORDER = pygame.draw.rect(WIN, BLACK, (0,250,900,10))

BULLET_HIT_SOUND = pygame.mixer.Sound(os.path.join('assets','gun_shot.mp3'))
BULLET_FIRE_SOUND = pygame.mixer.Sound(os.path.join('assets','bullet_hit.mp3'))

HEALTH_FONT = pygame.font.SysFont('comicsans', 40)
WINNER_FONT = pygame.font.SysFont('comicsans', 100)
SCORE_FONT=pygame.font.SysFont('comicsans', 50)

FPS = 60
VEL = 5
BULLET_VEL = 7
MAX_BULLETS = 5
OBJECT_WIDTH, OBJECT_HEIGHT = 55, 40

p2score=0
p1score=0

p1_HIT = pygame.USEREVENT + 1
p2_HIT = pygame.USEREVENT + 2

p1_IMAGE = pygame.image.load(
    os.path.join('assets', 'pic1.png'))
player1 = pygame.transform.rotate(pygame.transform.scale(
    p1_IMAGE, (OBJECT_WIDTH, OBJECT_HEIGHT)), 180)

p2_IMAGE = pygame.image.load(
    os.path.join('assets', 'pic2.png'))
player2 = pygame.transform.scale(
    p2_IMAGE, (OBJECT_WIDTH, OBJECT_HEIGHT))

background = pygame.transform.scale(pygame.image.load(
    os.path.join('assets', 'background.png')), (WIDTH, HEIGHT))


def draw_window(p2, p1, p2_bullets, p1_bullets, p2_health, p1_health):
    WIN.blit(background, (0, 0))
    pygame.draw.rect(WIN, BLACK, (0,250,900,10))

    p2_health_text = HEALTH_FONT.render(
        "PLayer 2- Energy: " + str(p2_health), 1, WHITE)
    p1_health_text = HEALTH_FONT.render(
        "PLayer 1- Energy: " + str(p1_health), 1, WHITE)
    WIN.blit(p2_health_text, (WIDTH - p2_health_text.get_width() - 10, 10))
    WIN.blit(p1_health_text, (10, 420))

    WIN.blit(player1, (p1.x, p1.y))
    WIN.blit(player2, (p2.x, p2.y))

    for bullet in p2_bullets:
        pygame.draw.rect(WIN, RED, bullet)

    for bullet in p1_bullets:
        pygame.draw.rect(WIN, YELLOW, bullet)

    pygame.display.update()


def yellow_handle_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_d] and yellow.x - VEL > 0:  # LEFT
        yellow.x -= VEL
    if keys_pressed[pygame.K_g] and yellow.x + VEL + yellow.width < WIDTH:  # RIGHT
        yellow.x += VEL
    if keys_pressed[pygame.K_r] and yellow.y - VEL > BORDER.y:  # UP
        yellow.y -= VEL
    if keys_pressed[pygame.K_f] and yellow.y + VEL + yellow.height < HEIGHT - 15:  # DOWN
        yellow.y += VEL


def red_handle_movement(keys_pressed, p2):
    if keys_pressed[pygame.K_LEFT] and p2.x - VEL > 0:  # LEFT
        p2.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and p2.x + VEL + p2.width < WIDTH:  # RIGHT
        p2.x += VEL
    if keys_pressed[pygame.K_UP] and p2.y - VEL > 0:  # UP
        p2.y -= VEL
    if keys_pressed[pygame.K_DOWN] and p2.y + VEL + p2.height < BORDER.y :  # DOWN
        p2.y += VEL


def handle_bullets(p1_bullets, p2_bullets, p1, p2):
    for bullet in p1_bullets:
        bullet.y -= BULLET_VEL
        if p2.colliderect(bullet):
            pygame.event.post(pygame.event.Event(p2_HIT))
            p1_bullets.remove(bullet)
        elif bullet.y < 0 :
            p1_bullets.remove(bullet)

    for bullet in p2_bullets:
        bullet.y += BULLET_VEL
        if p1.colliderect(bullet):
            pygame.event.post(pygame.event.Event(p1_HIT))
            p2_bullets.remove(bullet)
        elif bullet.y > HEIGHT :
            p2_bullets.remove(bullet)


def draw_winner(text):
    draw_text = WINNER_FONT.render(text, 1, WHITE)
    WIN.blit(draw_text, (WIDTH/2 - draw_text.get_width() /
                         2, HEIGHT/2 - draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(5000)

def draw_score(p1score,p2score):
    #this function displays the players scores
    p1score_text = SCORE_FONT.render(
        "Player1 score: " + str(p1score), 1, WHITE)
    p2score_text = SCORE_FONT.render(
        "PLayer2 score: " + str(p2score), 1, WHITE)
    WIN.blit(p1score_text, (WIDTH- p1score_text.get_width(), HEIGHT - p1score_text.get_height()))
    WIN.blit(p2score_text, (WIDTH - p2score_text.get_width(), HEIGHT-100 - p2score_text.get_height()))
                         
def main():
    p2 = pygame.Rect(400, 70, OBJECT_WIDTH, OBJECT_HEIGHT)
    p1 = pygame.Rect(400, 410, OBJECT_WIDTH, OBJECT_HEIGHT)

    p2_bullets = []
    p1_bullets = []

    p2_health = 10
    p1_health = 10

    global p1score
    global p2score

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z and len(p1_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(
                        p1.x + p1.width//2 , p1.y + p1.height//2 , 5, 10)
                    p1_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()

                if event.key == pygame.K_m and len(p2_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(
                        p2.x + p2.width//2 , p2.y + p2.height//2 - 2, 5, 10)
                    p2_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()

            if event.type == p2_HIT:
                p2_health -= 1
                BULLET_HIT_SOUND.play()

            if event.type == p1_HIT:
                p1_health -= 1
                BULLET_HIT_SOUND.play()

        winner_text = ""
        if p2_health <= 0:
            winner_text = "Player 1 won!"
            p1score=p1score+1
            draw_score(p1score,p2score)

        if p1_health <= 0:
            winner_text = "Player 2 Won!"
            p2score=p2score+1
            draw_score(p1score,p2score)
            

        if winner_text != "":
            draw_winner(winner_text)
            break
        

        keys_pressed = pygame.key.get_pressed()
        yellow_handle_movement(keys_pressed, p1)
        red_handle_movement(keys_pressed, p2)

        handle_bullets(p1_bullets, p2_bullets, p1, p2)

        draw_window(p2, p1, p2_bullets, p1_bullets,
                    p2_health, p1_health)
        
    main()


if __name__ == "__main__":
    main()