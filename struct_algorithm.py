import random
'''
随机法：依赖随机数的统计特性
    快排：一堆支票，选定一个中间值，将小于中间值的支票放一堆，将大于中间值的放另一堆。以同样的方式对以上两堆支票处理
    中间值的选取很重要，通常采用随机数。
'''
def partition(data, first, end):
    mid_value = data[end]
    i = first-1
    for j in range(first, end):
        if data[j] <= mid_value:
            i += 1
            data[i], data[j] = data[j], data[i]
    data[i+1], data[end] = data[end], data[i+1]    
    return i+1

def __quick_sort(data, first, end):
    if first < end:
        mid = partition(data, first, end)
        __quick_sort(data, first, mid-1)
        __quick_sort(data, mid+1, end)
    
def quick_sort(data):
    '''
    参考算法导论
    '''
    if isinstance(data, list):
        __quick_sort(data, 0, len(data)-1)

'''
分治法 分解、求解、合并：
    例子：归并排序
'''



'''
动态规划：
    与分治法类似，但是分解后的子问题往往不独立，不能简单合并。（常见例子 斐波那契数列求解
    1.刻画一个最优解的结构特征
    2.递归的定义最优解的值
    3.计算最优解的值，通常采用自底向上的方法
    4.利用计算出来的信息构造一个最优解
    例子：最大公共子序列、斐波那契数列、钢条切割
    最大公共子序列 https://github.com/lipracer/diffFile.git 可以用于文件查分，最大子序列即为相同内容，其余为不同内容。
    考虑构建表格消耗大量内存，因此通常做法不是针对单个字符分割，而是按行分割，将一行文本作为序列的一个元素。
'''
'''
贪心算法：
    贪心算法，寻求局部最优解。（局部最优解并不一定是全局最优解）常见例子：Huffman编码，图结构中最短路径也是贪心算法，还有诸如马踏棋盘等。
    Huffman实现：https://github.com/lipracer/huffman.git
    最短路径算法：https://github.com/lipracer/searchGraph.git
    win32 api实现，可以设置障碍，寻求最短路径，通常用于游戏寻路算。算法效率比较低下！！！！
'''
'''
近似法：
    并不计算出最优解，因为问题本身很有价值，退而求其次。常见类型，推销员问题（尽可能选择最短的路线走遍要去所有城市），也是著名NP问题。
'''


mlist = [0, 2, 3, 5, 7, 8, 6, 1, 4, 9]
quick_sort(mlist)

'''
打印全排列
'''

def print_all_order(n):
    print(n)

'''
0 1 2
7 8 3
6 5 4
'''

def write_matrix(start, end, matrix):
    if start == end:
        return
    if start + 1 == end:
        matrix[start][start] = 0
        return
    '''
    写边长
    '''
    max_statr = (end - start) ** 2 - 1
    slide_length = end - start - 1
    for i in range(start, end - 1):
        matrix[start][i] = max_statr
        matrix[i][end - 1] = max_statr - slide_length
        matrix[end - 1][end - i + start - 1] = max_statr - 2 * slide_length
        matrix[end - i + start - 1][start] = max_statr - 3 * slide_length
        max_statr -= 1
    #print_result(matrix)
    write_matrix(start + 1, end - 1, matrix)
def print_result(matrix):
    for it in matrix:
        line = ''
        for i in it:
            line += str(i) + "\t"
        print(line)

def print_continue_matrix(n):
    result = [[0 for i in range(n)] for i in range(n)]
    write_matrix(0, n, result)
    print_result(result)
for i in range(10):
    print_continue_matrix(i)
    print('\n')
