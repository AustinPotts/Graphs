from graph import Graph

def earliest_ancestor(ancestors, starting_node):
    pass

# What traversal method would best be used?
# Since we want to go as deep as possible into the connections,
# A Depth First Traversal should be used 
# We can use Recursion in that case 


## PROBLEM SOLVING!!!!!!
# 1.) Describe the problem using Graph terminology 
# What are your nodes?
# When are nodes connected?
# What are your connected components?

# 2.) Build your Graph() or write your GetNeighbors(), Figure out how to get the nodes edges

# 3.) Choose your Algorithm 


 # create a new graph using the Graph class in graph.py
    graph = Graph()

    # iterate through every tuple of values being passed in
    for pair in ancestors:
        graph.add_vertex(pair[0]) # add vertices for all values
        graph.add_vertex(pair[1])

    # iterate through all tuples,
    # We need to iterate through the ancestors 
    for pair in ancestors:
        graph.add_edge(pair[1], pair[0]) # add an edge from value at index 0 to value at index 1

    # call the ancestor Depth First Search function on the graph class 
    ancestor = graph.find_earliest_ancestor(starting_node)

    # if the last value in the list is the starting node,
    # there is no earliest ancestor,
    # return -1 indicating failure
    if ancestor[-1] == starting_node:
        return -1
    # else return the last element from the list
    else:
        return ancestor[-1]




# What is our node? When does our node have a connection?
# Nodes are people 
# Nodes are connected when th



# For example, in this diagram and the sample input, 3 is a child of 1 and 2, and 5 is a child of 4
# Write a function that, given the dataset and the ID of an individual in the dataset, 
# returns their earliest known ancestor – the one at the farthest distance from the input individual


# Input of 6 would return 10 
# Input of 7 would return 4 


# 10
# /
#1   2   4  11
# \ /   / \ /
#  3   5   8
#   \ / \   \
#    6   7   9