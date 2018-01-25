#! /usr/bin/python3
'''
Program: 5 - Sliding Puzzle Solver (Iterative Deepening Search)

Author:  Akshay S. Kale

Class: CSCI 8456 (Artificial Intelligence)

Assignment #1

'''

# Goal State
# 0 1 2
# 3 4 5

'''
FUNCTION NAME: main()
This is the main driver function.

'''
def main():
    startStateInput = input("Please Enter Initial State: ")
    startState = []
    for s in startStateInput:
        startState.append(int(s))
    goalState = [0,1,2,3,4,5]
    result = ids(startState, goalState)
    if result == None:
        print("No Solutions found")
    elif result ==[None]:
        print("The start node was the goal")
    else:
        print("The goal state is:")
        print(goalState)
        print("Solution: ")
        print(result)


'''
Definition of data structure node
with attributes
1. currentState
2. parent
3. move
4. pathCost
5. depth

'''
class Node:
    def __init__(self, currentState, parent, move, pathCost, depth):
        self.currentState = currentState
        self.parent = parent
        self.move = move
        self.pathCost = pathCost
        self.depth = depth

'''
FUNCTION NAME: createNode()
creates a object of the class node

INPUT PARAMETER: currentState, parent, move, pathCost, depth
OUTPUT: Returns an object of class Node with currentState, parent
         pathCost, depth
'''

def createNode(currentState, parent, move, pathCost, depth):
    return Node(currentState, parent, move, pathCost, depth)





'''
Below functions are finite number of different moves 
or actions performed on sliding puzzle
'''

'''
FUNCTION NAME: down()
performs down action on a tile above the empty tile
denoted by '0'

INPUT PARAMETER: 1. state : current state of the node.
OUTPUT: Returns new state after performing a down operation.

'''
def down(state):
    newState = state[:]
    index = newState.index(0)
    if index not in [0,1,2]:
        newState[index], newState[index -3] = newState[index - 3], newState[index] 
        return newState
    else:
        return None




'''
FUNCTION NAME: up()
performs up action on a tile below the empty tile
denoted by '0'

INPUT PARAMETER: 1. state : current state of the node.
OUTPUT: Returns new state after performing a up operation.

'''

def up(state):
    newState = state[:]
    index = newState.index(0)
    if index not in [3,4,5]:
       newState[index], newState[index + 3] = newState[index + 3], newState[index]
       return newState
    else:
       return None



'''
FUNCTION NAME: right()
performs right action on a tile to left the empty tile
denoted by '0'

INPUT PARAMETER: 1. state : current state of the node.
OUTPUT: Returns new state after performing a left operation.

'''

def right(state):
    newState = state[:]
    index = newState.index(0)
    if index not in [0,3]:
       newState[index], newState[index - 1] = newState[index - 1], newState[index]
       return newState
    else:
       return None

'''
FUNCTION NAME: left()
performs left action on a tile right the empty tile
denoted by '0'

INPUT PARAMETER: 1. state : current state of the node.
OUTPUT: Returns new state after performing a left operation.

'''

def left(state):
    newState = state[:]
    index = newState.index(0)
    if index not in [2,5]:
        newState[index], newState[index + 1] = newState[index + 1], newState[index]
        return newState
    else:
        return None



'''
FUNCTION NAME: Explorer()
Utility function to create new nodes (states) using four possible action:
    1. up
    2. down
    3. right
    4. left

INPUT PARAMETER: node
OUTPUT: Returns a list of all possible nodes (states)
'''
def Explorer(node):
    exploredTemp = []
    explored = []
    nodeUp    = createNode(down(node.currentState),node,"D", 0, node.depth + 1)
    nodeDown  = createNode(up(node.currentState), node,"U", 0, node.depth + 1)
    nodeRight = createNode(left(node.currentState), node, "L", 0, node.depth + 1)
    nodeLeft  = createNode(right(node.currentState),node, "R", 0, node.depth + 1)
    exploredTemp.append(nodeUp)
    exploredTemp.append(nodeDown)
    exploredTemp.append(nodeRight)
    exploredTemp.append(nodeLeft)

    for node in exploredTemp:
        if node.currentState != None:
            explored.append(node)

    return explored


'''
FUNCTION NAME: iddfs()
    Depth first search algorithm

INPUT PARAMETERS:
    1. startState - startState is the initial state the user is asked
    to enter.
   
    2. goalState - goalState is the desired state.

    3. depth - limited depth for Depth First Search

OUTPUT : returns a List of Solution (Moves):

'''

def iddfs(startState, goalState, depth):
    depthLimit = depth #setting depth limit
    fringe = [] # initializing fringe
    fringe.append(createNode(startState,None, None, 0, 0)) # adding our initial node into fringe
    while fringe:   # TO DO until fringe is not empty                 
          if len(fringe) == 0:
              return None
          node = fringe.pop() # pop the node out of fringe(stack)
          if node.currentState == goalState:  
              results = [] # initialized list, in which solutions will be contained
              tempNew = node

              # If the goal state is found, then reach the parent of the  and add moves that reached to results
              while True:  
                  results.insert(0,tempNew.move)
                  if tempNew.depth <= 1:
                      break
                  tempNew = tempNew.parent
              return results
          
          # If the depth limit is not reached then add possible nodes (states) to fringe 
          if depthLimit > node.depth:
             explored = Explorer(node)
             explored.extend(fringe)
             fringe = explored

'''
FUNCTION NAME: ids()
    The purpose of this function is to call depth first search
    iteratively from starting depth of 1

'''
def ids(startState, goalState, depth = 1000):
    for i in range(depth):
        result = iddfs(startState,goalState,i)
        if result != None:
            return result




# main function
if __name__ == "__main__":
  main()
