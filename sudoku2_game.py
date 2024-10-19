import random

def initialize(rows, cols):
    return [[0 for _ in range(cols)] for _ in range(rows)]

def display(grid):
    for row in grid:
        print(" ".join(str(num) if num != 0 else '.' for num in row))
    print()

def is_safe(grid, num, row, col):
    for i in range(len(grid)):
        if grid[row][i] == num or grid[i][col] == num:
            return False

    box_row_start = row - row % 3
    box_col_start = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + box_row_start][j + box_col_start] == num:
                return False
    return True

def fill_grid(rows, cols):
    grid = initialize(rows, cols)

    def fill_position(row, col):
        if row == rows - 1 and col == cols:
            return True
        if col == cols:
            row += 1
            col = 0
        
        random_nums = list(range(1, 10))  
        random.shuffle(random_nums)
        for num in random_nums:
            if is_safe(grid, num, row, col):
                grid[row][col] = num
                if fill_position(row, col + 1):
                    return True
                grid[row][col] = 0  
        return False
    
    fill_position(0, 0)
    return grid

def start_game(sudoku_state, position):
    row, col, num = position
    if sudoku_state[row][col] == 0:  
        sudoku_state[row][col] = num
    else:
        print("Position already filled. Choose another position.")
    return sudoku_state

def end_game(sudoku_state):
    for row in sudoku_state:
        if 0 in row:
            return False
    print("Congratulations! You've completed the Sudoku!")
    return True

if __name__ == "__main__":
    rows = int(input("Enter the number of rows (typically 9): "))
    cols = int(input("Enter the number of columns (typically 9): "))

    sudoku_grid = fill_grid(rows, cols)
    display(sudoku_grid)

    while True:
        try:
            r = int(input("Enter row (0-indexed): "))
            c = int(input("Enter column (0-indexed): "))
            num = int(input("Enter number to place (1-9): "))
            if 0 <= r < rows and 0 <= c < cols and 1 <= num <= 9:
                sudoku_grid = start_game(sudoku_grid, (r, c, num))
                display(sudoku_grid)
                if end_game(sudoku_grid):
                    break
            else:
                print("Invalid input. Try again.")
        except ValueError:
            print("Please enter valid integers.")
