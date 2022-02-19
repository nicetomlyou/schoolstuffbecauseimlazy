from math import sqrt

import numpy
import numpy as np
from numpy import reshape
from numpy import fliplr
def checksquare(mtx):
    rows = len(mtx[0])
    index = -1
    for column in mtx:
        index = index + 1
        if index + 1 == len(mtx):
            if len(column) == rows:
                return True, rows
            else:
                return False
        else:
            if len(column) == rows:
                continue
            else:
                return False


def det(mtx, dim):
    if dim == 2:
        return (mtx[0][0] * mtx[1][1] - mtx[0][1] * mtx[1][0])
    if dim == 3:
        a = []
        
        for num in range(0, dim):
            for num1 in range(0, dim):
                if num == 0 or 1:
                    a.append(mtx[num][num1])

        a.insert(3, mtx[0][0])
        a.insert(4, mtx[0][1])
        a.insert(8, mtx[1][0])
        a.insert(9, mtx[1][1])
        a.insert(13, mtx[2][0])
        a.insert(14, mtx[2][1])

        a = np.array(a)
        a = a.reshape(3,5)
        diags = []
        for num in range(0, dim):
            diags.append(a.diagonal(num))
        for num in range(0, dim):
            diags.append(fliplr(a).diagonal(num))
        diags = np.array(diags)
        return diagmult(diags[0]) + diagmult(diags[1]) + diagmult(diags[2]) - diagmult(diags[3]) - diagmult(diags[4]) - \
               diagmult(diags[5])

def diagmult(arr):
    return numpy.prod(arr)

def getdet(mtx):
    check, dimensions = checksquare(mtx)

    if check == True:
        determinant = det(mtx, dimensions)
        return determinant
    else:
        print("not a square matrix")
        exit(1)

if __name__ == '__main__':
    print("Matrix Determinant Calculator")
    print("Type any number of rows to \nmake a matrix.")
    print("Type a . to stop entering a matrix.")
    mtx = []

    n_tries = 1000
    while n_tries > 0:
        n_tries -= 1
        try:
            inp = input("> ").strip()
        except KeyboardInterrupt:
            print("interrupted - exiting")
            exit(0)

        if inp == '.':
            break

        elif inp == '':
            print("empty line - try again!")
            continue

        try:
            row = list(map(float, inp.split()))
            mtx.append(row)
        except Exception as e:
            print("exception while reading this row:" + str(e))
            print("try again!")

    try:
        mtx_result = getdet(mtx)
        print("the determinant of the matrix is: " + str(mtx_result))
        # print("d: eof")
    except Exception as e:
        print("exception while calculating determinant: " + str(e))
        exit(1)
