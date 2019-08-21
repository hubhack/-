'''
冒泡法python实现
'''
lst = [1, 3, 6, 2, 9]
def buddle(lst):
    length = len(lst)
    for i in range(length-1):
        for j in range(length-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j + 1] = lst[j+1], lst[j]
    print(lst)
buddle(lst)
