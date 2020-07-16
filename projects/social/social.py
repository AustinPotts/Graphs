import random
from util import Queue, Stack

# extended social network = connected componenets

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            # print("WARNING: You cannot be friends with yourself")
            return False
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            # print("WARNING: Friendship already exists")
            return False
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)
        return True

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {} # nodes
        self.friendships = {} # edges
        
        # add users
        for i in range(num_users):
            self.add_user(f'User {i}')
            
        # Generate all possible friendships
        possible_friendships = []
        
        # Avoid dups by ensuring the first number is smaller than the second
        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id + 1):
                possible_friendships.append( (user_id, friend_id) )
                
        # shuffle all possible friendships # this uses fisher yates shuffle
        random.shuffle(possible_friendships) 
        
        # create friendships for the first x pairs of the list
        # x is determined by the formula: num_users * avg_friendships // 2
        # need to divide by 2 since each add_friendship() creates 2 friendships
        for i in range(num_users * avg_friendships // 2):
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])

    def populate_graph_2(self, num_users, avg_friendships):
        # Reset graph
        self.last_id = 0
        self.users = {} # nodes
        self.friendships = {} # edges

        # add users
        for i in range(num_users):
            self.add_user(f'User {i}')

        target_friendships = (num_users * avg_friendships) // 2
        total_friendships = 0

        while total_friendships < target_friendships:
            user_id = random.randint(1, self.last_id)
            friend_id = random.randint(1, self.last_id)
            if self.add_friendship(user_id, friend_id):
                total_friendships += 1

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        # Breadth First Traversal
        visited = {} # create dictionary for visited

        q = Queue() # create queue 
        q.enqueue([user_id]) # enqueue starting vertext

        while q.size() > 0: # while queue is not empty 
            path = q.dequeue() # we need to create the current path = to Dequeue 
            current_user = path[-1] # grab last vertext from path 

            # check if it has been visited
            if current_user not in visited:
                visited[current_user] = path # Add to dictionary for visited/ storing path to user
                for friend in self.friendships[current_user]: #
                    q.enqueue(path + [friend]) # enqueue paths to neighbors (path to friends)
                    
        return visited

if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(15, 3)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)

    users_in_ext_network = len(connections) - 1
    total_users = len(sg.users)

    print(f'Percentage: {users_in_ext_network / total_users * 100:.2f}')
