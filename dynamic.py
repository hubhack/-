'''求两个字符串的最长公共子串'''
# 用动态规划算法 先构建出一个二维数组 , 之后求解
s1 = 'abcdefg'
s2 = 'defabcdd'
def findit(str1, str2):
    length1 = len(str1)
    length2 = len(str2)
    matrix = [[0]*length1 for i in range(length2)]
    xmax = 0
    xindex = 0
    for i, x in enumerate(str2):
        for j, y in enumerate(str1):
            if x != y:
                pass
            else:
                if i == 0 or j == 0:
                    matrix[i][j] = 1
                else:
                    matrix[i][j] = matrix[i-1][j-1] + 1
                if matrix[i][j] > xmax:
                    xmax = matrix[i][j]
                    xindex = j
    start = xindex + 1 -xmax
    end = xindex + 1
    return str1[start:end]
print(findit(s1, s2))
