"""
## counting all case w/ priority 4 dup cases
# input
3 -> test_num (<=30)
3 7 -> height width (1<=h,w<=20)
#..# -> #: black, .: white (.<=50)

sol)
0. filtering: # of white is N*3 because block size is 3
1. brute-force: 4case block w/ recursion => duplication w/ 4case block cover ordering
2. BF w/ priority: first cover at top/left white position

3
3 7
#.....#
#.....#
##...##
3 7
#.....#
#.....#
##..###
8 10
##########
#........#
#........#
#........#
#........#
#........#
#........#
##########

# output
0 -> # of case
2
1514
"""
import my_utils
import sys

rl = lambda: sys.stdin.readline()
test_num = int(rl())

# ny, nx
block_type = [
    [[0, 0], [0, 1], [1, 0]],
    [[0, 0], [0, 1], [1, 1]],
    [[0, 0], [1, 0], [1, 1]],
    [[0, 0], [1, -1], [1, 0]]
]


def cover(_board, _y, _x, _type, _value):
    ok = True
    for ptr in range(3):
        ny = _y + block_type[_type][ptr][0]
        nx = _x + block_type[_type][ptr][1]

        if ny < 0 or ny >= height or nx < 0 or nx >= width:
            ok = False
        else:
            _board[ny][nx] += _value
            if _board[ny][nx] > 1:
                ok = False
            # if _value == 1: # cover
            #     if _board[ny][nx] != 0:
            #         _board[ny][nx] = _value
            #         ok = False
            #     elif _board[ny][nx] != 9:
            #         _board[ny][nx] = _value
            #         ok = False
            # else:   # 0(uncover)
            #     if _board[ny][nx] == 1:
            #         ok = False
            #     else:
            #         _board[ny][nx] = _value
    return ok


def count_cover(_board):
    x = y = -1

    # find left/top blank
    for _y in range(height):
        for _x in range(width):
            if _board[_y][_x] == 0:  # found
                x = _x
                y = _y
                break
        if y != -1:  # found
            break

    # final state
    if y == -1:
        # print("x: " + str(x) + " y: " + str(y))
        return 1

    cnt = 0
    # try cover w/ 4 block type
    for _type in range(4):
        if cover(_board, y, x, _type, 1) is True:
            cnt += count_cover(_board)
        cover(_board, y, x, _type, -1)  # reset because of before covering check

    return cnt


for test in range(test_num):
    line = rl().strip().split(' ')
    height = int(line[0])
    width = int(line[1])
    board = [[0 for w in range(20)] for h in range(20)]

    w_cnt = 0
    for _h in range(height):
        f_line = list(rl().strip())
        for _w in range(width):
            if f_line[_w] == '#':
                board[_h][_w] = 1
            else:
                w_cnt += 1

    # my_utils.show_mat2(board, 20)

    if (w_cnt % 3) == 0 and w_cnt <= 50:
        print(count_cover(board))
    else:
        print(0)

