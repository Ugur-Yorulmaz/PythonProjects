#
# # 54. Spiral Matrix
matrix = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
# matrix = [[1,2,3,4,5,6],[7,8,9,10,11,12],[13,14,15,16,17,18],[19,20,21,22,23,24]]
# matrix=[[1],[2],[3]]

res=[]
while len(matrix)!=0 and len(matrix[0])!=0:

    for j in range(len(matrix[0])):
        print("j",j)
        res.append(matrix[0][j])
    del matrix[0]

    print("Matrix-0",matrix,res)

    for i in range(len(matrix)):
        res.append(matrix[i][len(matrix[i])-1])
        del matrix[i][len(matrix[i])-1]
    print("Matrix-1",matrix,res)

    for j in range(len(matrix[0])-1,-1,-1):
        print(matrix[len(matrix)-1],[j],matrix[len(matrix)-1][j])
        res.append(matrix[len(matrix)-1][j])
    del matrix[len(matrix)-1]
    print("Matrix-2",matrix,res)


    for i in range(len(matrix)-1,-1,-1):
        # res.append(matrix[len(matrix)-1][i])
        res.append(matrix[i][0])
        del matrix[i][0]
    print("Matrix-3",matrix,res)


