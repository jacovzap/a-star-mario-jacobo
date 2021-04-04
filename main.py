import numpy as np
from world import World
from settings import Settings
from agent import Agent
import math

def second_approach():
    '''
    You can use this approach to compare BFS with A* algorithm
    '''

    inf = math.inf
    # define the map, inf represents an empty space, -1 represents a wall and 0 a pipe :D
    map = np.array([[inf, -1 , inf,  0],
                    [inf, inf, inf, -1],
                    [inf, -1 , inf, -1],
                    [inf,   -1 , inf, inf]])

    settings = Settings()
    agent = Agent(settings)
    world = World(map, settings, agent)
    mario_position = [0, 0]

    success, pipe_position = world.find_position_shortest_pipe_from(mario_position)

    if success:
        print('Shortest pipe is at position:\n', pipe_position)
        print('the way explored by BFS\n', map)
    else:
        print('No solution')


def third_approach():

    inf = math.inf
    # define the map, inf represents an empty space, -1 represents a wall and 0 a pipe :D
    map = np.array([[inf, -1 , inf,  0],
                    [inf, inf, inf, -1],
                    [inf, -1 , inf, -1],
                    [inf,   -1 , inf, inf]])

    settings = Settings()
    agent = Agent(settings)
    world = World(map, settings, agent)
    mario_position = [0, 0]
    pipe_position = [0, 3]

    success, pipe_position = world.find_position_shortest_pipe_from_A_algoritm(mario_position, pipe_position)

    if success:
        print('Shortest pipe is at position:\n', pipe_position)
        print('the way explored by A*\n', map)
    else:
        print('No solution')



def main():
    #first_approach()
    second_approach()
    third_approach()


if __name__ == "__main__":
    main()

