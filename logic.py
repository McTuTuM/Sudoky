import random
import copy


class CheckSul:
    def __init__(self, game_mode):
        self.game_table = []
        self.table = []
        self.n = 3
        self.game_mode = game_mode

       
    def _creater_table(self):
        a = []
        for i in range(9):
            for j in range(9):
                 a.append(int((i*3 + i/3 + j) % 9 + 1))
            self.table.append(a)
            a = []
        self.mix()

    def transposing(self):
        self.table = list(map(list, zip(*self.table)))

    def swap_rows_small(self):
        area = random.randrange(self.n)
        line1 = random.randrange(self.n)
        N1 = area*self.n + line1
        line2 = random.randrange(self.n)
        while (line1 == line2):
            line2 = random.randrange(self.n)
        N2 = area*self.n + line2
        self.table[N1], self.table[N2] = self.table[N2], self.table[N1]

    def swap_colums_small(self):
        self.transposing()
        self.swap_rows_small()
        self.transposing()

    def swap_colums_area(self):
        self.transposing()
        self.swap_rows_area()
        self.transposing()

    def swap_rows_area(self):
        area1, area2 = random.sample(range(3), 2)
        for i in range(3):
            n1, n2 = area1 * 3 + i, area2 * 3 + i
            self.table[n1], self.table[n2] = self.table[n2], self.table[n1]

    def mix(self, amt = 15):
        mix_func = (
			self.swap_rows_small,
			self.swap_colums_small,
			self.swap_rows_area,
			self.swap_colums_area,
		)
        
        for _ in range(amt):
            self.transposing()
            random.choice(mix_func)()
        self.game_table = copy.deepcopy(self.table)
        self.diff()
        print(self.table)

    def diff(self):
        # a = self.table.copy()
        if self.game_mode == 1:
            diff = 0.7
        elif self.game_mode == 2:
            diff = 0.6
        else:
            diff = 0.5
        for i in range(self.n**2):
            for j in range(self.n**2):
                if self.game_table[i][j] == 0:
                    continue
                if random.random() > diff:
                    self.game_table[i][j] = 0
        # self.game_table = a
        print()
# a = CheckSul()
# a._creater_table()








    # def done_or_not(self): #board[i][j]
    #     while True:
    #         # b = [[1, 3, 2, 5, 7, 9, 4, 6, 8]
    #         #             ,[4, 9, 8, 2, 6, 1, 3, 7, 5]
    #         #             ,[7, 5, 6, 3, 8, 4, 2, 1, 9]
    #         #             ,[6, 4, 3, 1, 5, 8, 7, 9, 2]
    #         #             ,[5, 2, 1, 7, 9, 3, 8, 4, 6]
    #         #             ,[9, 8, 7, 4, 2, 6, 5, 3, 1]
    #         #             ,[2, 1, 4, 9, 3, 5, 6, 8, 7]
    #         #             ,[3, 6, 5, 8, 1, 7, 9, 2, 4]
    #         #             ,[8, 7, 9, 6, 4, 2, 1, 5, 3]]
    #         board = np.array(self.table)
    #         rows = [board[i,:] for i in range(9)]
    #         cols = [board[:,j] for j in range(9)]
    #         sqrs = [board[i:i+3,j:j+3].flatten() for i in [0,3,6] for j in [0,3,6]]
    #         cnt = 0
    #         for view in np.vstack((rows,cols,sqrs)):
    #             a = False
    #             if len(np.unique(view)) != 9:
    #                 a = True
    #             else:
    #                 cnt += 1
    #             if cnt >= 26:
    #                 print(thread_time())
    #                 print(self.table)
    #                 return self.table
    #             if a == True:
    #                 break


#         a = []
#         b = []
#         list = [i for i in range(1, 10)]
#         for i in range(9):
#             temp_list = list.copy()
#             # for j in range(9):
#             flag = False
#             cnt = 0
#             while flag == False:
#                 temp  = temp_list.pop(random.randint(0, len(temp_list) - 1))
#                 try:
#                     # print(tuple(b[z][9 - len(temp_list) - 1] for z in range(i)))
#                     if temp not in tuple(b[z][9 - len(temp_list) - 1] for z in range(i)):
#                         a.append(temp)
#                     else:
#                         cnt += 1
#                         temp_list.append(temp)
#                         if cnt > factorial(len(temp_list)):
#                             temp_list = list.copy()
#                             a = []
#                             cnt = 0
#                 except IndexError:
#                     a.append(temp)
#                 if len(temp_list) == 0:
#                     flag = True
#             b.append(a)
#             a = []
#         return b
# CheckSul.done_or_not()