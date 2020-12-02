class Agent():
    def __init__(self, state_space, start_state, end_state, container):
        self.state_space = state_space
        self.container = container
        self.state = start_state
        self.goal = end_state
        self.memo = list()
        self.path = list()
        self.cost = None

    def action(self):
        nxt = self.container.pop()
        self.memo.append(self.state)
        self.state = nxt
    
    def explore(self):
        if self.state == self.goal:
            self.track()
            return True
        self.transition()
        self.action()
        return self.explore()
    
    def track(self):
        path = self.state
        while path:
            if self.state_space[path].cost:
                self.cost += self.state_space[path].cost
            self.path.append(path)
            path = self.state_space[path].parent
        self.path = self.path[::-1]
    # Override
    def transition(self):
        acts = self.state_space[self.state].actions
        while acts:
            tmp = acts.pop(0)
            if not tmp in self.memo:
                self.container.append(tmp)
                self.state_space[tmp].parent = self.state

for class Astack:
    def __init__(self): self.container = list()
    def put(self, data): self.container.append(data)
    def pull(self): return self.container.pop()
    def __contains__(self, key): return key in self.container
    def empty(self): return not len(self.container)

class Aqueue(AIstack):
    def __init__(self): super().__init__()
    def pull(self): return self.container.pop(0)
    