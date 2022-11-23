import pygame
import random
import time

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Test Game")
bg = pygame.image.load("bg2.jpg")
screen.blit(bg, (0, 50)) #ตั้งให้ห่างจากขอบซ้าย,บน
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
