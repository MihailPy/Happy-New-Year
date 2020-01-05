from PIL import Image
from random import randint, choice
import pyscreenshot as ImGrab
import pygame

pygame.init()

im = ImGrab.grab() 
im.save('faux_trans.png','png')
im = Image.open("faux_trans.png")
(width, height) = im.size

for_trans = pygame.image.load('faux_trans.png')

pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play()
# song = pygame.mixer.('music.mp3')
# song.play()

# fullscreen = pygame.FULLSCREEN
screen = pygame.display.set_mode((width,height), pygame.FULLSCREEN)
clock = pygame.time.Clock()
FPS = 60  # Frames per second.

xi = 50
x = 50
y = 50
pos_gir = []
rgbs = []
color = [(255, 0, 0),(0, 255, 0),(0, 0, 255),(255, 255, 0),(0, 255, 255),(255, 0, 255)]
int1 = 1
for o in range(int(height / 50)):
    for i in range(int(width / 50)):
        pos_gir.append([randint(x-5, x+5), randint(y-5, y+5)])
        if int1 == 1:
            rgbs.append([*choice(color), 0, 7.8125])
            int1 = 2
        elif int1 == 2:
            rgbs.append([*choice(color), 250, -7.8125])
            int1 = 1
        x += xi
    if xi < 0:
        xi = 50
        x = 50
    else:
        xi = -50
        x = 50 * int(width / 50)
    y += 50

screen.blit(for_trans, (0,0))

superx = 0
x = 1
alpha = 1
runGame = True
while runGame:
    if not pygame.mixer.music.get_busy():
        runGame = False
        exit()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            runGame = False
            exit()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_1:
                pygame.mixer.music.pause()
            elif event.key == pygame.K_2:
                pygame.mixer.music.unpause()
    clock.tick(FPS)

    screen.blit(for_trans, (0,0))
    pygame.draw.lines(screen, (0,0,0), False, pos_gir, 2)
    box_surface = pygame.Surface((width,height), pygame.SRCALPHA)
    if i == len(pos_gir)-1:
        x = -1
    elif i == 0:
        x = 1
    superx += x
    # pygame.draw.rect(screen, (255, 255, 255), (20, 20, 500, 275))
    # if upd % 5 == 0:
    for i in range(len(pos_gir)):
        p = pos_gir[i]
        c = rgbs[i]
        if c[-2] + 7.8125 > 250:
            c[-1] = -7.8125
        elif c[-2] - 7.8125 < 0:
            c[-1] = 7.8125
        c[-2] += c[-1]
        pygame.draw.circle(box_surface, (c[0:-1]), (p[0],p[1]), 7)
            # upd = 0

        # rgbs.append(rgbs[0])
        # rgbs.remove(rgbs[0])
    screen.blit(box_surface, (0, 0))
    pygame.display.update()


pygame.quit()
