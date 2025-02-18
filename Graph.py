class Graph:
    def __init__(self, adjency_list=None):
        if adjency_list is None:
            self.adjency_list = {}
        else:
            self.adjency_list = adjency_list

    def add_vertex(self, vertex):
        if vertex not in self.adjency_list:
            self.adjency_list[vertex] = []

    def add_edge(self, vertex1, vertex2):
        self.adjency_list[vertex1].append(vertex2)

    def get_neighbors(self, vertex ):
        return self.add_vertex.get(vertex, [])
    
    def print_graph(self):
        for vertex in self.adjency_list:
            neighbors = ", ".join(map(str, self.adjency_list[vertex]))
            print(f"{vertex}: {neighbors}")

graph = Graph()
graph.add_vertex("Spongebob")
graph.add_vertex("Patrick")
graph.add_vertex("Squidward")

graph.add_edge("Spongebob", "Patrick")
graph.add_edge("Spongebob", "Squidward")
graph.add_edge("Patrick", "Squidward")

graph.print_graph()
