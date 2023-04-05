class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

    def takeinput():
        inputlist=[int(i) for i in input().split()]
        head=None
        for curr in inputlist:
            if curr==-1:
                break
            newnode=Node(curr)
            if head is None:
                head=newnode
            else:
                while curr.next is not None:
                    
                    curr=curr.next
                curr.next=newnode

        return head       
                    
