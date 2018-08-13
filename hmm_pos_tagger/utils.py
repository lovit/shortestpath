class Dictionary:

    def __init__(self, pos2words=None):
        self.pos2words = pos2words if pos2words else {}
        self.max_len = self._set_max_len()

    def _set_max_len(self):
        if not self.pos2words: return 0
        return max((len(word) for words in pos2words.values() for word in words))

    def get_pos(self, word):
        return [pos for pos, words in self.pos2words.items() if word in words]