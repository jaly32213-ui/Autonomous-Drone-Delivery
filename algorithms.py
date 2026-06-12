import heapq

def heuristic(a, b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])

def astar(grid, start, goal):
    open_list=[]
    heapq.heappush(open_list,(0,start))
    came_from={}
    g_score={start:0}
    f_score={start:heuristic(start,goal)}

    while open_list:
        _, current = heapq.heappop(open_list)
        if current==goal:
            path=[]
            while current in came_from:
                path.append(current)
                current=came_from[current]
            path.append(start)
            return path[::-1]

        x,y=current
        for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx,ny=x+dx,y+dy
            if 0<=nx<len(grid[0]) and 0<=ny<len(grid) and grid[ny][nx]==0:
                neighbor=(nx,ny)
                new_cost=g_score[current]+1
                if neighbor not in g_score or new_cost<g_score[neighbor]:
                    g_score[neighbor]=new_cost
                    f_score[neighbor]=new_cost+heuristic(neighbor,goal)
                    heapq.heappush(open_list,(f_score[neighbor],neighbor))
                    came_from[neighbor]=current
    return None