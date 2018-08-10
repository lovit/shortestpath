def ford(g, start, end, debug=False):
    if isinstance(g, dict):
        return _ford_dict(g, start, end, debug)
    raise NotImplemented

def _ford_dict(g, start, end, debug=False):
    if not ((start in g) and (end in g)):
        raise ValueError('start and end node should be exist in graph')

    n_nodes, n_edges, cost = _initialize_dict(g, start)

    for _iter in range(n_nodes * n_edges):
        cost, changed = _update_ford_dict(g, cost, debug)
        if not changed:
            break
    paths = _find_shortest_path_dict(g, start, end, cost, n_nodes)
    return {'paths': paths, 'cost': cost[end]}

def _initialize_dict(g, start):
    nodes = set(g.keys())
    nodes.update(set({n for nw in g.values() for n in nw.keys()}))
    n_nodes = len(nodes)
    n_edges = sum((len(nw) for nw in g.values()))
    max_weight = max(w for nw in g.values() for w in nw.values())

    init_cost = n_nodes * (max_weight + 1)
    cost = {node:(0 if node == start else init_cost) for node in g}
    return n_nodes, n_edges, cost

def _update_ford_dict(g, cost, debug=False):
    changed = False
    for from_, to_weight in g.items():
        for to_, weight in to_weight.items():
            if cost[to_] > cost[from_] + weight:
                before = cost[to_]
                after = cost[from_] + weight
                cost[to_] = after
                changed = True
                if debug:
                    _print_changing(from_, to_, before, after)
    return cost, changed

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