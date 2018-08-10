from .utils import _initialize_dict
from .utils import _print_changing
from .utils import _find_shortest_path_dict

def dijkstra(g, start, end, debug=False):
    if isinstance(g, dict):
        return _dijkstra_dict(g, start, end, debug)
    raise NotImplemented

def _dijkstra_dict(g, start, end, debug=False):
    if not ((start in g) and (end in g)):
        raise ValueError('start and end node should be exist in graph')

    n_nodes, n_edges, cost = _initialize_dict(g, start)

    raise NotImplemented