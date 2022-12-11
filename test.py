import pygame
import random
import time

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

def draw_circle():
    """draw player circle"""
    pygame.draw.circle(screen, p_color[0], ((block_position_dict.get(player_position[0])[0] + 10), (600-block_position_dict.get(player_position[0])[1])-50), 10, 20) #player1
    pygame.draw.circle(screen, p_color[1], ((block_position_dict.get(player_position[1])[0] + 50), (600-block_position_dict.get(player_position[1])[1])-50), 10, 20) #player2
    pygame.draw.circle(screen, p_color[2], ((block_position_dict.get(player_position[2])[0] + 10), (600-block_position_dict.get(player_position[2])[1])-10), 10, 20) #player3
    pygame.draw.circle(screen, p_color[3], ((block_position_dict.get(player_position[3])[0] + 50), (600-block_position_dict.get(player_position[3])[1])-10), 10, 20) #player4

def diceroll():
    """สุ่มผลลูกเต๋าแล้วส่งค่ากลับ"""
    result = random.randint(0,5)
    return result+1, dice_img_list[result] #ส่งกลับค่า แต้มที่ออก, รูปลูกเต๋า

def playing_func():
    """func to operate main game scene"""
    player_order = 0 # 0==p1, 1==p2, 2==p3, 3==p4
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.MOUSEBUTTONUP:
                mouse_pos = pygame.mouse.get_pos()
                if button_diceroll_area.collidepoint(mouse_pos):
                    pygame.draw.rect(screen, (0,0,0), pygame.Rect(600, 340, 400, 130)) #เอาไว้ปิดตัวหนังสือ log
                    #---สุ่มเต๋า 6 ครั้ง---------------------------------------
                    for _ in range(6):
                        dice_result, dice_img = diceroll()
                        screen.blit(dice_img, dice_img_position)
                        pygame.display.update(dice_img_area)
                        time.sleep(0.08)

                    #---ถ้าแต้มปัจจุบัน+ที่ได้เพิ่ม ยังไม่เกิน 100---------------------------------------
                    if player_position[player_order] + dice_result <= 100: 
                        player_position[player_order] += dice_result #เพิ่มแต้มผู้เล่นคนนั้น
                        #---แสดงข้อความ: ได้กี่แต้ม---------------------------------------
                        log_text = log_font.render("Player %d got %d point"%(player_order+1, dice_result), True, p_color[player_order], (0,0,0))
                        screen.blit(log_text, (620, 400))
                        #---แสดงข้อความ: เดินไปไหน---------------------------------------
                        log_text = log_font.render("Player %d move to %d  "%(player_order+1, player_position[player_order]), True, p_color[player_order], (0,0,0))
                        screen.blit(log_text, (620, 420))
                        #---เช็คว่าเหยียบงูหรือบันไดมั้ย---------------------------------------
                        check_ladder_and_snake(player_order)

                    #---ถ้าแต้มจะเกิน 100 หรืออื่นๆ---------------------------------------
                    else:
                        #---แสดงข้อความ: ต้องทอยให้ได้กี่แต้ม------------------------------------
                        log_text = log_font.render("player %d must roll %d point to win"%(player_order+1, 100-(player_position[player_order])), True, p_color[player_order], (0,0,0))
                        screen.blit(log_text, (620, 420))

                    #---วาดรูปตารางทับที่เดิม------------------------------------
                    screen.blit(table, (0, 0))
                    #---วาดรูปวงกลมผู้เล่นทับตาราง------------------------------------
                    draw_circle()

                    pygame.display.update()

                    #---ถ้าคนปัจจุบันชนะ------------------------------------
                    if player_position[player_order] == 100:
                        winner = player_order+1
                        end_game(winner)

                    player_order += 1

                #---เตรียมพร้อมสำหรับครั้งถัดไป------------------------------------
                    if player_order > 3:
                        player_order = 0
                    trun_text = turn_font.render("Player %d Turn"%(player_order+1), True, p_color[player_order], (0,0,0))
                    screen.blit(trun_text, (620, 480))
                    pygame.display.update()

def check_ladder_and_snake(player_order):
    """move player that step on snake or ladder"""
    if player_position[player_order] in snake:
        #---แสดงข้อความ: ไหลลงจากหัวงู---------------------
        log_text = log_font.render("Oh no Player %d falling from %d to %d"%(player_order+1, player_position[player_order], snake.get(player_position[player_order])), True, p_color[player_order], (0,0,0))
        screen.blit(log_text, (620, 440))
        #---เปลี่ยนตำแหน่งผู้เล่น---------------------
        player_position[player_order] = snake.get(player_position[player_order])

    elif player_position[player_order] in ladder:
        log_text = log_font.render("Oh yeah Player %d climbing from %d to %d"%(player_order+1, player_position[player_order], ladder.get(player_position[player_order])), True, p_color[player_order], (0,0,0))
        screen.blit(log_text, (620, 440))
        player_position[player_order] = ladder.get(player_position[player_order])

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

