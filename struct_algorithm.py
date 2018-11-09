import random
'''
随机法：依赖随机数的统计特性
    快排：一堆支票，选定一个中间值，将小于中间值的支票放一堆，将大于中间值的放另一堆。以同样的方式对以上两堆支票处理
    中间值的选取很重要，通常采用随机数。
'''

def __quick_sort__(first, end, data):
    mid_pos= (first + end) // 2
    mid_data = data[mid_pos]
    if first == end:
        return
    __first = first
    __end = end
    while __first < __end:
        while __first < mid_pos:
            if __first > mid_data:
                break
            else:
                __first -= 1
        data[mid], data[__first] = data[__first], data[mid]
        while __end > mid_pos:
            if __end < mid_data:
                break
            else:
                __end -=1
        data[mid_pos], data[__end] = data[__end], data[mid_pos]
    __quick_sort__(first, mid_pos, data)
    __quick_sort__(mid_pos, end, data)
    
def quick_sort(data):
    if isinstance(data, list):
        __quick_sort__(0, len(data)-1, data)

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


