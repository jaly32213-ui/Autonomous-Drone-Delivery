import random
from utils.algorithms import astar
from utils.map_generator import generate_grid

class DroneSim:
    def __init__(self):
        self.GRID_SIZE = 20
        self.start = (0,0)
        self.goal = (19,19)
        self.grid = generate_grid(size=self.GRID_SIZE, num_obstacles=60, start=self.start, goal=self.goal)
        self.path = astar(self.grid, self.start, self.goal)
        self.drone_pos = self.start
        self.path_index = 0

    def step(self):
        if random.random() < 0.05:
            ox = random.randint(0, self.GRID_SIZE-1)
            oy = random.randint(0, self.GRID_SIZE-1)
            if (ox, oy) != self.start and (ox, oy) != self.goal:
                self.grid[oy][ox] = 1
                self.path = astar(self.grid, self.drone_pos, self.goal)
                self.path_index = 0

        if not self.path or self.path_index >= len(self.path):
            return self.drone_pos == self.goal

        self.drone_pos = self.path[self.path_index]
        self.path_index += 1
        return self.drone_pos == self.goal