from util import Stack, Queue  # These may come in handy

class Graph():

    # This is all you need to build a simple graph
    def __init__(self):
        # create a dictionary(hashtable) to hold the vertices of the graph
        self.vertices = {}

    def add_vertex(self, vertex_id):
        # create an empty set to hold vertices
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        # add an edge value to the set in each vertex
        self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        # function to calculate all edges of a vertex
        return self.vertices[vertex_id]


    # Write a function within your Graph class that takes takes a starting node as an argument, then performs BFT.
    # The breadth-first method tries its best to stay as close to the top as possible. 
    # It traverses the tree one row at a time and looks at all of its the sibling nodes. 
    # It continues this until it reaches the last row.
    def bft(self, starting_vertex):
        # Create the queue, Breadth first Traversal requires a Queue
        q = Queue()
        # Enqueue the starting node
        q.enqueue(starting_vertex)

        # Use empty set to hold the nodes that have been visited
        visited = set()

        # run a loop while the queue still has items
        # While the queue is not empty
        while q.size() > 0: # base case

            # dequeue the first item and store it in a variable
            # Dequeue who is at the front 
            dq = q.dequeue() # I.E (3)

            # check if the node has already been visited or not
            if dq not in visited: # Has 3 been visited?
                # if not, print it and 
                # add it to the set
                print(dq)
                visited.add(dq)
                # Check for neighbors, if neighbors then enqueue 
                # Add neighbors to queue line 
                for next_vert in self.get_neighbors(dq): # Does 3 have neighbors? If so then Enqueue 
                    # enqueue new vertices for all the neighbors
                    q.enqueue(next_vert)


    # Run Time Complexity = O(n) Linear 
    # Add up nodes, Add Up Connections
    def dft(self, starting_vertex):
        # Create the stack, Depth First Traversal require Stacks
        stack = Stack()

        # push the starting node
        stack.push(starting_vertex)
        # create an empty set to hold the nodes that have been visited
        visited = set()

        # run a loop while the stack still has items
        while stack.size() > 0:

            # pop the first item and store it in a variable
            pop = stack.pop() #i.e (3)

            # check if the node has already been visited or not
            if pop not in visited: # I.E Has 3 been visited?
                # if not, print it and 
                # add it to the set
                print(pop)
                visited.add(pop)
                
                # Iterate through neighbors of pop I.E (3) get_neighbors(3)
                # Checking the 'Edges' 
                for next_vert in self.get_neighbors(pop): # I.E Get neighbors of 3
                    # push new vertices for all the neighbors
                    stack.push(next_vert)

    def dft_recursive(self, starting_vertex, visited = None):
        # create the base case
        # if vertex hasnt been visited, create a new set, add the starting vertex
        if not visited:
            visited = set()
        visited.add(starting_vertex)
        print(starting_vertex)

        # loop through all the vertices,
        # and if it hasn't been visited, recursively call DFT
        for vert in self.vertices[starting_vertex]:
            if vert not in visited:
                self.dft_recursive(vert, visited)

    def bfs(self, starting_vertex, destination_vertex):
        # Breadth First can find shortest path
        # create the queue, breadth first traversal requires a queue
        # enqueue the starting vertex in a list 
        # create the visited set to keep track of visited nodes
        q = Queue()
        q.enqueue([starting_vertex])
        visited = set()

        # while the queue still has items
        while q.size() > 0:
            # grab the first item in the queue
            path = q.dequeue()
            # and grab the vertex from the last index in the path
            vert = path[-1]

            # if the vertex hasn't been visited
            if vert not in visited:

                # if the vertex equals our destination value,
                # return the path, we have our answer
                if vert == destination_vertex:
                    return path

                # else add the vertex to visited
                visited.add(vert)

                # loop through all remaining neighbors and
                # create a copy of the path,
                # append the new vertex for all neighbors to the path,
                # and enqueue the new paths
                for next_vert in self.get_neighbors(vert):
                    path_copy = list(path)
                    path_copy.append(next_vert)
                    q.enqueue(path_copy)

        # if we get here, there was no path from start to destination
        return None


    def dfs(self, starting_vertex, destination_vertex):
        # create the stack Depth First Traversal requires a stack
        # push the starting vertex in a list to mark its traveled path
        # create a visited set to keep track of visited nodes
        s = Stack()
        s.push([starting_vertex])
        visited = set()

        # while the stack still has items
        while s.size() > 0:
            # grab the first item in the stack
            path = s.pop()
            # and grab the vertex from the last index in the path
            vert = path[-1]

            # if the vertex hasn't been visited
            if vert not in visited:

                # if the vertex equals our destination value,
                # return the path, we have our answer
                if vert == destination_vertex:
                    return path

                # else add the vertex to visited
                visited.add(vert)

                # loop through all remaining neighbors and
                # create a copy of the path,
                # append the new vertex for all neighbors to the path,
                # and push the new paths
                for next_vert in self.get_neighbors(vert):
                    path_copy = list(path)
                    path_copy.append(next_vert)
                    s.push(path_copy)

        # if we get here, there was no path from start to destination
        return None

    def dfs_recursive(self, starting_vertex, destination_vertex, visited = None, path = None):
        # You can only use recusrive with Depth First 
        # create the base case
        # if the visited set and the path list are None
        # create new set and path
        # else use the set and path passed in as parameters
        if not visited:
            visited = set()
        if not path:
            path = []

        # add starting vertex to the visited set
        # and add the vertex passed in to any vertices already in the list
        visited.add(starting_vertex)
        path = path + [starting_vertex]

        # if the starting vertex and the destination are the same, return the path
        if starting_vertex == destination_vertex:
            return path

        # else loop through all remaining vertices,
        # if the vertex hasn't been visited,
        # call dfs recursive and if there is a path,
        # return it
        for vert in self.vertices[starting_vertex]:
            if vert not in visited:
                path_copy = self.dfs_recursive(vert, destination_vertex, visited, path)
                if path_copy:
                    return path_copy

        # if we get here, there was no path so return None 
        return None

     
     # We need a Depth First Search to return the longest path to find the ancestor
    def find_earliest_ancestor(self, start):
        # once again we create a stack
        s = Stack()

        # push the starting vertex(node) to the stack
        # create the visited set to keep track of the visited nodes
        # create the path to hold the longest path 
        s.push([start])
        visited = set()
        path = [start]

        # check stack, while the stack still holds items
        while s.size() > 0:
            # create an inner path by popping a value from the stack
            inner_path = s.pop()
            vert = inner_path[-1] # grab the vertex from the last index of the list

            # if the vertex hasn't been visited,
            # add it to the set
            if vert not in visited:
                visited.add(vert)

                # loop through all remaining neighbors
                # create copy of inner path
                # append the vertex to the copy
                # push the path copy to the stack for all neighbors
                for next_vert in self.get_neighbors(vert):
                    path_copy = list(inner_path) # you want to make a new copy each time
                    # copy path so we dont mutate the original path 
                    path_copy.append(next_vert) # copy append neighbor, make new copy for each neighbor

                    s.push(path_copy) # push copy to the stack 

                    # if the path copy and the longest path contain the same number of values
                    # set the longest path equal to the path copy
                    if len(path_copy) > len(path):
                        path = path_copy

                    # if the paths lengths are equal, and the last elements of the lists are different,
                    # set the longest path equal to the path copy
                    if len(path_copy) == len(path) and path_copy[-1] != path[-1]:
                        path = path_copy

        # return the resulting path
        return path    

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
    print(graph.vertices)

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
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))