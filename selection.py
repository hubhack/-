'''
选择排序python实现

'''
m_list = [1, 9, 8, 5, 6, 7, 4, 3, 2]
nums = m_list
print(nums)
length = len(nums)
count_iter = 0
count_swap = 0
for i in range(length // 2):
    maxindex = i
    minindex = -i - 1
    minorigin = length + minindex
    for j in range(i+ 1, length - 1):
        count_iter += 1
        if nums[j] > nums[maxindex]:
            maxindex = j
        if nums[-j - 1] < nums[minindex]:
            minindex = - j - 1
    if nums[maxindex] == nums[minindex]:break
    minindex = length + minindex
    if i != maxindex:
        nums[i], nums[maxindex] = nums[maxindex], nums[i]
        count_iter += 1
        if i == minindex:
            minindex = maxindex
    if minindex != minorigin and nums[minorigin] != nums[minindex]:
        nums[minorigin], nums[minindex] = nums[minindex], nums[minorigin]
        count_swap += 1
print(nums, count_swap, count_iter)
