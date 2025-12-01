import numpy as np #type:ignore 
import re

INPUT_PATH = 'input.txt'
TEST_PATH = 'test.txt'

with open(INPUT_PATH, 'r') as f:
    input_data_raw = f.read()


word = 'XMAS'
patterns = [word, word[::-1]]  # Includes both 'XMAS' and 'SMAX'

# Parse input data into a NumPy array
input_data = np.array([list(line) for line in input_data_raw.strip().split('\n')])

def count_pattern(line, patterns):
    """Count occurrences of multiple patterns in a single string."""
    return sum(line.count(pattern) for pattern in patterns)

def extract_diagonals(matrix):
    """Efficiently extract all diagonals from a 2D NumPy array."""
    rows, cols = matrix.shape
    diags = []
    # Bottom-left to top-right
    for offset in range(-rows + 1, cols):
        diags.append(''.join(np.diagonal(matrix[::-1, :], offset=offset)))
    # Top-left to bottom-right
    for offset in range(-rows + 1, cols):
        diags.append(''.join(np.diagonal(matrix, offset=offset)))
    return diags

# Horizontal and vertical lines
horizontal_lines = [''.join(row) for row in input_data]
vertical_lines = [''.join(col) for col in input_data.T]

# Diagonals
diagonals = extract_diagonals(input_data)

# Combine all lines to search
all_lines = horizontal_lines + vertical_lines + diagonals

# Count occurrences of patterns
appeared = sum(count_pattern(line, patterns) for line in all_lines)

print(appeared)

# print([n.tolist() for n in diags[:4]])

def count_xmas_patterns(grid):
    rows, cols = len(grid), len(grid[0])
    count = 0

    # Define the diagonal offsets for the X-MAS pattern
    diagonals = [
        ((-1, -1), (1, 1)),  # Top-left to bottom-right
        ((-1, 1), (1, -1))   # Top-right to bottom-left
    ]

    def is_xmas(x, y):
        # Check each diagonal pair
        for (dx1, dy1), (dx2, dy2) in diagonals:
            # Check MAS on one diagonal
            if not (0 <= x + dx1 * 2 < rows and 0 <= y + dy1 * 2 < cols and
                    grid[x + dx1][y + dy1] == 'M' and
                    grid[x + dx1 * 2][y + dy1 * 2] == 'S'):
                return False
            # Check MAS on the opposite diagonal
            if not (0 <= x + dx2 * 2 < rows and 0 <= y + dy2 * 2 < cols and
                    grid[x + dx2][y + dy2] == 'M' and
                    grid[x + dx2 * 2][y + dy2 * 2] == 'S'):
                return False
        return True

    # Iterate over all cells in the grid
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 'A' and is_xmas(i, j):
                count += 1

    return count

# print(input_data[:, :10])
# Example Input Grid

print(count_xmas_patterns(input_data_raw.strip().split()))  # Output: 9
