from room import Room
from player import Player
from world import World
from util import Stack, Queue
import random
from ast import literal_eval

# Load world
world = World()

#Why cant we just use traversal?
#Traversal will just visit all of the nodes
# We want a list of directions to guide us 
# We also want to minimize the number of steps

# We need to keep track of where we have been
# Write a traversal algorithm that logs the path into `traversal_path`

### 3 Steps 
## User Graphs Terminology - What are our nodes? What are our Edges?
### Build the Graph or get_neighbors
#### Choose the algorithm best suited for this problem 

# These are your Map of Rooms to traverse
# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print map
world.print_rooms()
visited_rooms = set() # Create set of all the rooms we visit during traversal 
player = Player(world.starting_room) # create player for starting 

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

# Add current room to rooms visited 
visited_rooms.add(player.current_room)

# Step 1. Create the Breadth First Traversal 
#returns a shortest path to a room that has not been explored yet
def room_bft(current_room, total_traversed, world):
    q = Queue() # Create our Queue 
    q.enqueue([('n', current_room.id)]) # Enqueue the starting vertex with its direction
    visited_rooms = set() # Set for Visited rooms, add to set if visited 
    visited_rooms.add(current_room.id) # Add to Our Visit 
    while q.size() > 0: # While the Queue is not empty 
        curr_path = q.dequeue() # we need to create the current path = to Dequeue  
        curr_room_pair = curr_path[-1] # grab last vertext from path
        curr_room = world.rooms[curr_room_pair[1]]
         
        # Iterate through the room exits 
        for direction in curr_room.get_exits():
            # Check if the current rooms neighbor is not in total rooms traversed 
            if curr_room.get_room_in_direction(direction) not in total_traversed:
                # Add room with direction
                curr_path.append((direction, curr_room.get_room_in_direction(direction).id))
                return curr_path
            # check if current rooms neighbor id is in visited rooms     
            elif curr_room.get_room_in_direction(direction).id not in visited_rooms:
                # create new room 
                new_room = curr_room.get_room_in_direction(direction)
                # create new path so we dont mutate the original 
                new_path = curr_path.copy()
                # Add room with direction & Id
                new_path.append((direction, new_room.id))
                # Add to visited 
                visited_rooms.add(new_room.id)
                # Enqueue 
                q.enqueue(new_path)        

 # we need to find unexplored areas 
 # while the length of visted rooms is not equal to the total rooms
while(len(visited_rooms) != len(room_graph)):
    # get the exits of the current player 
     current_exits = player.current_room.get_exits()
     # create boolean indicator
     found_unexplored_exit = False
     # iterate through all the current exits 
     # in iteration, check if the players room directions arent in visted rooms
     for direction in current_exits:
         # Check if any neighbors havent been visited 
         if player.current_room.get_room_in_direction(direction) not in visited_rooms:  
             # travel to that direction          
             player.travel(direction)
             # Add that room to visted rooms
             visited_rooms.add(player.current_room)
             # Add the direction to  traversal path
             traversal_path.append(direction)
             # Set the indicator boolean to true
             found_unexplored_exit = True
             # Exit 
             break
     if found_unexplored_exit:
         continue
     
     # Neighbor Rooms have all been visted now find shortest path 
     path = room_bft(player.current_room, visited_rooms, world)
     # iterate through the range of path 
     for i in range(1, len(path)):
         # create list with room_bft
         dir = path[i][0]
         player.travel(dir)
         traversal_path.append(dir)
     visited_rooms.add(player.current_room)





## Dont Touch 
# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
#player.current_room.print_room_description(player)
#while True:
#    cmds = input("-> ").lower().split(" ")
#    if cmds[0] in ["n", "s", "e", "w"]:
#        player.travel(cmds[0], True)
#    elif cmds[0] == "q":
#        break
#    else:
#        print("I did not understand that command.")