def main_game_ui():
    """create UI for main game screen"""
    #---ถมดำก่อน-------------------------------------------------
    pygame.draw.rect(screen, (0,0,0), (0,0,1000,600))
    #---วาดภาพตารางลงไปบนจอ-------------------------------------------------
    screen.blit(table, (0, 0))
    #---วาดภาพหน้าลูกเต๋าไปบนจอ-------------------------------------------------
    screen.blit(dice_img_list[0], dice_img_position) #เอา diceimg ไปแสดงที่ จุดห่างจากขอบซ้าย 700, จากขอบบน 40
    #---วาด player ทั้ง 4 (วงกลม)-------------------------------------------------
    draw_circle()
    #---วาดปุ่มทอยเต๋าลงไปบนจอ-------------------------------------------------
    #phase 1 สร้างสี่เหลี่ยมมาเป็น bg ปุ่ม
    pygame.draw.rect(screen, (255,255,255), button_diceroll_area) #วาดสี่เหลี่ยม (วาดบนไหน ,สี ,คุณลักษณะสี่เหลี่ยม)
    #phase 2 สร้างตัวหนังสือมาวางทับ
    screen.blit(rolldice_font.render('Roll Dice', True, (0,0,0)), (758, 275)) #เขียน text ลงบนจอ
    #---แสดงตาของผู้เล่นคนแรก-------------------------------------------------
    trun_text = turn_font.render("Player 1 Turn", True, p_color[0], (0,0,0))
    screen.blit(trun_text, (620, 480))
    #************สั่งให้อัพเดทหน้าจอ****************
    pygame.display.update() #สั่งให้อัพเดทหน้าจอ เอาไว้ใช้ตอนเปลี่ยนภาพ (เจาะจงพื้นที่ได้)

def main_menu():
    """main menu ui and operate"""
    menu_bg_img = pygame.image.load("Mainmenu_bg.png")
    screen.blit(menu_bg_img, (0, 0))
    start_bt_area = pygame.Rect(120,430,250,155)
    quit_bt_area = pygame.Rect(630,430,250,155)
    #pygame.draw.rect(screen, (255,255,255), start_bt_area)
    #pygame.draw.rect(screen, (255,255,255), quit_bt_area)
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.MOUSEBUTTONUP:
                mouse_pos = pygame.mouse.get_pos()
                if start_bt_area.collidepoint(mouse_pos):
                    return 0
                elif quit_bt_area.collidepoint(mouse_pos):
                    quit()

#*******************เปิดเกมมาต้องทำไรบ้าง********************************************************************************
#---สร้าง & ตั้งค่าขนาดหน้าจอ-------------------------------------------------
pygame.init()
screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Snake and Ladder Inwza007")

#*******************สร้างตัวแปรสำคัญๆหลักๆ********************************************************************************
#*****งูและบันได ถ้าตกช่องไหน(key)ให้ไปตรงไหน(value)******
ladder={6: 35,
        41: 79,
        57: 65,
        75: 95}

snake ={49: 13,
        67: 46,
        87: 51,
        98: 3}
#*****ภาพลูกเต๋า*******
dice_img_list = [pygame.image.load("1diceface.png"), \
                pygame.image.load("2diceface.png"), \
                pygame.image.load("3diceface.png"), \
                pygame.image.load("4diceface.png"), \
                pygame.image.load("5diceface.png"), \
                pygame.image.load("6diceface.png")]
dice_img_position = (700, 40)
dice_img_area = pygame.Rect(700, 40, 200, 200)

#*****ภาพตาราง*******
table = pygame.image.load("table_1.png")

#*****ปุ่มทอยเต๋า*******
button_diceroll_area = pygame.Rect(750, 260, 100, 50) #(สีเหลี่ยมที่ตำแหน่ง ห่างขอบซ้าย750 ห่างบน260 กว้าง100 สูง50) (ประมาณว่าคุณลักษณะสี่เหลี่ยม)

#*****ตำแหน่งของแต่ละผู้เล่น ตามลำดับ******
player_position = [1, 1, 1, 1]

#*****สีของแต่ละผู้เล่น ตามลำดับ*******
p_color = [(255, 255, 255), (255, 0, 0), (0, 255, 0), (0, 0, 255)]

#*****กำหนด font*******
rolldice_font = pygame.font.Font('freesansbold.ttf', 20) #กำหนด font และขนาด ใส่ไปในตัวแปร
turn_font = pygame.font.Font('freesansbold.ttf', 40)
log_font = pygame.font.Font('freesansbold.ttf', 18)
#------------------------------------------------------------------------------------------------------------------

block_position_dict = set_position_each_block() #กำหนดจุดพิกัด(x, y)ล่างซ้ายของแต่ละช่องในตารางเกม
main_menu()
main_game_ui()
playing_func()