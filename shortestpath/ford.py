from .utils import _set_nodes_dict
from .utils import _initialize_dict
from .utils import _print_changing
from .utils import _find_shortest_path_dict

def ford(g, start, end, debug=False):
    if isinstance(g, dict):
        return _ford_dict(g, start, end, debug)
    raise NotImplemented

def _ford_dict(g, start, end, debug=False):
    from_nodes, to_nodes = _set_nodes_dict(g)
    if not ((start in from_nodes) and (end in to_nodes)):
        raise ValueError('There is no path {} - ... - {}'.format(start, end))

    n_nodes, n_edges, cost = _initialize_dict(g, start)

    for _iter in range(n_nodes * n_edges):
        cost, changed = _update_ford_dict(g, cost, debug)
        if not changed:
            break
    paths = _find_shortest_path_dict(g, start, end, cost, n_nodes)
    return {'paths': paths, 'cost': cost[end]}

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