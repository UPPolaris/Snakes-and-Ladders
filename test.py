import pygame
import random
import time

pygame.init()
screen = pygame.display.set_mode((1000, 600)) #สร้าง&ตั้งค่าขนาดหน้าจอ
pygame.display.set_caption("Test Game")
table = pygame.image.load("table_1.png")
screen.blit(table, (0, 0)) #ตั้งให้ห่างจากขอบซ้าย,บน

dice = pygame.image.load("1diceface.png")
screen.blit(dice, (700, 40))

pygame.display.update()
#movement
#now_po = 1
#dice = random.randint(1,6)
#new_po = now_po + dice


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
