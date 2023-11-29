grid=[ [0,0,0,0,0,0,0,0,0]
         ,[0,0,0,0,0,0,0,0,0]
         ,[0,0,0,0,0,0,0,0,0]
         ,[0,0,0,0,0,0,0,0,0]
         ,[0,0,0,0,0,0,0,0,0]
         ,[0,0,0,0,0,0,0,0,0]
         ,[0,0,0,0,0,0,0,0,0]
         ,[0,0,0,0,0,0,0,0,0]]

def checkvalid(row, col, number,problem):
    for i in range(10):

        #rows check
        if number ==problem[row][i]:
            return False
    
        #column check
        if number ==problem[i][col]:
            return False
    

        #cube check

    i=row//3 *3
    j=col//3*3
    for a in range(i,i+4):
        for b in range(j,j+4):
            if problem[a][b]==number:
                return False
    return True            



def lopp(problem):
    for i in range(10):
        for j in range(10):

            for numb in range(1,10):
                if checkvalid(i,j,numb,problem) == True:
                    problem[i][j]=numb
                else:
                    problem[i][j]=0



lopp(grid)

print(grid)


