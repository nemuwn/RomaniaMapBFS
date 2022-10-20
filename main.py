from time import sleep
from OPs import *

def BFSearch(graph, start, goal):
    explored = []
    queue = [[start]]
    cost = 0

    if start == goal:
        return "ali hediin ochson baina !"
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node not in explored:
            neighbors = graph[node]
    
            for neighbor in neighbors:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
                if neighbor == goal:
                    explored.append(goal)
                    return new_path, explored, cost

            explored.append(node)

    return "path oldsongui"


def main():
    in_file = "data.txt"
    goal = "Drobeta"

    city_map = read_in_dict(in_file)
    display_dict(city_map)
    root = verify_city_input(city_map)
    
    Status = True 
    search = 'Breadth-First_Search'
          
    res = BFSearch(city_map, root, goal)
    display_results(root, res, search)
        
    ExitRomania()


if __name__ == '__main__':
    main()
