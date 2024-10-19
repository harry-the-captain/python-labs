import random

def display(grid):
    size = len(grid)
    hr_line = '__' * size * 2
    print(hr_line)
    for r in range(size):
        row = '|' + '|'.join(str(grid[r][c] or ' ') for c in range(size)) + '|'
        print(row)
        print(hr_line)

def initialize():
    size = int(input("Enter grid size (e.g., 9 for 9x9): "))
    if size not in [4, 9, 16]: 
        print("Invalid size. Please enter 4, 9, or 16.")
        return
    grid = [[0 for _ in range(size)] for _ in range(size)] 
    fill_grid(grid, size)
    display(grid)

def fill_grid(grid, size):
    def is_safe(grid, row, col, num):
        box_size = int(size ** 0.5)
        for x in range(size):
            if grid[row][x] == num or grid[x][col] == num:
                return False
        start_row, start_col = row - row % box_size, col - col % box_size
        for i in range(box_size):
            for j in range(box_size):
                if grid[i + start_row][j + start_col] == num:
                    return False
        return True
    
    for row in range(size):
        for col in range(size):
            if grid[row][col] == 0:
                nums = list(range(1, size + 1))
                random.shuffle(nums)  
                for num in nums:
                    if is_safe(grid, row, col, num):
                        grid[row][col] = num
                        if fill_grid(grid, size):
                            return True
                        grid[row][col] = 0
                return False  
    return True

initialize()
