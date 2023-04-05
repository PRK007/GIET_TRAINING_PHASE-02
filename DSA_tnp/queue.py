class queue:
    def __init__(self,maxsize):
        self.__maxsize=maxsize
        self.__elements=[None]*self.__maxsize
        self.__rear=-1
        self.__front=0

    def is_full(self):
        if self.__rear==self.__maxsize-1:
            print(' the queue is full')
        return False
    def is_empty(self):
        if self.__front>self.__rear:
            return True
        return False
    def enqueue(self,data):
        if self.is_full():
            print(' queue is full')
        else:
            self.__rear+=1
            self.__elements[self.__rear]=data

    def dequeue(self):
        if self.is_empty():
            print('queue is empty')
        else:
            data=self.__elements[self.__front]
            self.__front+=1
            return data
    def display(self):
        for ind in range(self.__front,self.__rear+1):
            print(self.__elements[ind])

    def maxsize(self):
        return self.__maxsize





q1=queue(5)
q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)
q1.display()
q1.dequeue()
q1.display()









    








                         
            
        
