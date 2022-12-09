import pygame
import random
import time

#*****งูและบันได ถ้าตกช่องไหน(key)ให้ไปตรงไหน(value)******
ladder={6: 35,
        41: 79,
        57: 65,
        75: 95}

snake ={49: 13,
        67: 46,
        87: 51,
        98: 3}

#*****ตำแหน่งของแต่ละผู้เล่น ตามลำดับ******
player_position = [1, 1, 1, 1]

#*****สีของแต่ละผู้เล่น ตามลำดับ*******
p_color = [(255, 255, 255), (255, 0, 0), (0, 255, 0), (0, 0, 255)]

#---สร้างจุดอ้างอิงของแต่ละช่อง(สร้างไว้ที่มุมซ้ายล่าง)----------------------------------------------------------------------
def set_position_each_block():
    """set position at down-left corner for each block in table"""
    block_position_dict = {}
    countt = 0
    for row in range(10):
        for col in range(10):#:มาร์กจุดจากซ้ายไปขวา พอขึ้นแถวถัดไปขวาไปซ้าย
            countt += 1
            if row%2 == 0:
                block_position_dict[countt] = (col*60, row*60)
            else:
                block_position_dict[countt] = (600-((col+1)*60), row*60)
    return block_position_dict

block_position_dict = set_position_each_block()

def draw_circle():
    """draw player circle"""
    pygame.draw.circle(screen, p_color[0], ((block_position_dict.get(player_position[0])[0] + 10), (600-block_position_dict.get(player_position[0])[1])-50), 10, 20) #player1
    pygame.draw.circle(screen, p_color[1], ((block_position_dict.get(player_position[1])[0] + 50), (600-block_position_dict.get(player_position[1])[1])-50), 10, 20) #player2
    pygame.draw.circle(screen, p_color[2], ((block_position_dict.get(player_position[2])[0] + 10), (600-block_position_dict.get(player_position[2])[1])-10), 10, 20) #player3
    pygame.draw.circle(screen, p_color[3], ((block_position_dict.get(player_position[3])[0] + 50), (600-block_position_dict.get(player_position[3])[1])-10), 10, 20) #player4

#*******************เปิดเกมมาต้องทำไรบ้าง********************************************************************************
#---สร้าง & ตั้งค่าขนาดหน้าจอ-------------------------------------------------
pygame.init()
screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Test Game")

#---วาดภาพตารางลงไปบนจอ-------------------------------------------------
table = pygame.image.load("table_1.png")
screen.blit(table, (0, 0))

#---วาดภาพหน้าลูกเต๋าไปบนจอ-------------------------------------------------
dice = pygame.image.load("1diceface.png") #เรียกใช้รูปนี้ได้จากตัวแปรชื่อ dice
xy_dice_img = (700, 40)
reg_for_dice_img = pygame.Rect(700, 40, 200, 200)
screen.blit(dice, xy_dice_img) #เอา dice ไปแสดงที่ จุดห่างจากขอบซ้าย 700, จากขอบบน 40

#---วาดปุ่มทอยเต๋าลงไปบนจอ-------------------------------------------------
#phase 1 สร้างสี่เหลี่ยมมาเป็น bg ปุ่ม
color = (255,255,255) #กำหนด RGB ของสี
button_diceroll = pygame.Rect(750, 260, 100, 50) #(สีเหลี่ยมที่ตำแหน่ง ห่างขอบซ้าย750 ห่างบน260 กว้าง100 สูง50) (ประมาณว่าคุณลักษณะสี่เหลี่ยม)
pygame.draw.rect(screen, color, button_diceroll) #วาดสี่เหลี่ยม (วาดบนไหน ,สี ,คุณลักษณะสี่เหลี่ยม)
#phase 2 สร้างตัวหนังสือมาวางทับ
font = pygame.font.Font('freesansbold.ttf', 20) #กำหนด font และขนาด ใส่ไปในตัวแปร
text = font.render('Roll Dice', True, (0,0,0)) #สร้าง text แล้วเอาไปใส่ในตัวแปรชื่อ text
screen.blit(text, (758, 275)) #เขียน text ลงบนจอ

#---วาด player ทั้ง 4 (วงกลม)-------------------------------------------------
draw_circle()

#---แสดงตาของผู้เล่นคนแรก-------------------------------------------------
turn_font = pygame.font.Font('freesansbold.ttf', 40)
trun_text = turn_font.render("Player 1 Turn", True, p_color[0], (0,0,0))
screen.blit(trun_text, (620, 480))

