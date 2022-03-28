import numpy as np
import random
from time import thread_time
from math import factorial


# class CheckSul:
def done_or_not(): #board[i][j]
    while True:
        b = creater_table()
        # b = [[1, 3, 2, 5, 7, 9, 4, 6, 8]
        #             ,[4, 9, 8, 2, 6, 1, 3, 7, 5]
        #             ,[7, 5, 6, 3, 8, 4, 2, 1, 9]
        #             ,[6, 4, 3, 1, 5, 8, 7, 9, 2]
        #             ,[5, 2, 1, 7, 9, 3, 8, 4, 6]
        #             ,[9, 8, 7, 4, 2, 6, 5, 3, 1]
        #             ,[2, 1, 4, 9, 3, 5, 6, 8, 7]
        #             ,[3, 6, 5, 8, 1, 7, 9, 2, 4]
        #             ,[8, 7, 9, 6, 4, 2, 1, 5, 3]]
        board = np.array(b)
        rows = [board[i,:] for i in range(9)]
        cols = [board[:,j] for j in range(9)]
        sqrs = [board[i:i+3,j:j+3].flatten() for i in [0,3,6] for j in [0,3,6]]
        cnt = 0
        for view in np.vstack((rows,cols,sqrs)):
            a = False
            if len(np.unique(view)) != 9:
                a = True
            else:
                cnt += 1
            if cnt == 9:
                print(thread_time())
                return print(b)
            if a == True:
                break

    
def creater_table():
    a = []
    b = []
    list  = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(9):
        temp_list = list.copy()
        # for j in range(9):
        flag = False
        cnt = 0
        while flag == False:
            temp  = temp_list.pop(random.randint(0, len(temp_list) - 1))
            try:
                # print(tuple(b[z][9 - len(temp_list) - 1] for z in range(i)))
                if temp not in tuple(b[z][9 - len(temp_list) - 1] for z in range(i)):
                    a.append(temp)
                else:
                    cnt += 1
                    temp_list.append(temp)
                    if cnt > factorial(len(temp_list)):
                        temp_list = list.copy()
                        a = []
                        cnt = 0
            except IndexError:
                a.append(temp)
            if len(temp_list) == 0:
                flag = True
        b.append(a)
        a = []
    return b

done_or_not()