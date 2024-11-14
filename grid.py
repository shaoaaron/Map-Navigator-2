import pygame
import random

class Grid:
    def __init__(self, width, height, obstacle_prob=0.1):
        self.width = width
        self.height = height
        self.grid = [['dirty' for _ in range(width)] for _ in range(height)]

        for y in range(height):
            for x in range(width):
                if random.random() < obstacle_prob:
                    self.grid[y][x] = 'obstacle'

        self.base_station = (0, 0)
        self.grid[0][0] = 'base'

    def set_obstacle(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            self.grid[y][x] = 'obstacle'

    def random_update_obstacles(self, num_obstacles=1):
        for _ in range(num_obstacles):
            x, y = random.randint(0, self.width - 1), random.randint(0, self.height - 1)
            self.grid[y][x] = 'obstacle'
            chances = random.randint(0, 5)
            x, y = random.randint(0, self.width - 1), random.randint(0, self.height - 1)
            if(chances == 1 & self.grid[y][x] == 'obstacle'):
                self.grid[y][x] = 'dirty'

    def clean_cell(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            self.grid[y][x] = 'clean'

    def is_dirty(self, x, y):
        return self.grid[y][x] == 'dirty'

    def display_grid(self):
        for row in self.grid:
            print(" ".join(row))
        print()
