from aiUtils.aiTools import Agent


class DfsAgent(Agent):
    def __init__(self, state_space, start, end):
        super().__init__(state_space, start, end)

    def transition(self):
        #print('Transition:-')
        acts = self.state_space[self.state].actions
        while acts:
            tmp = acts.pop(0)
            if not tmp in self.memo:
                self.container.append(tmp)
                #print(tmp, '<<is reachable from>>', self.state)
                self.state_space[tmp].parent = self.state

    def action(self):
        nxt = self.container.pop()
        self.memo.append(self.state)
        #print('visited:', self.state)
        self.state = nxt


#class BfsAgent
class BfsAgent(Agent):
    def __init__(self, state_space, start, end):
        super().__init__(state_space, start, end)

    def transition(self):
        #print('Transition:-')
        acts = self.state_space[self.state].actions
        while acts:
            tmp = acts.pop(0)
            if not tmp in self.memo:
                self.container.append(tmp)
                #print(tmp, '<<is reachable from>>', self.state)
                self.state_space[tmp].parent = self.state
        #print('visited:', self.state)
        self.memo.append(self.state)

    def action(self):
        #print('\nAction:-\ncontainer:', self.container)
        #print('memo:\t', self.memo)
        nxt = self.container.pop(0)
        #print(f'visiting {nxt}\n')
        self.state = nxt
