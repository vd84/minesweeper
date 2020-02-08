import numpy as np
from pandas import *
import sys
import random as rnd

MATRIX_X_LENGTH = -3
MATRIX_Y_LENGTH = -7


def printMatrixE(a):
    print("Matrix[" + ("%d" % a.shape[0]) + "][" + ("%d" % a.shape[1]) + "]")
    rows = a.shape[0]
    cols = a.shape[1]
    for i in range(0, rows):
        for j in range(0, cols):
            print("%6.3f" % a[i, j]),
        print()
    print()


coordinates_for_bombs = [[1, 2], [3, 5], [2, 2], [1, 3], [1, 1], [5, 4], [1, 4]]

matrix = [['h', 'h', 'h', 'h', 'h', 'h', 'h', 'h'],
          ['h', 'h', 'h', 'h', 'h', 'h', 'h', 'h'],
          ['h', 'h', 'h', 'h', 'h', 'h', 'h', 'h'],
          ['h', 'h', 'h', 'h', 'h', 'h', 'h', 'h'], ]


def refresh_matrix(x, y):
    clicked_coordinate = [x, y]

    if try_bomb_coordinates(x, y):
        matrix[int(x)][int(y)] = 'b'
    else:
        mark_points(x, y)


def mark_point_as_done(x, y):
    try:
        matrix[x][y] = 'O'
    except:
        return


def mark_points(x, y):
    neighbors = is_neighbor(x, y)
    if count_bombs_as_neighbors(x, y) > 0:
        mark_point_as_number_of_neighbor_bombs(x, y, count_bombs_as_neighbors(x, y))
    else:
        mark_point_as_done(x, y)

    for neighbor in neighbors:

        if count_bombs_as_neighbors(neighbor[0], neighbor[1]) == 0:
            if not try_bomb_coordinates(neighbor[0], neighbor[1]):
                mark_point_as_done(neighbor[0], neighbor[1])
        else:
            mark_point_as_number_of_neighbor_bombs(neighbor[0], neighbor[1],
                                                   count_bombs_as_neighbors(neighbor[0], neighbor[1]))


def is_neighbor(x, y):
    list_of_neighbors = []
    try:
        if y - 1 >= 0:
            list_of_neighbors.append([x, y - 1])
            list_of_neighbors.append([x + 1, y - 1])
        list_of_neighbors.append([x, y + 1])
        if x - 1 >= 0:
            list_of_neighbors.append([x - 1, y])
            list_of_neighbors.append([x - 1, y + 1])

        list_of_neighbors.append([x + 1, y])
        if x - 1 >= 0 and y - 1 >= 0:
            list_of_neighbors.append([x - 1, y - 1])
        list_of_neighbors.append([x + 1, y + 1])

    except:
        return
    print(list_of_neighbors)
    return list_of_neighbors


def mark_point_as_number_of_neighbor_bombs(x, y, number):
    try:
        if not try_bomb_coordinates(x, y):
            matrix[x][y] = str(number)
    except:
        return


def mark_point_as_marked_bomb(x, y):
    matrix[x][y] = 'b'
    draw_matrix(matrix)


def count_bombs_as_neighbors(x, y):
    count = 0
    try:
        if x - 1 >= 0:
            if try_bomb_coordinates(x - 1, y):
                print("marking x-1,y")
                count = count + 1
            if try_bomb_coordinates(x - 1, y + 1):
                print("marking x-1,y+1")

                count = count + 1
        if y - 1 >= 0:
            if try_bomb_coordinates(x, y - 1):
                print("marking x,y-1")

                count = count + 1
            if try_bomb_coordinates(x + 1, y - 1):
                print("marking x+1,y-1")

                count = count + 1
        if try_bomb_coordinates(x + 1, y):
            print("marking x+1,y")

            count = count + 1
        if x - 1 >= 0 and y - 1 >= 0:
            if try_bomb_coordinates(x - 1, y - 1):
                print("marking x-1,y-1")

                count = count + 1
        if try_bomb_coordinates(x, y + 1):
            print("marking x,y+1")

            count = count + 1
        if try_bomb_coordinates(x + 1, y + 1):
            print("marking x+1,y+1")
            count = count + 1


    except:
        return

    return count


def try_bomb_coordinates(x, y):
    for i in coordinates_for_bombs:
        if i[0] == int(x):

            if i[1] == int(y):
                return True
    return False


def try_coordinates(x, y):
    refresh_matrix(x, y)
    draw_matrix(matrix)


def draw_matrix(matrix):
    s = [[str(e) for e in row] for row in matrix]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    print('\n'.join(table))


def computer_play():
    x = rnd.randint(0, 3)
    print(x)
    y = rnd.randint(0, 7)
    print(y)
    try_coordinates(x,y)



def play(x, y):
    draw_matrix(matrix)

    while True:
        want_to_mark_points = input("Want to mark point? y/n")

        x = int(input('X coord'))
        y = int(input('Y coord'))
        if want_to_mark_points == 'n':
            try_coordinates(x, y)
            if try_bomb_coordinates(x, y):
                print('BOOOM')
                sys.exit()
        else:
            mark_point_as_marked_bomb(x, y)


computer_play()
