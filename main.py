
import random
import sys
import pygame
import time
#pygame.init()
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 500
BLACK = (51, 51, 51)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 23)
RED = [255, 0, 0]
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
def score_borad(passed):
    font = pygame.font.Font(None, 24)
    text = font.render(("passed : " + str(passed)), True, RED)
    SCREEN.blit(text, (8, 150))
def crash():
    global SCREEN, SCREEN_WIDTH, SCREEN_HEIGHT
    font = pygame.font.Font(None, 80)
    text = font.render('Game Over', True, RED)
    text_width = text.get_width()
    text_height = text.get_height()
    x = int(SCREEN_WIDTH / 2 - text_width / 2)
    y = int(SCREEN_HEIGHT / 2 - text_height / 2)
    SCREEN.blit(text, (x, y))
    pygame.display.update()
    time.sleep(2)
    main()
def main():
    global SCREEN_WIDTH, SCREEN_HEIGHT
    pygame.init()
    player = pygame.image.load("./img/Player.png")
    player = pygame.transform.scale(player, (65, 90))
    player_rect = player.get_rect()
    player_rect.centerx = round(SCREEN_WIDTH / 2)
    player_rect.y = 310
    car1 = pygame.image.load("./img/Car04.png")
    car1 = pygame.transform.scale(car1, (65, 90))
    car1_rect = car1.get_rect()
    car1_rect.x = random.choice([125, 215])
    car1_rect.y = 0 - car1_rect.height
    SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("2126066_채문호")
    sound = pygame.mixer.Sound("./sound/b.mp3")
    sound_crash = pygame.mixer.Sound("./sound/crash.ogg")
    sound.play(-1)
    clock = pygame.time.Clock()
    dx = 0
    dy = 0
    dspeed = 25
    cspeed = 5
    score = 0
    playing = True
    counter = 0
    r1 = 0 * 70
    r5 = 4 * 70
    r8 = 7 * 70
    while playing:
        counter += 1
        #print(counter)
        if counter == 450:
            print("counter : ", counter)
            cspeed += 1
            if cspeed >= 18:
                cspeed = 18
            print("cspeed : ", cspeed)
            counter = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    dx = -dspeed
                if event.key == pygame.K_RIGHT:
                    dx = +dspeed
                if event.key == pygame.K_UP:
                    pass
                if event.key == pygame.K_DOWN:
                    pass
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    dx = 0
                if event.key == pygame.K_RIGHT:
                    dx = 0
                if event.key == pygame.K_UP:
                    pass

                if event.key == pygame.K_DOWN:
                    pass
        SCREEN.fill(BLACK)

        pygame.draw.rect(SCREEN, YELLOW, [100, r1, 20, 160])
        pygame.draw.rect(SCREEN, BLACK, [100, r1, 20, 160], 2)
        pygame.draw.rect(SCREEN, YELLOW, [SCREEN_WIDTH - 120, r1, 20, 160])
        pygame.draw.rect(SCREEN, BLACK, [SCREEN_WIDTH - 120, r1, 20, 160], 2)

        pygame.draw.rect(SCREEN, YELLOW, [100, r5, 20, 160])
        pygame.draw.rect(SCREEN, BLACK, [100, r5, 20, 160], 2)
        pygame.draw.rect(SCREEN, YELLOW, [SCREEN_WIDTH - 120, r5, 20, 160])
        pygame.draw.rect(SCREEN, BLACK, [SCREEN_WIDTH - 120, r5, 20, 160], 2)

        pygame.draw.rect(SCREEN, YELLOW, [100, r8, 20, 160])
        pygame.draw.rect(SCREEN, BLACK, [100, r8, 20, 160], 2)
        pygame.draw.rect(SCREEN, YELLOW, [SCREEN_WIDTH - 120, r8, 20, 160])
        pygame.draw.rect(SCREEN, BLACK, [SCREEN_WIDTH - 120, r8, 20, 160], 2)

        r1 += cspeed
        r5 += cspeed
        r8 += cspeed
        if r1 > 500:
            r1 = -200
        if r5 > 500:
            r5 = -200
        if r8 > 500:
            r8 = -200

        myFont = pygame.font.SysFont("corbel", 20, True, YELLOW)
        text = myFont.render("Racing Game", True, YELLOW)
        text_rect = text.get_rect()
        text_rect.centerx = round(SCREEN_WIDTH / 2)
        text_rect.y = 20
        SCREEN.blit(text, text_rect)
        player_rect.x += dx
        player_rect.y += dy
        if player_rect.left < 125:
            player_rect.left = 125
        if player_rect.right > 275:
            player_rect.right = 275
        if player_rect.top < 0:
            player_rect.top = 0
        car1_rect.y += cspeed
        if car1_rect.y > SCREEN_HEIGHT:
            score += 1
            car1_rect.y = 0 - 90
            if random.randint(0, 1) == 0:
                car1_rect.x = 125
            else:
                car1_rect.x = 215
        score_borad(score)
        if (car1_rect.top < player_rect.bottom) and (player_rect.top < car1_rect.bottom) and (car1_rect.left < player_rect.right) and (player_rect.left < car1_rect.right):
            sound.stop()
            sound_crash.play()
            crash()
        SCREEN.blit(car1, car1_rect)
        SCREEN.blit(player, player_rect)
        pygame.display.flip()
        clock.tick(60)
if __name__ == "__main__":
    main()