class WordSequenceGraph:

    def __init__(self, cohesion, uni_character_cost=-0.2):
        self.cohesion = cohesion
        self.uni_character_cost = uni_character_cost

    def as_graph(self, sentence):
        raise NotImplemented

    def _sentence_lookup(sentence):
        sent = []
        for eojeol in sentence.split():
            sent += word_lookup(eojeol, offset=len(sent))
        return sent

    def _word_lookup(eojeol, offset=0):
        n = len(eojeol)
        # (word, score, begin, end)
        words = [[(eojeol[i], 0, i, i+1)] for i in range(n)]
        for b in range(n):
            for r in range(2, self.cohesion.max_l_length+1):
                e = b+r
                if e > n:
                    continue
                sub = eojeol[b:e]
                score = self.cohesion[sub]
                if score > 0:
                    words[b].append((sub, score, b, e))
        return words