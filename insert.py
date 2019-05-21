'''插入排序 python'''
m_list = [1, 9, 8, 5, 6, 7, 4, 3, 2]
nums = [0] + m_list
print(nums[1:])
length = len(nums)
count_move = 0
for i in range(2, length):
    nums[0] = nums[i]
    j = i - 1
    if nums[j] > nums[0]:
        while nums[j] > nums[0]:
            nums[j+1] = nums[j]
            j -= 1
            count_move += 1
        nums[j+1] = nums[0]
print(nums[1:])
