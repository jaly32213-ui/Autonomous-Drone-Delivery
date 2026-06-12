import random

def generate_grid(size=20, num_obstacles=60, start=(0,0), goal=(19,19)):
    grid=[[0 for _ in range(size)] for _ in range(size)]
    for _ in range(num_obstacles):
        x=random.randint(0,size-1)
        y=random.randint(0,size-1)
        grid[y][x]=1
    grid[start[1]][start[0]]=0
    grid[goal[1]][goal[0]]=0
    return grid