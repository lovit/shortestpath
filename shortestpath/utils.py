from scipy.io import mmread
from collections import defaultdict

def load_sparse_graph_and_index(header):
    x = mmread(header+'.mtx').tocsr()
    with open('{}.vocab'.format(header), encoding='utf-8') as f:
        idx2vocab = [vocab.strip() for vocab in f]
    return x, idx2vocab