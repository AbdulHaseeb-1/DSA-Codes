class Graph:
    def __init__(self,vertices):
        self.vertices = vertices
        self.adjacency_list = []
        self.adjacency_list = [[] for _ in range(self.vertices)]
        
    def InsertNode(self,From ,To):
        self.adjacency_list[From].append(To)
        self.adjacency_list[To].append(From)
      
    def print_graph(self):
        for v in range(len(self.adjacency_list)):
            print(f"{v} is connected to",[ _ for _ in self.adjacency_list[v]])
            
g = Graph(6)
g.InsertNode(1,2)
g.InsertNode(0,1)
g.InsertNode(3,2)
g.InsertNode(0,4)
g.InsertNode(0,3)

g.print_graph()


