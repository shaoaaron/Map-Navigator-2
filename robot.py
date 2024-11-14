#note that the bot automatically cleans the first cell that it is in

class Robot:
    def __init__(self, grid, x=0, y=0):
        self.grid = grid
        self.x = x
        self.y = y

    def move(self, dx, dy):
        """Move the robot by (dx, dy) if within grid bounds."""
        new_x, new_y = self.x + dx, self.y + dy
        if 0 <= new_x < self.grid.width and 0 <= new_y < self.grid.height:
            if self.grid.grid[new_y][new_x] != 'obstacle':
                self.x, self.y = new_x, new_y
                self.grid.clean_cell(self.x, self.y)
                return True
        return False

    def display_position(self):
        """Print the robot's current position (for debugging)."""
        print(f"Robot is at ({self.x}, {self.y})")
