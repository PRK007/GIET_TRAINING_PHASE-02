def binarysearch(n,x):
    strt=0
    end=len(n)-1
    while strt<=end:
        
        mid=(strt+end)//2
        if x==n[mid]:
            return mid
        elif x>n[mid]:
            strt=mid+1

        else:
            end=mid-1

    return -1

n=[1,2,3,4,5,6,7,8]
x=10
print(binarysearch(n,x))


        
        
        
    
