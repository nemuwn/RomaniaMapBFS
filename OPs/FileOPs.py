import os
import shutil


def CD_results():
    os.chdir('..')

def create_city_dir(root):
    if not os.path.exists(root):
        os.makedirs(root)
    os.chdir(root)


def read_in_dict(filename):
    dict_graph = {}
    with open(filename, 'r') as f:
        for words in f:
            city_a, city_b, p_cost = words.split()
            if city_a not in dict_graph:
                dict_graph[city_a] = {}
            dict_graph[city_a][city_b] = int(p_cost)
            if city_b not in dict_graph:
                dict_graph[city_b] = {}
            dict_graph[city_b][city_a] = int(p_cost)
    return dict_graph


def print_dictionary(dictionary):
    for key in dictionary.keys():
        print(key, '->', dictionary[key])
    print('\n')

def display_dict(dictionary):
  
    print('\n')
    print_dictionary(dictionary)
           
