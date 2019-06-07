'''
快速排序使用分治法策略来把一个序列分为两个子序列
步骤:
1.从数列中挑出一个元素, 称为'基准'(pivot)
2.重新排序数列,所有元素比基准值小的摆在基准前面,所有元素比基准值大的摆在基准的后面
在这个分区结束后, 该基准就处于数列的中间位置,这个称为分区操作
3.递归把小于基准值元素的子数列和大于基准值元素的子数列排序
'''
def quick_sort(list):
    less = []
    pivotList = []
    more = []
    if len(list) <= 1:
        return list
    else:
        # 将第一个值作为基准值
        pivot = list[0]
        for i in list:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                more.append(i)
            else:
                pivotList.append(i)

        less = quick_sort(less)
        more = quick_sort(more)
        return less + pivotList + more

# 第二种方法
def qsort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        return qsort([x for x in arr[1:] if x < pivot]) + \
            [pivot] + \
                qsort([x for x in arr[1:]if x >= pivot])
