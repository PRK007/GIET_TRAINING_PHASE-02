class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Queue:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0

    def enqueue(self,data):
        Newnode=Node(data)
        if self.length==0:
            self.head=Newnode
            self.tail=Newnode
        else:
            self.tail.next=Newnode
            self.tail=Newnode
        self.length+=1


    def dequeue(self):
        if self.length==0:
            return None
        item=self.head
        self.head=self.head.next
        self.length-=1
        if self.length==0:
            self.tail=None
        item.next=None
        return item.data
    def front(self):
        if self.length==0:
            return 0
        return self.head.data
    def rear(self):
        if self.length==0:
            return 0
        return self.tail.data
    def size(self):
        if self.length==0:
            return 0
        return self.size
    
    # def display(self):
    #     if self.length==0:
    #         print('Queue is empty')

    #     print(self.head)    
    


q=Queue()
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
print(q.front())







        
                    