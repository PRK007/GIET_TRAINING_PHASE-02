
class queue:
    def __init__(self,maxsize):
        self.maxsize=maxsize
        self.queue=[None]*self.maxsize
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
            self.queue[self.rear]=data

    def dequeue(self):
        if self.is_empty():
            print('queue is empty')
        else:
            data=self.queue[self._front]
            self.front+=1
            return data
    def display(self):
        for ind in range(self.front,self.rear+1):
            
        
                print(self.queue[ind])
            

    def max_size(self):
        return self.maxsize





q1=queue(2)
q2=queue(3)
q3=queue(q1.max_size()+q2.max_size())
q1.enqueue(1)
q1.enqueue(2)
q2.enqueue(10)
q2.enqueue(20)
q2.enqueue(30)
q3.display()






while q1.rear>=q1.front and q2.rear>=q2.front:
    q3.enqueue(q1.queue[q1.front])
    q3.enqueue(q2.queue[q2.front])
    q1.front+=1
    q2.front+=1


while(q1.front<=q1.rear):
    q3.enqueue(q2.queue[q2.front])
    q1.front+=1
while(q2.front<q2.rear):
    q3.enqueue(q2.queue[q2.front])
    q2.front+=1

q3.display() 


    












    


    









    








                         
            
        
