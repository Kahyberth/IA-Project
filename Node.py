import numpy


class Nodo:

    def __init__(self, state, cost, father):
        self.state = state
        self.cost = cost
        self.father = father
        self.current_values = numpy.array([])


    def current_status(self):
        pass


