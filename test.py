import pygame
import random
import time

ladder={6: 35,
        41: 97,
        57: 65,
        75: 95}

snake ={49: 13,
        67: 46,
        87: 51,
        98: 3}

player_position = [1, 1, 1, 1] 

def set_position_each_block():
    """position at down-left corner for each block in table"""
    block_position_dict = {}
    countt = 0
    for row in range(10):
        for col in range(10):#:ซ้ายไปขวา พอขึ้นแถวถัดไปขวาไปซ้าย
            countt += 1
            if row%2 == 0:
                block_position_dict[countt] = (col*60, row*60)
            else:
                block_position_dict[countt] = (600-((col+1)*60), row*60)
    print(block_position_dict)
    return block_position_dict

block_position_dict = set_position_each_block()

def draw_circle():
    """draw player circle"""
    pygame.draw.circle(screen, color, ((block_position_dict.get(player_position[0])[0] + 10), (600-block_position_dict.get(player_position[0])[1])-50), 10, 20) #player1

#เปิดเกมมาต้องทำไรบ้าง---------------------------------------------------------------------------------------------------
pygame.init()
screen = pygame.display.set_mode((1000, 600)) #สร้าง&ตั้งค่าขนาดหน้าจอ
pygame.display.set_caption("Test Game")

table = pygame.image.load("table_1.png")
screen.blit(table, (0, 0)) #ตั้งให้ห่างจากขอบซ้าย,บน

#รูปลูกเต๋า
dice = pygame.image.load("1diceface.png") #เรียกใช้รูปนี้ได้จากตัวแปรชื่อ dice
xy_dice_img = (700, 40)
reg_for_dice_img = pygame.Rect(700, 40, 200, 200)
screen.blit(dice, xy_dice_img) #เอา dice ไปแสดงที่ จุดห่างจากขอบซ้าย 700, จากขอบบน 40

#ปุ่มทอยเต๋า (พื้นที่ไว้กดทอยเต๋า)
color = (255,255,255) #กำหนด RGB ของสี
button_diceroll = pygame.Rect(750, 260, 100, 50) #(สีเหลี่ยมที่ตำแหน่ง ห่างขอบซ้าย750 ห่างบน260 กว้าง100 สูง50)
pygame.draw.rect(screen, color, button_diceroll) #วาดสี่เหลี่ยม(วาดบนไหน,สีไร,สี่เหลี่ยมไหน)
font = pygame.font.Font('freesansbold.ttf', 20) #font
text = font.render('Roll Dice', True, (0,0,0))
screen.blit(text, (758, 275))

#ตัว player
draw_circle()

pygame.display.update() #สั่งให้อัพเดทหน้าจอ เอาไว้ใช้ตอนเปลี่ยนภาพ (เจาะจงพื้นที่ได้)
#------------------------------------------------------------------------------------------------------------------


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
                #ทดสอบ
                player_position[0] += dice_result
                screen.blit(table, (0, 0))
                draw_circle()
                pygame.display.update()
                
