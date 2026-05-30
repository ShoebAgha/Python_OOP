def SpiralMatrix(n):
    matrix = [['' for j in range(n)] for i in range(n)]
    top, bottom = 0, len(matrix)-1
    left, right = 0, len(matrix)-1
    element=0
    while top <= bottom and left <= right:

        for i in range(left, right +1):
            matrix[top][i]=element
            element+=1
        top+=1

        for i in range(top, bottom+1):
             matrix[i][right]=element
             element+=1
        right-=1

        if top <=bottom:
            for i in range(right, left-1,-1):
                matrix[bottom][i]=element
                element+=1
            bottom-=1

        if left<=right:
            for i in range(bottom,top-1,-1):
                matrix[i][left]=element
                element+=1
            left+=1
    return matrix

print(SpiralMatrix(3))
    

