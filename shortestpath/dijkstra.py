from .utils import _set_nodes_dict
from .utils import _initialize_dict
from .utils import _print_changing
from .utils import _find_shortest_path_dict

def dijkstra(g, start, end, debug=False):
    if isinstance(g, dict):
        return _dijkstra_dict(g, start, end, debug)
    raise NotImplemented

def _dijkstra_dict(g, start, end, debug=False):
    from_nodes, to_nodes = _set_nodes_dict(g)
    if not ((start in from_nodes) and (end in to_nodes)):
        raise ValueError('There is no path {} - ... - {}'.format(start, end))

    n_nodes, n_edges, cost = _initialize_dict(g, start)
    unvisited = {node for node in from_nodes}
    unvisited.update(to_nodes)

    current = unvisited.pop(start)

    raise NotImplemented