
import pygame
import os
import random

pygame.init()
mWidth, mHeight = pygame.display.Info().current_w, pygame.display.Info().current_h
mHeight = mHeight = + 960
GUI = pygame.display.set_mode((1000, mHeight), pygame.RESIZABLE)  # window
pygame.display.set_caption("Window Run")
programIcon = pygame.image.load(os.path.join("pygame", "gfx", "icon.png"))
levelint = 1
level = str(levelint)

pygame.display.set_icon(programIcon)

# define fonts

font = pygame.font.SysFont("rifficfreemedium", 60)

# define colours
white = 255, 255, 255
grey = 110, 110, 110
colour = grey


def draw_text(text, font, colour, x, y):
    img = font.render(level, True, colour)
    GUI.blit(img, (x, y))


def update(self):
    self.surface.fill(self.bg)
    self.txt_surf = self.font.render(self.txt, True, self.fg)
    self.surface.blit(self.txt_surf, self.txt_rect)


x, y = GUI.get_size()
width = 32
length = 32
run = True
isJump = False
y_gravity = 0.5
jump_height = 15
EnemyRectX = x - 40


y_velocity = jump_height
topRectL = random.randint(1, y - 60)
bottomRectL = random.randint(topRectL + 32, topRectL + 100)
topRectL = random.randint(bottomRectL - 100, bottomRectL - 32)
moveEnemy = False


while run:
    x, y = GUI.get_size()
    level = str(levelint)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                isJump = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                x -= 30

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                x += 30
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                x = 284
                y = 500
                isJump = False

    if isJump == True:
        y -= y_velocity
        y_velocity -= y_gravity
        if y_velocity < -jump_height:
            y_velocity = jump_height
            isJump = False

        if event.type == pygame.QUIT:
            run = False

    topRectY = 1

    if EnemyRectX == x - 40:
        bottomRectY = y - 32

    if EnemyRectX < 1:
        topRectL = random.randint(1, y - 60)
        bottomRectL = random.randint(topRectL + 32, y)
        EnemyRectX = x - 40
        bottomRectY = y - 32
        levelint + 1
        level = str(levelint)
        
        

    GUI.fill(white)
    pygame.draw.rect(GUI, (255, 210, 0), (x/2, y - 32, width, length))
    pygame.draw.rect(GUI, (255, 3, 3), (EnemyRectX, topRectY, width, topRectL))
    pygame.draw.rect(GUI, (255, 3, 3), (EnemyRectX,
                     bottomRectY, width, bottomRectL))
    
    draw_text(level, font, colour, (x / 2), (y / 2))
    
    pygame.display.update()
    EnemyRectX -= 1



pygame.quit()
