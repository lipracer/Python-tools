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
    归并排序
'''
'''
动态规划：
	与分治法类似，但是分解后的子问题往往不独立，不能简单合并。（常见例子 斐波那契数列求解）
'''
'''
贪心算法：
	贪心算法，寻求局部最优解。（局部最优解并不一定是全局最优解）常见例子：Huffman编码，图结构中最短路径也是贪心算法，还有诸如马踏棋盘等。
'''
'''
近似法：
	并不计算出最优解，因为问题本身很有价值，退而求其次。常见类型，推销员问题（尽可能选择最短的路线走遍要去所有城市），也是著名NP问题。
'''


mlist = [0, 2, 3, 5, 7, 8, 6, 1, 4, 9]
quick_sort(mlist)

print(mlist)


