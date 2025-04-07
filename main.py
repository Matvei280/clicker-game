import time

import pygame
from random import randint
from time import sleep
BACK = (200, 255, 255)  # Light blue background
YELLOW = (255,255,0)
pygame.init()
DARK_BLUE = (0,0,100)
BLUE = (80,80,255)
RED = (255,0,0)
GREEN = (0,255,51)
mw = pygame.display.set_mode((500, 500))
mw.fill(BACK)

clock = pygame.time.Clock()

class Area():
    def __init__(self, x=0, y=0, width=10, height=10, color=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = color
    def set_color(self, new_color):
        self.fill_color = new_color
    def collidepoint(self,x,y):
        return self.rect.collidepoint(x,y)

    def fill(self):
        pygame.draw.rect(mw, self.fill_color, self.rect)

    def outline(self, frame_color, thickness):
        pygame.draw.rect(mw, frame_color, self.rect, thickness)

class Label(Area):
    def settext(self,text,fsisze = 12,textColor = (0,0,0)):
        self.image = pygame.font.SysFont('verdana',fsisze).render(text,True,textColor)
    def draw(self,schiftx = 0,schifty = 0):
        self.fill()
        mw.blit(self.image,(self.rect.x + schiftx,self.rect.y + schifty))


















cards = []
num_cards = 4
x = 70








for i in range(num_cards):
   new_card = Label(x, 170, 70, 100, YELLOW)
   new_card.outline(BLUE, 10)
   new_card.settext('CLICK', 18)
   cards.append(new_card)
   x = x + 100




start_time = time.time()
cur_time = start_time
time_text = Label(0,0,50,50,BACK)
time_text.settext('time:',25,DARK_BLUE)
time_text.draw(20,20)


time_num = Label(50,55,50,50,BACK)
time_num.settext('0',25,DARK_BLUE)
time_num.draw(0,0)



points = 0


score_text = Label(380,0,50,50,BACK)
score_text.settext('score:',25,DARK_BLUE)
score_text.draw(20,20)


score_num = Label(430,55,50,50,BACK)
score_num.settext('0',25,DARK_BLUE)
score_num.draw(0,0)






running = True
wait = 0
while running:

    if wait == 0:
        wait = 25
        click = randint(1,num_cards)
        for i in range(num_cards):
            cards[i].set_color(YELLOW)
            if click == (i+1):
                cards[i].draw(10,40)
            else:
                cards[i].fill()

    else:
        wait -= 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x,y = event.pos
            for i in range(num_cards):
                if cards[i].collidepoint(x, y):
                    if i + 1 == click:
                        cards[i].set_color(GREEN)
                        points = points +1
                    else:
                        cards[i].set_color(RED)
                        points = points -1
                    cards[i].fill()
                    score_num.settext(str(points),25,DARK_BLUE)
                    score_num.draw(0,0)
    new_time = time.time()
    if new_time -start_time >= 11:
        timeover = Label(0,0,500,500,RED)
        timeover.settext('TIME OVER',60,BLUE)
        timeover.draw(110,180)

    if int(new_time) - int(cur_time) == 1:
        time_num.settext(str(int(new_time - start_time)),25,DARK_BLUE)
        time_num.draw(0,0)
        cur_time = new_time
    if points >= 5 :
        timeover = Label(0,0,500,500,GREEN)
        timeover.settext('you win !!!!',60,BLUE)
        timeover.draw(110,180)


    pygame.display.update()

    clock.tick(40)

pygame.quit()
