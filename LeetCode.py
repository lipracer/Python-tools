#https://siddontang.gitbooks.io/leetcode-solution/content/array/remove_element.html

#Quest 1:
class Solution:
    def remove_element(A, n, elem):
        i = 0; j = 0
        return 0

Solution.remove_element([1,2,3], 3, 2)


def get_count(n):
    result = 0
    remain = n
    while remain > 1:
        if remain == 2:
            result += 1
            break
        result += remain // 3
        remain = remain // 3 + remain % 3
    print(result)
while True:
    n = input()
    n_ = int(n)
    if n_ == 0:
        break
    get_count(n_)


def get_array(data):
    result = set(data)
    result = list(result)
    result.sort()
    print(result)
    return result
get_array([11, 10, 20, 40, 32, 67, 40, 20, 89, 300, 400, 15])

def get_decimal(value):
    if value.lower.().startwith("0x"):
        
