class WordSequenceGraph:

    def __init__(self, cohesion, uni_character_cost=-0.2):
        self.cohesion = cohesion
        self.uni_character_cost = uni_character_cost

    def as_graph(self, sentence):
        raise NotImplemented