#example
import random

class question_01
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

    def test_result():
        ll = [[10000000 for i in range(10)] for j in range(5)]
        computer_distance(ll, (3, 3), (4, 4))
        print_matrix(ll)


class diffStr:
    def __init__(self, lstr, rstr):
        self.lmaxQue = []
        self.rmaxQue = []
        self.lstr = lstr
        self.rstr = rstr
        self.buildTable(lstr, rstr)

        ldmaxQue = [i for i in range(len(lstr)) if i not in self.lmaxQue]
        rdmaxQue = [i for i in range(len(rstr)) if i not in self.rmaxQue]
     
        self.lscque = self.compressQue(self.lmaxQue)
        self.rscque = self.compressQue(self.rmaxQue)

        self.ldcque = self.compressQue(ldmaxQue)
        self.rdcque = self.compressQue(rdmaxQue)

        for i in self.ldcque:
            print(i[0], i[1])
            print(lstr[i[0]:i[1]])
        print("diff str2:")
        for i in self.rdcque:
            print(i[0], i[1])
            print(rstr[i[0]:i[1]])
        
        
    def buildTable(self, lstr, rstr):
        llen = len(lstr)
        rlen = len(rstr)

        table = [[0 for j in range(rlen+1)] for i in range(llen+1)]
        for i in range(llen):
            for j in range(rlen):
                if lstr[i] == rstr[j]:
                    table[i+1][j+1] = table[i][j]+1
                else:
                    table[i+1][j+1] = max(table[i+1][j], table[i][j+1])

        while (llen!=0) and (rlen!=0):
            vmax = max(table[llen-1][rlen], table[llen][rlen-1])
            if table[llen][rlen] != vmax:
                llen-=1
                rlen-=1
                self.lmaxQue.insert(0, llen)
                self.rmaxQue.insert(0, rlen)
            else:
                if vmax == table[llen-1][rlen]:
                    llen-=1
                else:
                    rlen-=1
    def compressQue(self, que):
        if len(que)==0:
            return []
        ret = [[que[0], que[0]+1]]
        for i in range(1, len(que)):
            if que[i] - que[i-1] != 1:
                ret.append([que[i], que[i]+1])                
            else:
                ret[-1][1]+=1
        return ret
    
    def test_result():
        f = open('1.txt', 'rt')
        str1 = f.read()
        f.close()

        f = open('2.txt', 'rt')
        str2 = f.read()
        f.close()
        #str1 = '0123456789qwertyuiop'
        #str2 = '34567890ertyuiopasdfghjk'
        diffStr(str1.split('\n'), str2.split('\n'))

