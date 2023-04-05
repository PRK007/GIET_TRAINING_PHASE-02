#implementation of stack using list

'''stack=[]
stack.append('a')
stack.append('b')
stack.append('c')
print(stack)
stack.pop()
stack.pop()
print(stack)'''


class Stack():
    def __init__(self):
        self.stack=[]
#push operation in stack
    def add(self,dataval):
        if dataval not in self.stack:
            stack.append(dataval)
            
            return True
        else:
            
            return False
        
    
# pop operation in stack
    def remove(self):
        
        if len(self.stack)<=0:
             
            return ('no element to remove')
        else:
            return self.stack.pop()

#displaying the elements in the stack

    '''def display(self):
        if len(self.stack)<=0:
                return 'stack is empty'
        else:
            for val in self.stack:
                print(*self.stack)'''



s=Stack()
s.add(2)
s.add(4)
s.add(3)

             
