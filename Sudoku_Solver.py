from pprint import pprint

def find_next_empty(puzzle):
    for r in range(9):
        for c in range(9): 
            if puzzle[r][c] == -1:
                return r, c
    return None, None 

def is_valid(puzzle, guess, row, col):
    row_vals = puzzle[row]
    if guess in row_vals:
        return False
        
    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False

    row_start = (row // 3) * 3
    col_start = (col // 3) * 3
    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False

    return True

def solve_sudoku(puzzle):
    row, col = find_next_empty(puzzle)
    if row is None:
        return True 
    for guess in range(1, 10):
        if is_valid(puzzle, guess, row, col):
            puzzle[row][col] = guess
            if solve_sudoku(puzzle):
                return True
        puzzle[row][col] = -1
    return False

if __name__ == '__main__':
    # execution_board = [
    #     [1, 0, 0,   0, 0, 7,   0, 9, 0],
    #     [0, 3, 0,   0, 2, 0,   0, 0, 8],
    #     [0, 0, 9,   6, 0, 0,   5, 0, 0],

    #     [0, 0, 5,   3, 0, 0,   9, 0, 0],
    #     [0, 1, 0,   0, 8, 0,   0, 0, 2],
    #     [6, 0, 0,   0, 0, 4,   0, 0, 0],

    #     [3, 0, 0,   0, 0, 0,   0, 1, 0],
    #     [0, 4, 0,   0, 0, 0,   0, 0, 7],
    #     [0, 0, 7,   0, 0, 0,   3, 0, 0]
    # ]
    execution_board=[[[] for j in range(9)] for i in range(9)]
    for i in range(9):
        for j in range(9):
            number=int(input("Enter value:")) 
            if number==0:
                execution_board[i][j]=-1
            else:
                execution_board[i][j]=number
    print(solve_sudoku(execution_board))
    pprint(execution_board)
