import pygame
import random

class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.grid = [['dirty' for _ in range(width)] for _ in range(height)]

    def set_obstacle(self, x, y):
        """Mark a cell as an obstacle."""
        if 0 <= x < self.width and 0 <= y < self.height:
            self.grid[y][x] = 'obstacle'

    def clean_cell(self, x, y):
        """Mark a cell as cleaned."""
        if 0 <= x < self.width and 0 <= y < self.height:
            self.grid[y][x] = 'clean'

    def is_dirty(self, x, y):
        """Check if a cell is still dirty."""
        return self.grid[y][x] == 'dirty'

    def display_grid(self):
        """Print the grid (for debugging)."""
        for row in self.grid:
            print(" ".join(row))
        print()
