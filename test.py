import pygame
import random
import time

pygame.init()
screen = pygame.display.set_mode((1000, 600)) #สร้าง&ตั้งค่าขนาดหน้าจอ
pygame.display.set_caption("Test Game")
table = pygame.image.load("table_1.png")
screen.blit(table, (0, 0)) #ตั้งให้ห่างจากขอบซ้าย,บน


dice = pygame.image.load("1diceface.png") #เรียกใช้รูปนี้ได้จากตัวแปรชื่อ dice
xy_dice_img = (700, 40)
reg_for_dice_img = pygame.Rect(700, 40, 200, 200)
screen.blit(dice, xy_dice_img) #เอา dice ไปแสดงที่ จุดห่างจากขอบซ้าย 700, จากขอบบน 40

#สร้างสี่เหลี่ยม (พื้นที่ไว้กดทอยเต๋า)
color = (255,255,255) #กำหนด RGB ของสี
button_diceroll = pygame.Rect(750, 260, 100, 50) #(สีเหลี่ยมที่ตำแหน่ง ห่างขอบซ้าย750 ห่างบน260 กว้าง100 สูง50)
pygame.draw.rect(screen, color, button_diceroll) #วาดสี่เหลี่ยม(วาดบนไหน,สีไร,วาดอะไร)
#สร้าง text
font = pygame.font.Font('freesansbold.ttf', 20)
text = font.render('Roll Dice', True, (0,0,0))
screen.blit(text, (758, 275))
pygame.display.update() #สั่งให้อัพเดทหน้าจอ
#movement
#now_po = 1
#dice = random.randint(1,6)
#new_po = now_po + dice
def diceroll():
    result = random.randint(1,6)
    if result == 1: dice = pygame.image.load("1diceface.png")
    elif result == 2: dice = pygame.image.load("2diceface.png")
    elif result == 3: dice = pygame.image.load("3diceface.png")
    elif result == 4: dice = pygame.image.load("4diceface.png")
    elif result == 5: dice = pygame.image.load("5diceface.png")
    elif result == 6: dice = pygame.image.load("6diceface.png")
    return result, dice #ส่งกลับค่า แต้มที่ออก, รูปลูกเต๋า

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        elif event.type == pygame.MOUSEBUTTONUP:
            mouse_pos = pygame.mouse.get_pos()
            if button_diceroll.collidepoint(mouse_pos):
                for _ in range(12):
                    dice_result, dice_img = diceroll()
                    screen.blit(dice_img, xy_dice_img)
                    pygame.display.update(reg_for_dice_img)
                    time.sleep(0.08)
