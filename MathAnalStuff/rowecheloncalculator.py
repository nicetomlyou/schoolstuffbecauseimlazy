def row_mult(row, num):
    return [x * num for x in row]


def row_sub(row_left, row_right):
    return [a - b for (a, b) in zip(row_left, row_right)]


def row_echelon(mtx):
    temp_mtx = list(mtx)

    def echelonify(rw, col):
        for i, row in enumerate(temp_mtx[(col + 1):]):
            i += 1
            if rw[col] == 0:
                continue
            #print(temp_mtx[i + col - 1])
            temp_mtx[i + col] = row_sub(row, row_mult(rw, row[col] / rw[col]))
            print("mutated row " + str(row) + " by subrtracting " + str(row[col] / rw[col]) + " times row " + str(rw))
            print("resulting row: " + str(row_sub(row, row_mult(rw, row[col] / rw[col]))))

    for i in range(len(mtx)):
        #print(temp_mtx)
        active_row = temp_mtx[i]
        #print(active_row)
        echelonify(active_row, i)


    temp_mtx = [
        [(0 if (0.0000000001 > x > -0.0000000001) else x)
         for x in row]
        for row in temp_mtx
    ]

    return temp_mtx


if __name__ == '__main__':
    print("[ Row Echelon Calculator ] ")
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
        mtx_result = row_echelon(mtx)
        for row in mtx_result:
            print(' '.join(("{0:.2f}".format(x) for x in row)))
        # print("d: eof")
    except Exception as e:
        print("exception while calculating row echelon form: " + str(e))
        exit(1)