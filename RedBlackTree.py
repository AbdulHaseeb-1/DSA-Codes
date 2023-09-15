from termcolor import colored
class Node:
    def __init__(self,data:int):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None
        self.color = 1
    

class RedBlackTree:
    def __init__(self):
        self.nullNode = Node(0)
        self.nullNode.color = 0
        self.root = self.nullNode
            
        
    def rotate_left(self, node):
            pass
        
        
    def rotate_right(self, node):
            pass
        
        
        
    def fix_insert(self,node):  
        while node.parent.color == 1:
            if node.parent.parent.right == node.parent:
                uncle = node.parent.parent.left 
                if uncle.color == 1:
                    node.parent.parent.color = 1
                    uncle.color = 0
                    node.parent.color = 0
                else:
                    if node.parent.left == node:
                        node = node.parent
                        self.rotateRight(node)
                        
                    node.parent.color = 0
                    node.parent.parent.color = 1           
                    self.rotateLeft(node.parent.parent)
            else:
                uncle = node.parent.parent.right 
                if uncle.color == 1:
                    node.parent.parent.color = 1
                    uncle.color = 0
                    node.parent.color = 0
                else:
                    if node.parent.right == node:
                        node = node.parent
                        self.rotateLeft(node)
                        
                    node.parent.color = 0
                    node.parent.parent.color = 1           
                    self.rotateRight(node.parent.parent)       
        self.root.color = 0
                    
    
    def insertNode(self,data):
        self.node = Node(data)
        self.node.left = self.nullNode
        self.node.right = self.nullNode
        
        y = None
        x = self.root
        
        while x != self.nullNode:
            y = x
            if self.node.data > x.data:
                x = x.right
            else:
                x = x.left
            
        self.node.parent = y
        if self.node.parent == None:
            self.root = self.node
        elif self.node.data > y.data:
            y.right = self.node
        else:
            y.left = self.node
             
        if self.node.parent is None:
            self.node.color = 0
            return 
        if self.node.parent.parent is None:
            return 
        
        self.fix_insert(self.node)
            
        
if __name__ == "__main__":
    rbt = RedBlackTree()
    rbt.insertNode(19)
    rbt.insertNode(12)
    rbt.insertNode(20)
    rbt.insertNode(10)
    rbt.insertNode(15)
    rbt.insertNode(1)
  