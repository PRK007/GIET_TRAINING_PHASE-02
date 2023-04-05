class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Linkedlist:
    def __init__(self):
        self.head=None

    def isempty(self):
        if self.head==None:
            return True
        return False
    def insertatstrt(self):
        newnode=node(data)
        if self.isempty():
            self.head=newnode
        else:
            newnode.next=self.head
            self.head=newnode

    def insertatend(self):
        newnode=node(data)
        if self.isempty():
            self.head=newnode
        else:
            h=self.head
            while h.next is not None:
                h=h.next
            h.next=newnode

    def  insertatmid(self):
               

