import numpy as np
from world import World
from settings import Settings
from agent import Agent
import math

def second_approach(Map):
    '''
    You can use this approach to compare BFS with A* algorithm
    '''

    inf = math.inf
    # define the map, inf represents an empty space, -1 represents a wall and 0 a pipe :D
    
    map = Map
    settings = Settings()
    agent = Agent(settings)
    world = World(map, settings, agent)
    mario_position = [0, 0]

    success, pipe_position, branchingFactor = world.find_position_shortest_pipe_from(mario_position)

    if success:
        print('Shortest pipe is at position:\n', pipe_position)
        print('the best road found by BFS\n', map)
        print('the branching Factor of BFS is: ', branchingFactor)
    else:
        print('No solution')


def third_approach(Map, goalState):

    # define the map, inf represents an empty space, -1 represents a wall and 0 a pipe :D
    map = Map

    settings = Settings()
    agent = Agent(settings)
    world = World(map, settings, agent)
    mario_position = [0, 0]
    pipe_position = goalState

    success, pipe_position, branchingFactor = world.find_position_shortest_pipe_from_A_algoritm(mario_position, pipe_position)

    
    
    if success:
        print('Shortest pipe is at position:\n', pipe_position)
        print('the best road found by A*\n', map)
        print('the branching Factor of A* is: ', branchingFactor)
    else:
        print('No solution')


def menu():

    inf = math.inf
    map = []

    print('Choose the difficult')
    print('1. easy')
    print('2. medium')
    print('3. hard')

    option = int(input())

    if option == 1:
        map = np.array([[inf, -1 , inf,  0],
                       [inf, inf, inf, -1],
                       [inf, -1 , inf, -1],
                       [inf, -1 , inf, inf]])

        goalState = [0, 3]
    
    if option == 2:
        map = np.array([[inf, -1 , -1,  -1, -1, -1, inf, inf, inf, inf],
                       [inf, inf, inf, -1, -1, -1, inf, inf, inf, inf],
                       [inf, -1 , inf, -1, inf, inf, inf, inf, inf, inf],
                       [inf, -1 , inf, -1, inf, inf, -1, -1, -1, inf],
                       [inf, -1,  inf, inf, inf, inf, inf, -1, -1, inf],
                       [-1,  -1,  inf, inf, -1, -1, inf, inf, -1, inf],
                       [-1,  -1,  inf, inf, inf, inf, inf, inf, 0, inf],
                       [inf, inf, inf, -1, -1, -1, inf, inf, inf, inf],
                       [inf, inf, inf, inf, inf, -1, inf, inf, inf, -1],
                       [inf, inf, -1, -1, -1, -1, inf, inf, -1, -1]])

        goalState = [6, 8]

    if option == 3:
        map = np.array([[inf, -1 , -1,  -1, -1, -1, inf, inf, inf, inf],
                       [inf, inf, inf, -1, -1, -1, inf, inf, inf, inf],
                       [inf, -1 , inf, -1, inf, inf, inf, inf, inf, inf],
                       [inf, -1 , inf, -1, inf, inf, -1, -1, -1, inf],
                       [inf, -1,  inf, inf, inf, inf, inf, -1, -1, inf],
                       [-1,  -1,  inf, inf, -1, -1, inf, inf, inf, inf],
                       [-1,  -1,  inf, inf, inf, inf, inf, -1, 0, inf],
                       [inf, inf, inf, -1, -1, -1, inf, -1, inf, inf],
                       [inf, inf, inf, inf, inf, -1, inf, inf, inf, -1],
                       [inf, inf, -1, -1, -1, -1, inf, inf, -1, -1]])       
       
        goalState = [6, 8]
   

    print('Choose a searching method:')
    print('1. BFS')
    print('2. A*')

    option = int(input())

    if option == 1:
        second_approach(map)
    if option == 2:
        third_approach(map, goalState)


def main():
    #first_approach()
    menu()
    #second_approach()
    #third_approach()


if __name__ == "__main__":
    main()

