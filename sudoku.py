from time import sleep
import pygame
from pygame.color import THECOLORS
import sys, threading
from logic import CheckSul

pygame.init
pygame.font.init()
class MainWindow():
    def __init__(self):
        self.height = 750
        self.wight = 950
        self.game_over = False
        self.start_game = False
        self.press = False
        self.game_mode = 0
        self.table = []
        self.fin_table = []
        self.key, self.i, self.j = 0, 0, 0
        self.live = 3
        self.mode_pause = False
        # self.core()

    def fonts(self, font_size, text, x, y, color = "black"):
        f = pygame.font.Font(None, font_size)
        self.screen.blit(f.render(text, True, color), (x, y))
   
    def exit(self):
        pygame.quit()
        sys.exit()

    def core(self):
        self.draw_win_before()
        while True:
            for event in pygame.event.get():
                if self.game_over == True:
                    if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN:
                        self.start_game = False
                        self.game_over = False
                        self.game_mode = 0
                        self.draw_win_before()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.click(event.pos[0], event.pos[1], event.type)
                if event.type == pygame.QUIT:
                    self.exit()
                if self.press == True:
                    if event.type == pygame.KEYDOWN:
                        if event.key >= 49 and event.key <= 58:
                                self.input_key(event.key)
                pygame.display.flip()
            
    def click(self, x, y, event_type):
        if event_type == pygame.MOUSEBUTTONDOWN:
            if x > 730 and x < 880 and y > 610 and y < 690:
                self.exit()
            if self.start_game == False:
                if x > 730 and x < 880 and y > 60 and y < 140:
                    self.start()       
                if x > 730 and x < 880 and y > 160 and y < 240:
                    self.game_mode_set()
            else:
                if x > 730 and x < 880 and y > 60 and y < 140:
                    if self.mode_pause == False:
                        self.pause() 
                    else:
                        self.mode_pause = False   
                        pygame.draw.rect(self.screen, 'white', [(50, 60), (630, 630)])
                        self.draw_grid()
                        self.draw_numbs()   
                        pygame.draw.rect(self.screen, 'white', [(730, 60), (150, 80)])
                        self.fonts(48, "Пауза", 755, 80)
                    
                if x > 730 and x < 880 and y > 160 and y < 240:
                    self.start_game = False
                    self.game_mode = 0
                    self.draw_win_before()
                if x > 50 and x < 680 and y > 60 and y < 690:
                    self.check(x, y)

    def pause(self):
        self.mode_pause = True
        pygame.draw.rect(self.screen, (200,200,200), [(50, 60), (630, 630)])
        pygame.draw.rect(self.screen, 'white', [(730, 60), (150, 80)])
        self.fonts(32, "Возобновить", 735, 85)
        self.fonts(72, "Пауза", 300, 330)

    def check(self, x, y):
        x_start = 50
        y_start = 60
        step = 70
        for i in range(1, 10):
            for j in range(1, 10):
                if x > x_start + step * (i - 1) and x < x_start + step * i and y > y_start + step * (j - 1) and y < y_start + step * j:
                    num = self.table[j - 1][i - 1]
                    pygame.draw.rect(self.screen, 'white', [(50, 60), (630, 630)]) # game_field
                    self.draw_grid()
                    self.draw_numbs()
                    if num == 0:
                        self.press = True
                        # self.draw_grid()
                        # self.draw_numbs()
                        self.red_sqrt((x_start + step * (i - 1)) + 3, (y_start + step * (j - 1)) + 3, step - 5)
                        self.i, self.j = i, j
                        print('empty', self.fin_table[j - 1][i - 1])
                    else:      
                        for i_0 in range(1, 10):
                            for j_0 in range(1, 10):
                                if num == self.table[j_0 - 1][i_0 - 1]:
                                    self.red_sqrt((x_start + step * (i_0 - 1)) + 3, (y_start + step * (j_0 - 1)) + 3, step - 5)
                    print('__', i, j, x, y)
                    print('***', self.table[j - 1][i - 1])
                    
    def input_key(self, key):
        self.key = key - 48
        x_start = 50
        y_start = 60
        step = 70
        sur = pygame.image.load(f'png/{str(self.key)}.png')
        rec = sur.get_rect(center  = ((x_start + int(1/2 * step) + step * (self.i - 1)) + 1, ( y_start + int(1/2 * step) + step * (self.j - 1)) + 1))
        self.screen.blit(sur, rec)
        self.correct()

    def correct(self):
        if self.fin_table[self.j - 1][self.i - 1] == self.key:
            self.table[self.j - 1][self.i - 1] = self.key
        else:
            self.live -= 1
            pygame.draw.rect(self.screen, 'white', [(730, 330), (150, 80)]) # rect number lives
            sur_heart = pygame.image.load('png/heart.png')
            rec_heart = sur_heart.get_rect(center = (790, 370))# 120 60
            self.screen.blit(sur_heart, rec_heart)
            self.fonts(80, str(self.live), 850, 343)
            print(self.live)

        if self.fin_table == self.table:
            self.win() 
        if self.live <= 0:
            self.lose()
        pygame.display.update

    def lose(self):
        self.game_over = True
        pygame.draw.rect(self.screen, 'white', [(50, 60), (630, 630)])
        self.fonts(70, "Повезет в другой раз..:)", 65, 330)
        self.fonts(65, "Нажмите любую клавишу", 70, 400)   

    def win(self):
        self.game_over = True
        pygame.draw.rect(self.screen, 'white', [(50, 60), (630, 630)])
        self.fonts(70, "Победа!!!", 300, 330)
        self.fonts(65, "Нажмите любую клавишу", 70, 400)
        pygame.display.update

    def draw_numbs(self):
        x_start = 50
        y_start = 60
        step = 70
        for i in range(1, 10):
            for j in range(1, 10):
                num = self.table[j - 1][i - 1]
                if num != 0:
                    sur = pygame.image.load(f'png/{str(num)}.png')
                    rec = sur.get_rect(center  = ((x_start + int(1/2 * step) + step * (i - 1)) + 1, ( y_start + int(1/2 * step) + step * (j - 1)) + 1))
                    self.screen.blit(sur, rec)
                    pygame.display.update

    def start(self):
        self.live = 3
        self.press = False
        self.start_game = True
        check_sul = CheckSul(self.game_mode)
        check_sul._creater_table()
        self.table = check_sul.game_table      
        self.fin_table = check_sul.table  
        sleep(0.1)
        self.draw_win_after()
        self.draw_grid()
        self.draw_numbs()
        threading.Thread(target=self.timer, daemon= True).start()

    def timer(self): 
        f1 = pygame.font.Font(None, 48)
        for m1 in range(6):
            for m2 in range(10):
                for s1 in range(6):
                    for s2 in range(10):
                        if self.start_game == False or self.game_over == True:
                            return                                                                                               
                        pygame.draw.rect(self.screen, 'white', [(730, 260), (150, 50)])
                        self.screen.blit(f1.render(f"{m1}{m2}:{s1}{s2}", True, 'black'), (760, 268))        
                        pygame.display.update()
                        while self.mode_pause == True:
                            sleep(0.1)
                        sleep(1)
        return
            

    def draw_grid(self):
        step = 630 / 9
        for i in range(1, 11):
            w = 3
            if (i - 1) % 3 == 0:
                w = 7
            x0 = 50
            x1 = 680
            y0 = i * step - 10         
            y1 = i * step - 10
            x0_1 = i * step - 20 
            x1_1 = i * step - 20 
            y0_1 = 60
            y1_1 = 690
            self.draw_line(x0, x1, y0, y1, x0_1, x1_1, y0_1, y1_1, w)

    def draw_line(self, x0, x1, y0, y1, x0_1, x1_1, y0_1, y1_1, w):
        pygame.draw.line(self.screen, 'black', (x0, y0), (x1, y1), w)
        pygame.draw.line(self.screen, 'black', (x0_1, y0_1), (x1_1, y1_1), w)

    def game_mode_set(self):
        self.game_mode += 1
        if self.game_mode > 3:
            self.game_mode -= 3
        if self.game_mode == 1:
            pygame.draw.rect(self.screen, 'green', [(730, 160), (150, 80)])
            self.fonts(48, "Легкая", 750, 180) 
            # self.screen.blit(f1.render("Легкая", True, 'black'), (750, 180))

        elif self.game_mode == 2:
            pygame.draw.rect(self.screen, 'yellow', [(730, 160), (150, 80)])
            self.fonts(48, "Средняя", 732, 180) 
            # self.screen.blit(f1.render("Средняя", True, 'black'), (732, 180))  
        else:
            pygame.draw.rect(self.screen, 'red', [(730, 160), (150, 80)])
            self.fonts(48, "Сложная", 732, 180) 
            # self.screen.blit(f1.render("Сложная", True, 'black'), (732, 180))

    def draw_win_after(self):
        pygame.draw.rect(self.screen, 'white', [(50, 60), (630, 630)])
        pygame.draw.rect(self.screen, 'white', [(730, 60), (150, 80)]) #buttom start game
        self.fonts(48, "Пауза", 755, 80) 
        pygame.draw.rect(self.screen, 'white', [(730, 160), (150, 80)])  #bottom_pause
        self.fonts(38, 'Новая игра', 733, 185) 
        pygame.draw.rect(self.screen, 'white', [(730, 260), (150, 50)]) #lable_time
        pygame.draw.rect(self.screen, 'white', [(730, 330), (150, 80)]) # rect number lives
        sur_heart = pygame.image.load('png/heart.png')
        rec_heart = sur_heart.get_rect(center = (790, 370))# 120 60
        self.screen.blit(sur_heart, rec_heart)
        self.fonts(80, str(self.live), 850, 343) 


    def draw_win_before(self):
        f1 = pygame.font.Font(None, 48)
        self.screen = pygame.display.set_mode((self.wight, self.height))
        self.screen.fill((75,75,75))
        pygame.draw.rect(self.screen, (200,200,200), [(50, 60), (630, 630)])
        pygame.draw.rect(self.screen, 'white', [(730, 60), (150, 80)]) #buttom start game
        self.screen.blit(f1.render("Начать", True, 'black'), (745, 80))
        self.game_mode_set()
          #buttom dif mode
        pygame.draw.rect(self.screen, 'white', [(730, 610), (150, 80)])   #buttom quit
        self.screen.blit(f1.render("Выход", True, 'black'), (750, 635))

    def red_sqrt(self,x1,y1,step):
        pygame.draw.rect(self.screen, 'red', [(x1, y1), (step, step)], 3)

if __name__ == '__main__':
    d = MainWindow()
    d.core()