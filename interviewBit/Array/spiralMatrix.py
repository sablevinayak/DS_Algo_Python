# https://www.interviewbit.com/problems/spiral-order-matrix-i/



def spiralMatrix(A):
    if len(A) == 1:
        return A[0]

    rowBegin = 0
    rowEnd = len(A) - 1

    columnBegin = 0
    columnEnd = len(A[0]) - 1

    ans = []

    while (rowBegin<=rowEnd and columnBegin<=columnEnd):
        for i in range(columnBegin, columnEnd+1):
            ans.append(A[rowBegin][i])
        rowBegin+=1

        for i in range(rowBegin, rowEnd+1):
            ans.append(A[i][columnEnd])
        columnEnd-=1

        if rowBegin<=rowEnd:
            for i in range(columnEnd, columnBegin-1, -1):
                ans.append(A[rowEnd][i])
            rowEnd-=1

        if columnBegin<=columnEnd:
            for i in range(rowEnd, rowBegin-1, -1):
                ans.append(A[i][columnBegin])
            columnBegin+=1
        
        return ans




input1 = [[1]]
input2 = [[1,2,3]]
input3 = [
        [1, 2],
        [3, 4],
        [5, 6]
        ]
input4 = [
        [1,2],
        [3,4]
        ]        

# print(spiralMatrix(input1))
# print(spiralMatrix(input2))
# print(spiralMatrix(input3))
print(spiralMatrix(input4))