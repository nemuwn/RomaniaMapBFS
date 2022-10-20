import sys

def print_shortest(path):
    print("\nHamgiin bogino path:\n")
    print(path, '\n')


def print_other_routes(lists):
    if not lists:
        print("Zuvhun neg path baina.\n")
 

def display_results(root, result, search):
 
    print_shortest(result[0])
    print_other_routes(result[1])
  
