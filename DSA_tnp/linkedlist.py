#traversing a linked list


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


class Slinkedlist:
    def __init__(self):
        self.head=None
    def listprint(self):
        printval=self.head
        while printval is not None:
            print(printval.data)
            printval=printval.next



list=Slinkedlist()
list.head=Node('mon')
e1='tue'
e2='wed'
head.data.next=e1
    
