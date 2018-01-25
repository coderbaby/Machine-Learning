#! /usr/bin/python3
'''
Program Title: 8 - Sliding Puzzle Solver (A STAR with Count of misplaced tiles as heuristics)

Author:  Akshay S. Kale

Class: CSCI 8456 (Artificial Intelligence)

Assignment #1

'''

# Goal State
# 0 1 2
# 3 4 5
# 6 7 8

'''
FUNCTION NAME: main()
This is the main driver function.

'''
def main():
    startStateInput = input("Please Enter Initial State: ")
    startState = []
    for s in startStateInput:
        startState.append(int(s))
    goalState = [0,1,2,3,4,5,6,7,8]
    result = astarMi(startState, goalState)
    if result == None:
        print("No Solutions found")
    elif result ==[None]:
        print("The start node was the goal")
    else:
        print("The goal state is:")
        print(goalState)
        print("Solution : ")
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
    if index not in [6,7,8]:
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
    if index not in [0,3,6]:
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
    if index not in [2,5,8]:
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
FUNCTION NAME: astarMi()
This function is an astar algorithm to

'''

def astarMi(startState, goalState):
    fringe = []
    start = createNode(startState,None,None,0, 0)
    start.pathCost = f(start,goalState)
    fringe.append(start)
    while fringe:
        if len(fringe) == 0:
            return None
        fringe.sort(key=lambda x: x.pathCost, reverse=False)
        node = fringe.pop(0)
        if node.currentState == goalState:
            results = []
            tempNew = node
            while True:
                results.insert(0,tempNew.move)
                if tempNew.depth <= 1:
                    break
                tempNew = tempNew.parent
            return results
        exploredList = Explorer(node)
        for explored_node in exploredList:
            explored_node.pathCost = f(explored_node, goalState)
        fringe.extend(exploredList)

'''

FUNCTION NAME: f()
   This is a evaluation function 
    f(n) = g(n) + h(n)
   
    1. f(n) = estimated total cost of path through n to goal.

    2. g(n) = cost so far to reach n 
       g(n) is the depth of the node so far.

    3. h(n) = estimated cost from n to reach goal
       h(n) is the heuristic function using misplaced tiles 

INPUT PARAMETERS: 
    1. node
    2. goalState

OUTPUT: Returns total estimated cost of the path through n to goal

'''
def f(node, goalState):
    return (node.depth + heuristicMisplacedTiles(node.currentState,goalState))


'''

FUNCTION NAME: heuristicMisplacedTiles()
     Counts the number of tiles that are not correctly places

INPUT PARAMETERS: 
      1. startState - startState is the node's current state,
      2. goalState - goalState is the desired state.

OUTPUT: Count of Misplaced Tiles

'''
def heuristicMisplacedTiles(startState, goalState):
    misplaced = 0
    for i, j in zip(startState, goalState):
        if i != j:
           misplaced += 1
    return misplaced




# main function
if __name__ == "__main__":
  main()
