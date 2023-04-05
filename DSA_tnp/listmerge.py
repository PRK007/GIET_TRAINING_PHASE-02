list1=['A','app','a','d','ke','th','doc','awa']
list2=['y','tor','e','eps','ay',None,'le','n']

list2.reverse()
for i in range(0,len(list1)):
    if list2[i]==None:
        print(list1[i]+" ",end=' ')
    else:
        print(list1[i]+list2[i],end=' ')
    
        
