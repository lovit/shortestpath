from scipy.io import mmread
from collections import defaultdict

def load_sparse_graph_and_index(header):
    x = mmread(header+'.mtx').tocsr()
    with open('{}.vocab'.format(header), encoding='utf-8') as f:
        idx2vocab = [vocab.strip() for vocab in f]
    return x, idx2vocab

def to_dict_graph(x, idx2vocab):
    def to_csr(i):
        return idx2vocab[i]

    rows, cols = x.nonzero()
    data = x.data
    d = defaultdict(lambda: {})
    for i, j, w in zip(rows, cols, data):
        d[to_csr(i)][to_csr(j)] = w
    return dict(d)