#************สั่งให้อัพเดทหน้าจอ****************
pygame.display.update() #สั่งให้อัพเดทหน้าจอ เอาไว้ใช้ตอนเปลี่ยนภาพ (เจาะจงพื้นที่ได้)
#------------------------------------------------------------------------------------------------------------------

log_font = pygame.font.Font('freesansbold.ttf', 18)

def diceroll():
    result = random.randint(1,6)
    if result == 1: dice = pygame.image.load("1diceface.png")
    elif result == 2: dice = pygame.image.load("2diceface.png")
    elif result == 3: dice = pygame.image.load("3diceface.png")
    elif result == 4: dice = pygame.image.load("4diceface.png")
    elif result == 5: dice = pygame.image.load("5diceface.png")
    elif result == 6: dice = pygame.image.load("6diceface.png")
    return result, dice #ส่งกลับค่า แต้มที่ออก, รูปลูกเต๋า

def playing_func():
    """func to operate game"""
    player_order = 0 # 0คือp1 1คือp2
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.MOUSEBUTTONUP:
                mouse_pos = pygame.mouse.get_pos()
                if button_diceroll.collidepoint(mouse_pos):
                    pygame.draw.rect(screen, (0,0,0), pygame.Rect(600, 340, 400, 130))#เอาไว้ปิดตัวหนังสือ log
                    for _ in range(6):
                        dice_result, dice_img = diceroll()
                        screen.blit(dice_img, xy_dice_img)
                        pygame.display.update(reg_for_dice_img)
                        time.sleep(0.08)
                    if player_position[player_order] + dice_result <= 100:
                        player_position[player_order] += dice_result
                        #print("player %d got %d point"%(player_order+1, dice_result))
                        log_text = log_font.render("Player %d got %d point"%(player_order+1, dice_result), True, p_color[player_order], (0,0,0))
                        screen.blit(log_text, (620, 400))
                        log_text = log_font.render("Player %d move to %d  "%(player_order+1, player_position[player_order]), True, p_color[player_order], (0,0,0))
                        screen.blit(log_text, (620, 420))
                        if player_position[player_order] in snake:
                            log_text = log_font.render("Oh no Player %d falling from %d to %d"%(player_order+1, player_position[player_order], snake.get(player_position[player_order])), True, p_color[player_order], (0,0,0))
                            screen.blit(log_text, (620, 440))
                            player_position[player_order] = snake.get(player_position[player_order])
                        elif player_position[player_order] in ladder:
                            log_text = log_font.render("Oh yeah Player %d climbing from %d to %d"%(player_order+1, player_position[player_order], ladder.get(player_position[player_order])), True, p_color[player_order], (0,0,0))
                            screen.blit(log_text, (620, 440))
                            player_position[player_order] = ladder.get(player_position[player_order])
                    else:
                        log_text = log_font.render("player %d must roll %d point to win"%(player_order+1, 100-(player_position[player_order])), True, p_color[player_order], (0,0,0))
                        screen.blit(log_text, (620, 420))
                        #print("player %d must roll %d point to win"%(player_order+1, 100-(player_position[player_order])))
                    screen.blit(table, (0, 0))
                    draw_circle()
                    pygame.display.update()
                    if player_position[player_order] == 100:
                        winner = player_order+1
                        end_game(winner)
                    player_order += 1
                    if player_order > 3:
                        player_order = 0
                    trun_text = turn_font.render("Player %d Turn"%(player_order+1), True, p_color[player_order], (0,0,0))
                    screen.blit(trun_text, (620, 480))
                    pygame.display.update()
def end_game(winner):
    """work when game end (some player win)"""
    #---สร้างcover (ฉากพื้นหลังบางๆ)----------------------------------------------------------------------
    scene_cover = pygame.Surface((1000, 600))
    scene_cover.set_alpha(200)
    scene_cover.fill((255, 255, 255))
    screen.blit(scene_cover, (0, 0))
    #---สร้างตัวหนังสือของผู้ชนะ----------------------------------------------------------------------
    win_font = pygame.font.Font('freesansbold.ttf', 80)
    win_text = win_font.render("Player %d Win"%winner, True, (0,0,0))
    screen.blit(win_text, (250, 260))
    #---อัพเดทหน้าจอ-------
    pygame.display.update()
    #---ใส่ลูปไม่ให้เกมออกเอง----------------------------------------------------------------------
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

playing_func()