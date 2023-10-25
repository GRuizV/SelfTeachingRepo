# wieghted graph implementation using adjacency matrix


class WAMGraph:

    def __init__(self, num_vertices, undir = True):

        self.num_vertices = num_vertices
        self.graph = [[0 for _ in range(num_vertices)] for _ in range(num_vertices)]
        self.undir = undir

    def __iter__(self):
        yield from [vtx_list for vtx_list in self.graph]

    def __str__(self):

        res = ''
        idx = 0

        for vtx in self.graph:
            res += f'{idx} -> {' '.join(map(str, vtx))} \n'
            idx += 1

        return res



    def add_edge(self, vtx1, vtx2, weight):

        if 0 <= vtx1 < self.num_vertices and 0 <= vtx2 < self.num_vertices:
            self.graph[vtx1][vtx2] = weight

            if self.undir:
                self.graph[vtx2][vtx1] = weight

    def add_vertex(self):

        self.num_vertices += 1

        for vtx in self.graph:
            vtx.append(0)
        
        self.graph.append([0]*self.num_vertices)

    def remove_edge(self, vtx1, vtx2):

        if 0 <= vtx1 < self.num_vertices and 0 <= vtx2 < self.num_vertices:
            self.graph[vtx1][vtx2] = 0

            if self.undir:
                self.graph[vtx2][vtx1] = 0






class WALGraph:

    def __init__(self, undir=True):

        self.graph = dict()
        self.undir = undir

    def __str__(self):
        
        res = ''

        for vtx, neighbors in self.graph.items():
            res += f'{vtx} -> {neighbors} \n'
        
        return res




    def add_vertex(self, vtx1):

        if vtx1 not in self.graph:
            self.graph[vtx1] = list()

    def add_edge(self, vtx1, vtx2, weight):

        if vtx2 not in self.graph[vtx1]:
            self.graph[vtx1].append((vtx2, weight))
        
            if self.undir and vtx1 not in self.graph[vtx2]:
                self.graph[vtx2].append((vtx1, weight))
    
    def remove_edge(self,vtx1,vtx2):

        if vtx1 in self.graph and vtx2 in self.graph:
            self.graph[vtx1] = [(vtx, w) for vtx, w in self.graph[vtx1] if vtx != vtx2 ]

            if self.undir:
                self.graph[vtx2] = [(vtx, w) for vtx, w in self.graph[vtx2] if vtx != vtx1 ]






class ALGraph:

    def __init__(self, undir=True):

        self.graph = dict()
        self.undir = undir

    def __str__(self):
        
        res = ''

        for vtx, neighbors in self.graph.items():
            res += f'{vtx} -> {neighbors} \n'
        
        return res



    def get_graph(self):
        return self.graph

    def add_vertex(self, vtx1):

        if vtx1 not in self.graph:
            self.graph[vtx1] = list()

    def add_edge(self, vtx1, vtx2):

        if vtx2 not in self.graph[vtx1]:
            self.graph[vtx1].append(vtx2)
        
            if self.undir and vtx1 not in self.graph[vtx2]:
                self.graph[vtx2].append(vtx1)
    
    def remove_edge(self,vtx1,vtx2):

        if vtx1 in self.graph and vtx2 in self.graph:
            self.graph[vtx1] = [vtx for vtx in self.graph[vtx1] if vtx != vtx2 ]

            if self.undir:
                self.graph[vtx2] = [vtx for vtx in self.graph[vtx2] if vtx != vtx1 ]
