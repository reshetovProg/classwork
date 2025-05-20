# # имя, возраст, номер группы, средний балл
#
# desk = [['-', '-', '-'],
#         ['-', '-', '-'],
#         ['-', '-', '-']]
#
# count_step=0
#
# def show_desk():
#     print("    1 2 3")
#     for i in range(len(desk)):
#         print(i+1,"|", end=" ")
#         for j in range(len(desk[i])):
#             print(desk[i][j], end=" ")
#         print()
#
# def step(symbol):
#     global count_step
#     while True:
#         y=int(input("введите номер строки: "))
#         x=int(input("введите номер столбца: "))
#         if 0<y<4 and 0<x<4 and desk[y-1][x-1]=='-':
#             desk[y-1][x-1]=symbol
#             count_step+=1
#             break
#         print("некорректные координаты")
#
# def check_result():
#     # проверка горизонтали
#     for i in range (3):
#         if desk[i][0]=='-':
#             continue
#         compare = desk[i][0]
#         flag=True
#         for j in range(3):
#             if compare!=desk[i][j]:
#                 flag=False
#                 break
#         if flag:
#             print("победил", compare)
#             return True
#
#         # проверка вертикали
#         for i in range(3):
#             if desk[0][i] == '-':
#                 continue
#             compare = desk[0][i]
#             flag = True
#             for j in range(3):
#                 if compare != desk[j][i]:
#                     flag = False
#                     break
#             if flag:
#                 print("победил", compare)
#                 return True
#
#     if count_step>=9:
#         print("ничья")
#         return True
#
#     # проверка диагонали 1
#     if desk[0][0]!='-' and desk[0][0]==desk[1][1]==desk[2][2] :
#         print("победил", desk[0][0])
#         return True
#
#     # проверка диагонали 2
#     if desk[2][0] != '-' and desk[0][2] == desk[1][1] == desk[2][0]:
#         print("победил", desk[0][2])
#         return True
#
# if __name__=="__main__":
#     while True:
#         show_desk()
#         print("ходят крестики")
#         step("X")
#         if check_result():
#             break
#
#         show_desk()
#         print("ходят нолики")
#         step("O")
#         if check_result():
#             break
#
#     show_desk()
import random

desk = [['-' for j in range(3)] for i in range(3)]
random_x = random.randint(0,2)
random_y = random.randint(0,2)
print(random_y+1, random_x+1)
count_step=0
def show_desk():
    print("    1 2 3")
    for i in range(len(desk)):
        print(i+1,"|", end=" ")
        for j in range(len(desk[i])):
            print(desk[i][j], end=" ")
        print()

def step(symbol):
    global count_step
    while True:
        y=int(input("введите номер строки: "))
        x=int(input("введите номер столбца: "))
        if 0<y<4 and 0<x<4 and desk[y-1][x-1]=='-':
            desk[y-1][x-1]=symbol
            count_step+=1
            break
        print("некорректные координаты")
    if y-1==random_y and x-1==random_x:
        desk[y - 1][x - 1] = 'X'
        print("проигрыш")
        return False
    return True

while True:
    show_desk()
    if not step('O'):
        break
    if (count_step == 8):
        print("победа")
        break
show_desk()