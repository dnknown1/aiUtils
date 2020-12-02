class Astack:
    def __init__(self): self.container = list()
    def put(self, data): self.container.append(data)
    def pull(self): return self.container.pop()
    def __contains__(self, key): return key in self.container
    def empty(self): return not len(self.container)

class Aqueue(Astack):
    def __init__(self): super().__init__()
    def pull(self): return self.container.pop(0)

class Node:
    """ 
    Base Node class: every states of actual problem to be converted into
    this datastructure. A node representes each point in the problem set
    """
    def __init__(self, state=None, action=None, cost=None):
        self.state = state
        self.actions = action
        self.cost = cost
        self.parent = None

    def __eq__(self, other):
        return self.state == other.state

class Problem:
    @staticmethod
    def to_statespace(problem):
        row = len(problem)
        col = len(problem[0])
        state_space = list()
        def set_action(loc, i):
            if i >= 0:
                if loc == state_space[i].state: return i
            return set_action(loc, i-1)

        # make nodes
        for i in range(row): # row
            for j in range(col): #column
                if not problem[i][j] == 1:
                    state_space.append(Node((i, j)))

        #find neighbours : set actions to Nodes
        for node in state_space:
            node.actions = set()
            i, j = node.state
            
            #right
            if (j+1) < col and not problem[i][j+1]:
                node.actions.append(set_action((i, j+1), len(state_space)-1))
            #up
            if (i-1) >= 0 and not problem[i-1][j]:
                node.actions.append(set_action((i-1, j), len(state_space)-1))
            #down
            if (i+1) < row and not problem[i+1][j]:
                node.actions.append(set_action((i+1, j), len(state_space)-1))
        return state_space
    
    @staticmethod
    def view_matrix(problem):
        for _,j in enumerate(problem): print(*j)
    @staticmethod
    def view_graph(state_space):
        print('Node', '=:>',  'state', '=:>', 'actions', '=:>', 'parent', '=:>', 'cost', '=:>')
        for i, state in enumerate(state_space):
            print(i, '=:>', state.state, '=:>', state.actions, '=:>', state.parent, '=:>', state.cost)

class Agent:
    def __init__(self, start_state, end_state, container):
        #self.state_space = state_space.copy()
        self.container = container
        self.state = start_state
        self.goal = end_state
        self.memo = list()
        self.path = list()
        self.cost = None
    def action(self):
        nxt = self.container.pull()
        self.memo.append(self.state)
        self.state = nxt

    def explore(self, state_space):
        if self.state == self.goal:
            return self.track(state_space, [self.state,])
        self.transition(state_space)
        self.action()
        return self.explore(state_space)

    def track(self, state_space,__path=list(), __cost=1):
        if not state_space[__path[-1]].parent:
            return (__cost, __path[::-1])
        if not state_space[__path[-1]].cost: __cost += 1 
        else: __cost +=  state_space[__path[-1]].cost
        __path.append(state_space[__path[-1]].parent)
        return self.track(state_space, __path, __cost)
    # Override
    def transition(self, state_space):
        acts = state_space[self.state].actions
        while acts:
            tmp = acts.pop(0)
            if not tmp in self.memo:
                self.container.put(tmp)
                state_space[tmp].parent = self.state

