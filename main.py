import pygame,sys,random
from pygame.locals import *
from card import Card
from deck import Deck

pygame.init()
size = width,height = (700,700)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
BG_COLOR = (0,102,0)

deck = None
board = pygame.sprite.Group()
def init():
    global deck
    deck = Deck()

def main():
    global screen,clock
    init()

    while True:
        clock.tick(60)
        for event in pygame.event.get():

            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_f:
                    screen = pygame.display.set_mode(size,FULLSCREEN)
                if event.key == K_d:
                    screen = pygame.display.set_mode(size)
            if event.type == MOUSEBUTTONDOWN:
                click_point = pygame.mouse.get_pos()

        screen.fill(BG_COLOR)

        pygame.display.flip()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

