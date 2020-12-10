from aiUtils.datastructures import *

def actions(state_space, state):
    y, x = state 
    r = len(state_space) 
    c = len(state_space[0])
    nodes = list()
    #left
    if x-1 >= 0 and not state_space[y][x-1]:
        nodes.append((y, x-1))
    #right
    if x+1 < c and not state_space[y][x+1]: nodes.append((y, x+1))
    #up
    if y-1 >= 0 and not state_space[y-1][x]: nodes.append((y-1, x))
    # down
    if y+1 < r and not state_space[y+1][x]: nodes.append((y+1, x))
    return nodes

def transition_model(state, neighbours, cost_func, memo):
    neighbours = filter(lambda x: not x in memo, neighbours)
    nodes = list(map(lambda x: Node(x, state, cost_func(state)), neighbours))[::-1]
    memo.add(state)
    return nodes, memo

def track_path(graph, state):
    if not graph: raise Exception('Unable to track path from empty graph!')
    path = []
    cost = int()
    i = int()
    while state != None:
        node = graph[i%len(graph)]
        if node.state == state: 
            path.append(i%len(graph))
            cost += node.cost
            state = node.parent
        i += 1
    return cost, path[::-1]

def solve(state_space, start, end, cost_func, container=Astack()):
    memo = set()
    graph = list()
    location = Node(start, None, 0)
    graph.append(location)
    while not location.state == end:
        neighbours = actions(state_space, location.state)
        nodes, memo = transition_model(location.state, neighbours, cost_func, memo)
        graph.extend(nodes)
        for node in nodes: container.put(node)
        if container.empty(): return False
        location = container.pull()
    return location, graph
