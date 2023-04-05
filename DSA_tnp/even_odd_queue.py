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
            data=self.elements[self.front]
            self.front+=1
            return data
    def display(self):
        if self.is_empty():
            print('Queue is empty')
        for ind in range(self.front,self.rear+1):
            print(self.elements[ind],end=" ")
        print()

    def maxsize(self):
        return self.maxsize
    

q=queue(7)
q1=queue(7)
q2=queue(7)
q.enqueue(2)   
q.enqueue(7) 
q.enqueue(9) 
q.enqueue(4) 
q.enqueue(6) 
q.enqueue(5) 
q.enqueue(10) 


for i in range(q.front,q.rear+1):
    if q.elements[i] %2==0:
        q1.enqueue(q.elements[i])
    else:
        q2.enqueue(q.elements[i])
        
q1.display()
q2.display()        






