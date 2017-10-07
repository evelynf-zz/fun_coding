# Complete the function below.
#find all paths in a matrix that go through 1 on grid. if 0, can't go through path   
def find_path(grid, parent, visited):
    num_paths = 0
    num_rows = len(grid)
    num_columns = len(grid[0])
    (x,y) = parent
    if x == num_columns - 1 and y == num_rows - 1:
        return 1
    #check if in graph range
    if x < 0 or x >= num_columns or y < 0 or y >= num_rows:
        #out of range
        return 0
    if grid[y][x] == 1:
        children = [(x+1,y), (x, y+1)]
        for child in children:
            if child not in visited:
                visited[child] = find_path(grid, child, visited)
            num_paths += visited[child]
    print visited      
    return num_paths

def  numberOfPaths(a):
     return find_path(a, (0,0), {})