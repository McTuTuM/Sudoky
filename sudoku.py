import re
from time import sleep
import pygame
from pygame.color import THECOLORS
import sys, threading


pygame.init
pygame.font.init()
class MainWindow():
    def __init__(self):
        self.height = 750
        self.wight = 950
        self.game_over = False
        self.start_game = False
        self.game_mode = 0
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
                    print('__', i, j, x, y)
    def start(self):
        self.start_game = True
        threading.Thread(target=self.timer, daemon= True).start()
        self.draw_win_after()
        self.draw_grid()

    def timer(self): 
        f1 = pygame.font.Font(None, 48)
        for m1 in range(6):
            for m2 in range(10):
                for s1 in range(6):
                    for s2 in range(10):
                        pygame.draw.rect(self.screen, 'white', [(730, 260), (150, 50)])
                        self.screen.blit(f1.render(f"{m1}{m2}:{s1}{s2}", True, 'black'), (750, 280))        
                        if self.start_game == False:
                           return                         
                        sleep(1)
                        print('************')
            

    def draw_grid(self):
        step = 630 / 9
        for i in range(1, 11):
            w = 3
            if (i - 1) % 3 == 0:
                w = 10
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
        pygame.draw.rect(self.screen, 'white', [(730, 60), (150, 80)]) #buttom start game
        self.screen.blit(f1.render("Пауза", True, 'black'), (745, 80))
        pygame.draw.rect(self.screen, 'white', [(730, 160), (150, 80)])  #bottom_pause
        self.screen.blit(f2.render('Новая игра', True, 'black'), (730, 180))
        pygame.draw.rect(self.screen, 'white', [(730, 260), (150, 50)]) #lable_time


    def draw_win_before(self):
        f1 = pygame.font.Font(None, 48)
        self.screen = pygame.display.set_mode((self.wight, self.height))
        self.screen.fill(THECOLORS['grey'])
        pygame.draw.rect(self.screen, 'white', [(50, 60), (630, 630)])
        pygame.draw.rect(self.screen, 'white', [(730, 60), (150, 80)]) #buttom start game
        self.screen.blit(f1.render("Начать", True, 'black'), (745, 80))
        self.game_mode_set()
        # pygame.draw.rect(self.screen, 'green', [(730, 160), (150, 80)])  #buttom dif mode
        pygame.draw.rect(self.screen, 'white', [(730, 610), (150, 80)])   #buttom quit
        self.screen.blit(f1.render("Выход", True, 'black'), (750, 635))



# class GameWindow(MainWindow):
#     def __init__(self):
#        self.num_bloc = num_bloc # цифра в блоке 
#        self.status = status # изменяемый блок или нет 
#        self.corrent = corrent  # верное значение или нет  0 \ 1 


if __name__ == '__main__':
    d = MainWindow()
