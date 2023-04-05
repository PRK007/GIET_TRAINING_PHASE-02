def linearsearch(n,x):
    for i in range(0,len(n)):
        
        if x==n[i]:
            return i
        
    return -1



n=[1,2,3,4,5,6,7]
x=7
print(linearsearch(n,x))

    
