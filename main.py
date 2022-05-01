import pygame, sys, random
from pygame.locals import *
from card import Card
from deck import Deck

pygame.init()
size = width, height = (700, 700)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BG_COLOR = (0, 102, 0)

deck = None
board = pygame.sprite.Group()
selectedcard = pygame.sprite.GroupSingle()


def init():
    global deck
    deck = Deck()
    for i in range(7):
        for j in range(i + 1):
            card = deck.deal()
            card.rect.midtop = (width // 2 - 40 * i + 80 * j, 30 + 30 * i)
            card.flip()
            board.add(card)


def check_sprite_clicked(click_point):
    card_clicked = None
    for card in board:
        if card.rect.collidepoint(click_point):
            card_clicked = card
    if card_clicked is not None:
        hit_list = pygame.sprite.spritecollide(card_clicked,board,False)
        for card in hit_list:
            if card.rect.y > card_clicked.rect.y:
                return
        selectedcard.add(card_clicked)


def main():
    global screen, clock
    init()

    while True:
        clock.tick(60)
        for event in pygame.event.get():

            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_f:
                    screen = pygame.display.set_mode(size, FULLSCREEN)
                if event.key == K_d:
                    screen = pygame.display.set_mode(size)
            if event.type == MOUSEBUTTONDOWN:
                click_point = pygame.mouse.get_pos()
                check_sprite_clicked(click_point)

        screen.fill(BG_COLOR)
        board.draw(screen)
        if len(selectedcard) > 0:
            pygame.draw.rect(screen, (204, 173, 0), selectedcard.sprite.rect, 3)
        pygame.display.flip()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
