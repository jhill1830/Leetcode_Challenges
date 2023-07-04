from collections import Counter

board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
         ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."],
         ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."],
         [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]


def isValidSudoku(board):
    # check if line has duplicate
    for line in board:
        for key in Counter(line).keys():
            if key != "." and Counter(line)[key] > 1:
                return False

        # create new array based on columns
    cols = [[".", ".", ".", ".", ".", ".", ".", ".", "."]
            for empty in range(len(board))]
    for itr, line in enumerate(board):
        for i in range(len(line)):
            cols[i][itr] = line[i]

        # check in column has duplicate
    for line in cols:
        for key in Counter(line).keys():
            if key != "." and Counter(line)[key] > 1:
                return False

        # create new array based on 3x3 groups
    subBox = [[".", ".", ".", ".", ".", ".", ".", ".", "."]
              for empty in range(len(board))]

    for itr, line in enumerate(board):
        index = 0
        if itr < 3:
            increment = 0
        if itr >= 3 and itr < 6:
            increment = 3
        if itr >= 6:
            increment = 6
        for i in range(len(line)):
            if itr < 3:
                subBox[increment][index+(3*itr)] = line[i]
                index += 1
                if index == 3:
                    index = 0
                    increment += 1

            if itr >= 3 and itr < 6:
                subBox[increment][index+(3*(itr-3))] = line[i]
                # print(index)
                index += 1
                if index == 3:
                    index = 0
                    increment += 1

            if itr >= 6:
                subBox[increment][index+(3*(itr-6))] = line[i]
                index += 1
                if index == 3:
                    index = 0
                    increment += 1

            # check if 3x3 has duplicate
    for line in subBox:
        for key in Counter(line).keys():
            if key != "." and Counter(line)[key] > 1:
                return False

    print(subBox)


isValidSudoku(board)
