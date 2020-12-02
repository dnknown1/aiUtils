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
    """
    Base Artificial Agent Class thst percieves a given envioronment and acts upon
    # defalut container is list
    """
    def __init__(self, state_space, start_state, end_state, container=list()):
        self.state_space = state_space
        self.container = container
        self.state = start_state
        self.goal = end_state
        self.memo = list()
        self.path = list()
        self.cost = None

    # override
    def transition(self):
        pass

    # override
    def action(self):
        pass

    # track path and cost
    def track(self):
        path = self.state
        while path:
            if self.state_space[path].cost:
                self.cost += self.state_space[path].cost
            self.path.append(path)
            path = self.state_space[path].parent
        self.path = self.path[::-1]

    # Only to run
    def explore(self):
        if self.state == self.goal:
            self.track()
            return True
        self.transition()
        self.action()
        return self.explore()

    def __reset(self):
        self.state_space = None
        self.container = None
        self.state = None
        self.goal = None
        self.memo = None
        self.path = None
        self.cost = None
