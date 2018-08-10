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

def _print_changing(from_, to_, before, after):
    print('cost[{}]: {} -> {} (from {})'.format(
        to_, before, after, from_))

def _find_shortest_path_dict(g, start, end, cost, n_nodes):
    immatures = [[start]]
    mature = []
    n_iter = 0
    for _ in range(n_nodes):
        immatures_ = []
        for path in immatures:
            last = path[-1]
            for adjacent, c in g[last].items():
                if cost[adjacent] == cost[last] + c:
                    if adjacent == end:
                        mature.append([p for p in path] + [adjacent])
                    else:
                        immatures_.append([p for p in path] + [adjacent])
        immatures = immatures_
    return mature