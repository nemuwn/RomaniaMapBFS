import sys

def get_source_city():
    root = input("Ehlel:  ")
    root = root.capitalize()
    return root

def GetNewInput():
    answer = input("\nBuruu baina. Dahin oruulna uu.\n:  ")
    return answer

def printErrMsg():
    print("\nBuruu baina. Dahin oruulna uu.")

def is_city(root, dictionary):
    state = False
    for key in dictionary.keys():
        if root == key:
            state = True
            print(f"\n{root} to Drobeta\n")
    return state

def verify_city_input(data):
    count = 0
    user_inp = get_source_city()
    state = is_city(user_inp, data)
    while state is False:
        printErrMsg()
        user_inp = get_source_city()
        state = is_city(user_inp, data)
    return user_inp

def search_menu():
    options = [1, 2, 3]
    count = 0
    print("""
    1. Breadth-First Search (BFS)
    2. Shine city oruulah
    3. Exit\n""")

    answer = input(':  ')
    answer = int(answer)
    while answer not in options:
        count += 1
        answer = input('\n:')
        answer = int(answer)
        if count % 3 == 0:
            search_menu()
    return answer

def validate_action(input):
    count = 0
    t = 0
    while input not in range(1,6):
        count += 1
        i += 1
        print(i)
        input = GetNewInput()
        input = int(input)
        if count % 3 == 0:
            printErrMsg()
            search_menu()
        return input


def ExitRomania():
    sys.exit("Exiting...")
