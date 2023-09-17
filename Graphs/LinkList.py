class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.pre = None
        
class DLL:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__current = None

    def InsertNode(self,data):
        if self.__head is None:
            self.__head = Node(data)
        else:
            self.newNode = Node(data)
            self.__current = self.__head
            while self.__current.next is not None:
                self.__current = self.__current.next
            self.__current.next = self.newNode
            self.newNode.pre = self.__current
            self.end = self.newNode
            
    def display(self,order:int = 0):
        """
            Displays the LinkList in ascending or descending order
            default:0
        Args:
            order (int):  0:ascending , 1:descending
        """
        if not order:
            if self.__head is None:
                return
            else:
                self.__current = self.__head
                print("Ascending:" ,end="\n")
                while self.__current is not None:
                    print(self.__current.data ,end=" ")
                    self.__current = self.__current.next
        else:
            if self.end is None:
                return
            else:
                self.__current = self.end
                print("Descending:" ,end="\n")
                while self.__current is not None:
                    print(self.__current.data ,end=" ")
                    self.__current = self.__current.pre
                    
        




    