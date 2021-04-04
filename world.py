import queue
import math
from node import Node

class World:
    def __init__(self, map, settings, agent):
        self.map = map
        self.settings = settings
        self.agent = agent

        (self.rows, self.columns) = self.map.shape

    def calculateBranchingFactor(self, n, d):
        b = n**(1/d)
        return b


    def discard_successors_marios_perspective(self, successors):
        filtered_successors = []

        for successor in successors:
            i = successor[0]
            j = successor[1]

            if 0 <= i < self.rows and 0 <= j < self.columns and \
                    (self.map[i][j] == self.settings.EMPTY or self.map[i][j] == self.settings.PIPE):
                filtered_successors.append(successor)

        return filtered_successors

   
   
    def find_position_shortest_pipe_from_A_algoritm(self, mario_position, pipe_position):
        open = queue.SimpleQueue()
        cost = 0
        expandedStates = 0
     

        # start A* from Mario:
        open.put(mario_position)


        while open.qsize() != 0:
            state = open.get()

            # Goal Test: return pipe's position
            if self.map[state[0]][state[1]] == self.settings.PIPE:
                branchingFactor = self.calculateBranchingFactor(expandedStates, cost)
                return True, state, branchingFactor

            # Mark state as visited
            self.map[state[0]][state[1]] = self.settings.VISITED

            # Transition Function
            actions = [self.settings.NORTH, self.settings.NORTHWEST, self.settings.NORTHEAST, self.settings.SOUTH, self.settings.SOUTHWEST, self.settings.SOUTHEAST, self.settings.WEST, self.settings.EAST]
            successors = self.agent.transition_function_A(state, actions)
            successors = self.discard_successors_marios_perspective(successors)

            expandedStates = len(successors) + expandedStates
            
            # calculate the heuristic function and the f value of the successors
            optionList = []
            for successor in successors:
                node = Node(successor, cost)
                node.calculateHeuristicFunction(pipe_position)
                node.calculateF()
                optionList.append(node)
            
            # calculate the best option to go
            minor = optionList[0]
            for i in range (0, len(optionList)):
                if(optionList[i].getF() < minor.getF()):
                    minor = optionList[i]
           
            # Put the best option into the queue
            toGo = [minor.ubication[0], minor.ubication[1]]
            open.put(toGo)
            
            #the cost increments
            cost = cost + 1

         # No solution
        return False, None, None


    def find_position_shortest_pipe_from(self, mario_position):
        open = queue.SimpleQueue()
        cost = 0
        expandedStates = 0
     

        # start bfs from Mario:
        open.put(mario_position)

        while open.qsize() != 0:
            state = open.get()

            # Goal Test: return pipe's position
            if self.map[state[0]][state[1]] == self.settings.PIPE:
                branchingFactor = self.calculateBranchingFactor(expandedStates, cost)
                return True, state, branchingFactor

            # Mark state as visited
            self.map[state[0]][state[1]] = self.settings.VISITED
            
            # Transition Function
            actions = [self.settings.NORTH, self.settings.SOUTH, self.settings.WEST, self.settings.EAST]
            successors = self.agent.transition_function_BFS(state, actions)
            successors = self.discard_successors_marios_perspective(successors)

            expandedStates = len(successors) + expandedStates
            
            # Put the successors into the queue
            for successor in successors:
                open.put(successor)

            #the cost increments
            cost = cost + 1

        # No solution
        return False, None, None

    

