# given a queue that returns the evenly divisible numbers (1,10)
class queue:
    def __init__(self,maxsize):
        self.maxsize=maxsize
        self.elements=[None]*self.maxsize
        self.rear=-1
        self.front=0

    def is_full(self):
        if self.rear==self.maxsize-1:
            print(' the queue is full')
        return False
    def is_empty(self):
        if self.front>self.rear:
            return True
        return False
    def enqueue(self,data):
        if self.is_full():
            print(' queue is full')
        else:
            self.rear+=1
            self.elements[self.rear]=data

    def dequeue(self):
        if self.is_empty():
            print('queue is empty')
        else:
            data=self.elements[self._front]
            self.front+=1
            return data
    def display(self):
        for ind in range(self.front,self.rear+1):
            res=1
            for k in range(1,11):
                if q1.elements[ind]%k!=0:
                    res=0
                    break
            if res==1:
                print(q1.elements[ind])
            

    def maxsize(self):
        return self.maxsize





q1=queue(5)
q1.enqueue(13983)
q1.enqueue(10080)
q1.enqueue(7113)
q1.enqueue(2520)
q1.enqueue(2500)
q1.display()

'''s=q1.front
e=q1.rear
for i in range(s,e):
    res=1
    for k in range(1,11):
        if q1.elements[i]%k!=0:
            res=0
            break
    if res==1:
        print(q1.elements[i])'''
    









    








                         
            
        
