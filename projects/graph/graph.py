"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.
        """
        # TODO
        self.vertices[vertex] = set()


    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("that vertex does not exist")

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # TODO

        #Create an empy queue and enqueue the starting vertex ID
        q = Queue()
        q.enqueue(starting_vertex)
        #Create an empty Set to store visited vertices
        visited = set()
        #While the queue is not empty...
        while q.size() > 0:
            #Dequeue the first vertex
            v = q.dequeue()
            #If that vertex has not been visited...
            if v not in visited:
                #Mark it as visited
                print(v)
                visited.add(v)
                #Then add all of its neighbors to the back of the queue
                for neigbor in self.vertices[v]:
                    q.enqueue(neigbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create an empty stack and push the starting vertex ID
        s = Stack()
        print(f"{self.vertices} vertices")
        s.push(starting_vertex)
        # Create a Set to store visited vertices
        visited = set()
        # While the stack is not empty...
        while s.size() > 0:
            # Pop the first vertex
            v = s.pop()
            # If that vertex has not been visited...
            if v not in visited:
                # Mark it as visited...
                print(v)
                visited.add(v)
                # Then add all of its neighbors to the top of the stack
                for i in self.vertices[v]:
                    s.push(i)


    def dft_recursive(self, starting_vertex,visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        # TODO

        if visited is None:
            visited = set()

        visited.add(starting_vertex)
        print(starting_vertex)

        for next in self.vertices[starting_vertex]:

            if next not in visited:
                self.dft_recursive(next,visited)


        # v =set()
        #
        # if starting_vertex in v:
        #     print(v)
        #     return v
        #
        # else:
        #     v.add(starting_vertex)
        #     for neigbors in self.vertices[starting_vertex]:
        #         self.dft_recursive(neigbors)
        #     print(v)







    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # TODO
        #Created an empty Queue
        q = Queue()

        #Put an array with Starting Vertex in the front of the Queue
        q.enqueue([starting_vertex])

        #created a set to check for visited nodes and called it visited
        visited = set()

        #loop through queue as long as q's size is greater then 0
        while q.size() > 0:

            #Pull the array out of queue and calling it 'path'
            path = q.dequeue()

            #Grabbing the last index of the array to check when array becomes larger then 1
            vertex = path[-1]

            #Checking if last index called "vertex" has been visited
            if vertex not in visited:
                visited.add(vertex)

            #Checks to see if the vertex has hit its Target.
            if vertex == destination_vertex:
                #if so then return the array of vertices
                return path

            # loop through connecting nodes
            for neighbor in self.vertices[vertex]:

                 #create a copy of path array
                 path_add = path.copy()

                 #add the vertexs to the back of array
                 path_add.append(neighbor)

                 #add path_add to queue to loop through again
                 q.enqueue(path_add)


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        """
        # TODO
        s = Stack()

        visited = set()

        s.push([starting_vertex])

        while s.size() > 0:

            path = s.pop()

            vertex = path[-1]

            if vertex not in visited:
                visited.add(vertex)

            if vertex == destination_vertex:
                return path

            for neighbor in self.vertices[vertex]:

                 #create a copy of path array
                 path_add = path.copy()

                 #add the vertexs to the back of array
                 path_add.append(neighbor)

                 #add path_add to queue to loop through again
                 s.push(path_add)









if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    # print(graph.vertices)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    # graph.dft(1)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    # graph.bft(1)

    '''
    Valid DFT recursive paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    # print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    # print(graph.dfs(1, 6))
