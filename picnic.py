"""
## counting all case w/ ordering 4 dup cases
# input
3 -> test_num
2 1 -> std_num, pair_num
0 1 -> std_ids w/ friend
3
2 1
0 1
4 6
0 1 1 2 2 3 3 0 0 2 1 3
6 10
0 1 0 2 1 2 1 3 1 4 2 3 2 4 3 4 3 5 4 5

# output
1 -> # of pairing case
3
4
"""
import sys

rl = lambda: sys.stdin.readline()


def show_mat1(mat, size, prefix="mat1: "):
    _row = ''
    for _x in xrange(size):
        _row = _row + str(mat[_x]) + ' '
    print prefix + _row


def show_mat2(mat, size):
    for _y in xrange(size):
        _row = ''
        for _x in xrange(size):
            _row = _row + str(mat[_y][_x]) + ' '
        print _row


def count_pairs(_taken):
    finished = True
    for std in xrange(std_num):
        if _taken[std] is False:
            finished = False
    if finished is True:
        return 1

    ret = 0
    for _i in xrange(std_num):
        for _j in xrange(std_num):
            if _taken[_i] is False and _taken[_j] is False and friends[_i][_j] is True:
                _taken[_i] = _taken[_j] = True
                ret += count_pairs(_taken)
                _taken[_i] = _taken[_j] = False
    return ret


def count_pairs3(_taken):
    first = -1
    for std in xrange(std_num):
        if _taken[std] is False:
            first = std
            break

    if first == -1:
        return 1

    cnt = 0
    for _i in xrange(first+1, std_num):
        if _taken[first] is False and _taken[_i] is False and friends[first][_i] is True:
            _taken[first] = _taken[_i] = True
            cnt += count_pairs3(_taken)
            _taken[first] = _taken[_i] = False

    return cnt


test_num = int(rl())

for test in xrange(test_num):
    line = rl().strip().split(' ')
    std_num = int(line[0])
    pair_num = int(line[1])
    taken = [False for i in xrange(10)]
    friends = [[False for x in xrange(10)] for y in xrange(10)]

    f_line = rl().strip().split(' ')
    for p_idx in xrange(pair_num):
        friends[int(f_line[p_idx*2])][int(f_line[p_idx*2+1])] = True
        friends[int(f_line[p_idx*2+1])][int(f_line[p_idx*2])] = True

    print count_pairs3(taken)


