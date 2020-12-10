from collections import namedtuple

Node = namedtuple('Node', 'state parent cost')

class Astack:
    def __init__(self): self.container = list()
    def put(self, data): self.container.append(data)
    def pull(self): return self.container.pop()
    def empty(self): return not len(self.container)

class Aqueue(Astack):
    def __init__(self): super().__init__()
    def pull(self): return self.container.pop(0)

