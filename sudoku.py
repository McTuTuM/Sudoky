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
        self.core()
        

    def exit(self):
        pygame.quit()
        sys.exit()

    def core(self):
        self.draw_win_before()
        while self.game_over == False:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEBUTTONUP:
                    self.click(event.pos[0], event.pos[1], event.type)
                if event.type == pygame.QUIT:
                    self.exit()
                if self.press == True:
                    if event.type == pygame.KEYDOWN:
                        if event.key >= 49 and event.key <= 58:
                                self.input_key(event.key)
                pygame.display.flip()
            
    def click(self, x, y, event_type):
        if event_type == pygame.MOUSEBUTTONUP: #only bitton options or not....
            if x > 730 and x < 880 and y > 610 and y < 690:
                self.exit()
            if self.start_game == False:
                if x > 730 and x < 880 and y > 60 and y < 140:
                    self.start()       
                if x > 730 and x < 880 and y > 160 and y < 240:
                    self.game_mode_set()
            else:
                if x > 730 and x < 880 and y > 60 and y < 140:
                    print('__________________')
                    
                if x > 730 and x < 880 and y > 160 and y < 240:
                    self.start_game = False
                    sleep(1)
                    self.game_mode = 0
                    self.draw_win_before()
                if x > 50 and x < 680 and y > 60 and y < 690:
                    self.check(x, y)

    def check(self, x, y):
        x_start = 50
        y_start = 60
        step = 70
        for i in range(1, 10):
            for j in range(1, 10):
                if x > x_start + step * (i - 1) and x < x_start + step * i and y > y_start + step * (j - 1) and y < y_start + step * j:
                    num = self.table[j - 1][i - 1]
                    if num == 0:
                        self.press = True
                        pygame.draw.rect(self.screen, 'white', [(50, 60), (630, 630)]) # game_field
                        self.draw_grid()
                        self.draw_numbs()
                        self.red_sqrt((x_start + step * (i - 1)) + 3, (y_start + step * (j - 1)) + 3, step - 5)
                        self.i, self.j = i, j
                        print('empty', self.fin_table[j - 1][i - 1])
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
        pygame.display.update
        if self.fin_table[self.j - 1][self.i - 1] == self.key:
            self.table[self.j - 1][self.i - 1] = self.key
        else:
            print("nOOOOOOOOOOOOOOOOOO")

        if self.fin_table == self.table:
            print('game win')

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
        self.press = False
        self.start_game = True
        threading.Thread(target=self.timer, daemon= True).start()
        check_sul = CheckSul()
        check_sul._creater_table()
        self.table = check_sul.game_table      
        self.fin_table = check_sul.table  
        self.draw_win_after()
        self.draw_grid()
        self.draw_numbs()

    def timer(self): 
        f1 = pygame.font.Font(None, 48)
        for m1 in range(6):
            for m2 in range(10):
                for s1 in range(6):
                    for s2 in range(10):
                        if self.start_game == False:
                           return                         
                        pygame.draw.rect(self.screen, 'white', [(730, 260), (150, 50)])
                        self.screen.blit(f1.render(f"{m1}{m2}:{s1}{s2}", True, 'black'), (760, 265))        
                        pygame.display.update()
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
        f1 = pygame.font.Font(None, 48)
        self.game_mode += 1
        if self.game_mode > 3:
            self.game_mode -= 3
        if self.game_mode == 1:
            pygame.draw.rect(self.screen, 'green', [(730, 160), (150, 80)])
            self.screen.blit(f1.render("Легкая", True, 'black'), (750, 180))

        elif self.game_mode == 2:
            pygame.draw.rect(self.screen, 'yellow', [(730, 160), (150, 80)])
            self.screen.blit(f1.render("Средняя", True, 'black'), (732, 180))  
        else:
            pygame.draw.rect(self.screen, 'red', [(730, 160), (150, 80)])
            self.screen.blit(f1.render("Сложная", True, 'black'), (732, 180))

    def draw_win_after(self):
        f1 = pygame.font.Font(None, 48)
        f2 = pygame.font.Font(None, 38)
        pygame.draw.rect(self.screen, 'white', [(50, 60), (630, 630)])
        pygame.draw.rect(self.screen, 'white', [(730, 60), (150, 80)]) #buttom start game
        self.screen.blit(f1.render("Пауза", True, 'black'), (745, 80))
        pygame.draw.rect(self.screen, 'white', [(730, 160), (150, 80)])  #bottom_pause
        self.screen.blit(f2.render('Новая игра', True, 'black'), (730, 180))
        pygame.draw.rect(self.screen, 'white', [(730, 260), (150, 50)]) #lable_time


    def draw_win_before(self):
        f1 = pygame.font.Font(None, 48)
        self.screen = pygame.display.set_mode((self.wight, self.height))
        self.screen.fill((75,75,75))
        pygame.draw.rect(self.screen, (200,200,200), [(50, 60), (630, 630)])
        pygame.draw.rect(self.screen, 'white', [(730, 60), (150, 80)]) #buttom start game
        self.screen.blit(f1.render("Начать", True, 'black'), (745, 80))
        self.game_mode_set()
        # pygame.draw.rect(self.screen, 'green', [(730, 160), (150, 80)])  #buttom dif mode
        pygame.draw.rect(self.screen, 'white', [(730, 610), (150, 80)])   #buttom quit
        self.screen.blit(f1.render("Выход", True, 'black'), (750, 635))

    def red_sqrt(self,x1,y1,step):
        pygame.draw.rect(self.screen, 'red', [(x1, y1), (step, step)], 3)
        


# class GameWindow(MainWindow):
#     def __init__(self):
#        self.num_bloc = num_bloc # цифра в блоке 
#        self.status = status # изменяемый блок или нет 
#        self.corrent = corrent  # верное значение или нет  0 \ 1 


if __name__ == '__main__':
    d = MainWindow()
