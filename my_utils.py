
def show_mat2(mat, size):
    for _y in range(size):
        _row = ''
        for _x in range(size):
            _row = _row + str(mat[_y][_x]) + ' '
        print(_row)
