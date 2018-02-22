
def triplets( list ):
    res = []
    for i in range(len(list)):
        for j in range(i + 1, len(list)):
            for k in range(j + 1, len(list)):
                if (list[i] + list[j] + list[k] == 0):
                    res.append( [list[i], list[j], list[k]] )
    print(res)


triplets( [1 , 3, 6, 2 , -1, 2, 8, -2 ,9, -7] )
        
        
