class CohesionScore:
    def __init__(self, l_max_length=10):
        self.l_max_length = l_max_length
        self._scores = {}

    def __call__(self, word):
        return self.get_cohesion(word)

    def train(self, sentences):
        raise NotImplemented

    def get_cohesion(self, word):
        return self._scores.get(word, 0)