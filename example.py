#example
import random
'''
给定一个矩阵，给一组京东储物柜的位置，求矩阵所有点距离最近储物柜的距离（只计算水平与垂直距离）：
例如：储物柜Point(1, 1)     例如：储物柜Point(1, 1) Point(0, 0)
结果矩阵：                  结果矩阵：
2 1 2                     0 1 2
1 0 1                     1 0 1
2 1 2                     2 1 2
'''

def print_matrix(matrix):
    for l in matrix:
        line = ''
        for it in l:
            line = "%s%d\t" %(line, it)
        print(line)

def computer_distance_one(matrix, point):
    row_count = len(matrix)
    col_count = len(matrix[0])
    for row in range(row_count):
        for col in range(col_count):
            cur_distance = abs(point[0]-row) + abs(point[1] - col)
            matrix[row][col] = min(cur_distance, matrix[row][col])

def computer_distance(matrix, *points):
    #first = random.randint(0, len(points))
    #del points[first]
    #computer_distance_one(matrix, points[first])
    for pt in points:
        computer_distance_one(matrix, pt)
        pass
        
def vector_cross(ll, rl):
    vlen = len(ll)
    


ll = [[10000000 for i in range(10)] for j in range(5)]
computer_distance(ll, (3, 3), (4, 4))
print_matrix(ll)

