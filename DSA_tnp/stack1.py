class stack:
    def __init__(self,maxsize):
        self.__maxsize=maxsize
        self.__elements=[None]*self.__maxsize
        self.__top=-1

    def is_full(self):
        if self.__top==self.__maxsize-1:
            return True 
        else:
            return False
    def isempty(self):
        if self.__top==-1:
            return True
        return False
    def push(self,data):
        if self.is_full():
            print('the stack is full')
        else:
            self.__top+=1
            self.__elements[self.__top]=data
        
            
