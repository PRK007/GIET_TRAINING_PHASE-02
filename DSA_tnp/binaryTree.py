class Node:
    def __init__(self,item):
        self.right=None
        self.left=None
        self.val=item

def inorder(root):
    if root:
        inorder(root.left)
        print(str(root.val)+'->',end='')
        inorder(root.right)
def preorder(root):
    if root:
        print(str(root.val)+'->',end='')
        preorder(root.left)
        preorder(root.right)
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(str(root.val)+'->',end='')


n1=Node(1)
n1.left=Node(2)
n1.right=Node(3)
n1.left.left=Node(4)
n1.left.right=Node(5)
postorder(n1)
        
    
